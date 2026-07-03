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
      f"(<= {N} patients, the sparse-support property; NPAG found 18).")
print("                          Ka(/h)  Ke(/h)   V(L)   Tlag(h)  CL=Ke*V(L/h)")
print(f"  open NPMLE (this work):  {mean[0]:.3f}  {mean[1]:.4f}  {mean[2]:.1f}   {mean[3]:.2f}    {mean[1]*mean[2]:.2f}")
print(f"  NPAG (bespoke, LAPKB) :  0.628  0.0514  77.8   1.19    4.00")

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
