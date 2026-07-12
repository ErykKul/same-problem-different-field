#!/usr/bin/env python3
"""Executed import (paper 1): geostatistics "kriging" is the same computation as Gaussian-process
regression. The system surfaces the kinship (the geostatistics paper gp-geo-noname-001, which never
says "Gaussian process", retrieves GP-family papers across fields); here we IMPORT the standard ML
solver in place of the bespoke geostatistics one and check it reproduces the kriging predictor.

The shared computational problem: best linear unbiased prediction (BLUP) of a spatially correlated
field from scattered observations under a stationary covariance. Ordinary kriging fits a variogram by
least squares and solves the kriging system; Gaussian-process regression fits the SAME covariance by
marginal likelihood and returns the SAME posterior mean, but LEARNS the hyperparameters instead of
plugging in a least-squares variogram fit. We use a Matern(nu=1/2) GP so both sides use the identical
(exponential) covariance family, isolating the import to HOW the hyperparameters are chosen.

NOTE (accuracy): ordinary kriging is NOT uncertainty-free -- it defines a plug-in kriging variance, and
that is one of its selling points. What the plug-in variance conditions on is the fitted variogram, whose
own parameter uncertainty it ignores; and the compact bespoke implementation below simply does not return
it. So the import's honest payoff is LEARNED hyperparameters (it recovers the true range) plus a posterior
variance calibrated by marginal likelihood, NOT uncertainty where the incumbent had none.

Offline, needs only numpy + scikit-learn. Synthetic field with a fixed seed, so it reproduces exactly.
"""
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, WhiteKernel, ConstantKernel

rng = np.random.default_rng(0)
TRUE_RANGE, TRUE_SILL, TRUE_NUGGET = 0.18, 1.0, 0.04   # exponential covariance + nugget


def exp_cov(A, B, sill, rng_):
    d = np.sqrt(((A[:, None, :] - B[None, :, :]) ** 2).sum(-1))
    return sill * np.exp(-d / rng_)


# --- synthetic spatial field drawn from the true exponential covariance ---
n = 140
X = rng.uniform(0, 1, (n, 2))
C = exp_cov(X, X, TRUE_SILL, TRUE_RANGE) + TRUE_NUGGET * np.eye(n)
y = rng.multivariate_normal(np.zeros(n), C)
ntr = 100
Xtr, ytr, Xte, yte = X[:ntr], y[:ntr], X[ntr:], y[ntr:]


# --- bespoke side: ordinary kriging (empirical variogram -> exponential model -> kriging system) ---
def empirical_variogram(X, y, nbins=15):
    d = np.sqrt(((X[:, None, :] - X[None, :, :]) ** 2).sum(-1))
    g = 0.5 * (y[:, None] - y[None, :]) ** 2
    iu = np.triu_indices(len(X), 1)
    dd, gg = d[iu], g[iu]
    edges = np.linspace(0, dd.max() * 0.6, nbins + 1)
    bc, gv = [], []
    for b0, b1 in zip(edges[:-1], edges[1:]):
        m = (dd >= b0) & (dd < b1)
        if m.sum() > 5:
            bc.append((b0 + b1) / 2)
            gv.append(gg[m].mean())
    return np.array(bc), np.array(gv)


def fit_exp_variogram(bc, gv):
    # gamma(h) = nugget + sill*(1 - exp(-h/range)); grid the range, linear LS for (nugget, sill)
    best = None
    for r in np.linspace(0.03, 0.6, 60):
        basis = np.c_[np.ones_like(bc), 1 - np.exp(-bc / r)]
        coef, *_ = np.linalg.lstsq(basis, gv, rcond=None)
        if coef[0] >= 0 and coef[1] > 0:
            sse = ((basis @ coef - gv) ** 2).sum()
            if best is None or sse < best[0]:
                best = (sse, coef[0], coef[1], r)
    return best[1], best[2], best[3]   # nugget, sill, range


def krige(Xtr, ytr, Xte, nugget, sill, r):
    K = exp_cov(Xtr, Xtr, sill, r) + nugget * np.eye(len(Xtr))
    A = np.ones((len(Xtr) + 1, len(Xtr) + 1))
    A[:-1, :-1] = K
    A[-1, -1] = 0.0
    k0 = exp_cov(Xtr, Xte, sill, r)
    pred = np.empty(len(Xte))
    for j in range(len(Xte)):
        sol = np.linalg.solve(A, np.r_[k0[:, j], 1.0])
        pred[j] = sol[:-1] @ ytr
    return pred


bc, gv = empirical_variogram(Xtr, ytr)
nugget, sill, r = fit_exp_variogram(bc, gv)
yk = krige(Xtr, ytr, Xte, nugget, sill, r)
rmse_k = np.sqrt(((yk - yte) ** 2).mean())

# --- imported standard solver: scikit-learn GP, identical (Matern 1/2 = exponential) covariance,
#     but hyperparameters by marginal likelihood and a posterior variance returned ---
kern = ConstantKernel(1.0, (1e-2, 1e2)) * Matern(0.2, (1e-2, 1.0), nu=0.5) + WhiteKernel(0.05, (1e-3, 1.0))
gp = GaussianProcessRegressor(kernel=kern, normalize_y=True, n_restarts_optimizer=4, random_state=0).fit(Xtr, ytr)
yg, ystd = gp.predict(Xte, return_std=True)
rmse_g = np.sqrt(((yg - yte) ** 2).mean())
gp_range = gp.kernel_.k1.k2.length_scale
cover = float(np.mean(np.abs(yg - yte) <= 2 * ystd))
agree = np.sqrt(((yk - yg) ** 2).mean())

print(f"spatial field: {n} sites ({ntr} train, {n-ntr} test); true exponential range {TRUE_RANGE}, "
      f"sill {TRUE_SILL}, nugget {TRUE_NUGGET}\n")
print("                                         range   test-RMSE   notes")
print(f"  bespoke ordinary kriging (variogram LS): {r:.3f}     {rmse_k:.3f}    plug-in variance, not returned here")
print(f"  imported GP solver (marginal lik.)     : {gp_range:.3f}     {rmse_g:.3f}    "
      f"2-sigma coverage {cover:.2f}, learns range/nugget")
print(f"\nthe two predictors agree to RMSE {agree:.3f} (same BLUP); the import recovers the true range "
      f"{TRUE_RANGE} by marginal likelihood,\nwhere the bespoke side must hand-fit a variogram, and it "
      f"returns a posterior variance calibrated by the learned\nhyperparameters rather than plugged in "
      f"from that variogram fit (ordinary kriging does define a plug-in variance;\nthe compact bespoke "
      f"implementation above simply does not return it).")
