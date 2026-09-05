#!/usr/bin/env python3
"""Executed import (paper 1): reproduce the bespoke nonparametric population-PK method (NPAG, from
LAPKB, the lab in our isomorphism trace) with an OPEN nonparametric-maximum-likelihood / support-point
solver on LAPKB's own NPAG example data, and compare to NPAG's output.

The isomorphism (concepts.md section 2): NPAG estimates the population parameter distribution as a set
of discrete SUPPORT POINTS maximizing the joint likelihood = the NPMLE of a mixing distribution
(Lindsay 1983, Mallet 1986). Its solution is SPARSE (<= N support points), found at the maxima of the
likelihood-gradient (Schumitzky's NPEM). The same nonparametric-mixture computation appears in machine
learning, astronomy, and nuclear physics under other names. We solve the SAME NPMLE with a plain open EM
(no NPAG, no proprietary software) and check whether it recovers NPAG's population estimates.

Model (genmodel.txt): 1-compartment, first-order oral absorption + lag. Params Ka, Ke, V, Tlag.
"""
import numpy as np

# NPAG's own result on the same data, read from LAPKB's completed run report shipped beside the data
# (data/vanco/NP_RF0001.TXT, Pmetrics NPAG engine 1.8, Oct 2015): the final-cycle population means and
# the number of active support points. NPAG itself is not run here.
def npag_reference(path="data/vanco/NP_RF0001.TXT"):
    L = open(path).read().split("\n")
    start = next(i for i, l in enumerate(L) if "# START CYCLE MEANS" in l)
    end = next(i for i, l in enumerate(L) if "# START CYCLE STD. DEVS." in l)
    s0, s1 = int(L[start].split()[0]), int(L[end].split()[0])
    vals = [float(l) for l in L[s0:s1] if l.strip() and not l.strip().startswith("#")]
    ka, ke, v, tlag = vals[-4:]
    nact = int(next(l for l in L if "NACTVE FOR ALL" in l).split()[0])
    return ka, ke, v, tlag, nact


def num(x):
    return None if x in (".", "") else float(x)

def parse(path):
    pts = {}
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("POPDATA"):
            continue
        f = line.split(",")
        pid, evid = f[0], f[1]
        time, dur, dose, out = num(f[2]), num(f[3]), num(f[4]), num(f[8])
        p = pts.setdefault(pid, {"doses": [], "obs": []})
        if evid == "1":
            p["doses"].append((time, dose, dur or 0.0))
        elif evid == "0" and out is not None:
            p["obs"].append((time, out))
    return pts

def conc(params, doses, t):
    Ka, Ke, V, Tlag = params
    c = 0.0
    for (td, D, dur) in doses:
        dt = t - td - Tlag
        if dt > 0:
            if abs(Ka - Ke) < 1e-6:
                c += D / V * Ke * dt * np.exp(-Ke * dt)        # equal-rates limit
            else:
                c += D * Ka / (V * (Ka - Ke)) * (np.exp(-Ke * dt) - np.exp(-Ka * dt))
    return max(c, 1e-9)

def sd(y):
    return max(5.0 * (0.02 + 0.05 * y - 0.0002 * y * y), 0.5)  # Pmetrics assay error x gamma

pts = parse("data/vanco/gendata.csv")
ids = [i for i in pts if pts[i]["obs"]]
N = len(ids)
nobs = sum(len(pts[i]["obs"]) for i in ids)
print(f"{N} patients with observations, {nobs} concentration measurements\n")

# fixed 4-D grid over (Ka, Ke, V, Tlag) (the NPEM approach; NPAG adapts the grid instead)
grid = [(ka, ke, v, tl)
        for ka in np.linspace(0.1, 0.9, 10)
        for ke in np.linspace(0.005, 0.1, 10)
        for v in np.linspace(30, 120, 10)
        for tl in (0.0, 0.5, 1.0, 1.5, 2.0)]
K = len(grid)

L = np.zeros((N, K))
for i, pid in enumerate(ids):
    obs, doses = pts[pid]["obs"], pts[pid]["doses"]
    for k, th in enumerate(grid):
        ll = 0.0
        for (t, y) in obs:
            pred = conc(th, doses, t)
            s = sd(y)
            ll += -0.5 * ((y - pred) / s) ** 2 - np.log(s)
        L[i, k] = ll
L = np.exp(L - L.max(axis=1, keepdims=True))  # per-patient normalize for numerical stability

# NPMLE via EM (the open nonparametric-MLE / support-point solver)
w = np.ones(K) / K
converged = False
for it in range(60000):
    denom = L @ w
    w_new = w * (L / denom[:, None]).mean(axis=0)
    w_new /= w_new.sum()
    if np.abs(w_new - w).max() < 1e-10:
        converged = True
        break
    w = w_new

G4 = np.array([g[:4] for g in grid])
mean = w @ G4
support = sorted([(grid[k], w[k]) for k in range(K) if w[k] > 1e-3], key=lambda x: -x[1])
print(f"NPMLE (open EM) {'converged' if converged else 'did NOT converge'} in {it + 1} iters.")
print(f"SPARSE support: {len(support)} support points with weight > 1e-3, out of {K} grid points "
      f"(<= {N} patients, the sparse-support property; NPAG found {npag_reference()[4]}).")
print("                          Ka(/h)  Ke(/h)   V(L)   Tlag(h)  CL=Ke*V(L/h)")
print(f"  open NPMLE (this work):  {mean[0]:.3f}  {mean[1]:.4f}  {mean[2]:.1f}   {mean[3]:.2f}    {mean[1]*mean[2]:.2f}")
ka_r, ke_r, v_r, tlag_r, nact_r = npag_reference()
print(f"  NPAG (bespoke, LAPKB) :  {ka_r:.3f}  {ke_r:.4f}  {v_r:.1f}   {tlag_r:.2f}    {ke_r*v_r:.2f}")

# individual fit quality: posterior-mean prediction vs observed
err = []
for i, pid in enumerate(ids):
    post = w * L[i]
    post /= post.sum()
    for (t, y) in pts[pid]["obs"]:
        pred = sum(post[k] * conc(grid[k], pts[pid]["doses"], t) for k in range(K))
        err.append((y - pred) / y)
err = np.array(err)
print(f"\nindividual Bayesian-posterior predictions vs observed: mean abs rel error "
      f"{np.abs(err).mean()*100:.1f}%, bias {err.mean()*100:+.1f}% (n={len(err)})")
