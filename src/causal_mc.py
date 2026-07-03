#!/usr/bin/env python3
"""Executed import (paper 1): causal panel-data estimation imports recommender-systems low-rank matrix
completion. The system surfaces the kinship (the political-methodology ideal-points paper retrieves the
recommender-systems factorization paper pca-recsys-001 as a cross-field neighbor; both are low-rank
factorization of a sparse preference/outcome matrix). Here we IMPORT the standard recsys solver
(SoftImpute: iterated SVD soft-thresholding) in place of the bespoke econometric counterfactual
estimator (two-way fixed effects) and measure counterfactual accuracy.

Shared computational problem: fill the unobserved (treated) entries of an N-unit x T-period outcome
matrix whose untreated potential outcomes are approximately low-rank. Two-way fixed effects assumes an
additive unit-plus-time structure; matrix completion (Athey et al., JASA 2021) recovers the full
low-rank structure and nests fixed effects, so it should estimate the held-out counterfactual better.

Offline, numpy only. Synthetic low-rank panel with a fixed seed, so it reproduces exactly.
"""
import numpy as np

rng = np.random.default_rng(0)
N, T, rank = 60, 40, 4
U, V = rng.normal(size=(N, rank)), rng.normal(size=(T, rank))
L = (U @ V.T) / np.sqrt(rank)                                   # true low-rank untreated outcomes
L += 0.6 * rng.normal(size=(N, 1)) + 0.6 * rng.normal(size=(1, T))  # + additive unit/time (FE is fair)
Y = L + 0.3 * rng.normal(size=(N, T))                          # observed = signal + noise

Ntreat, Tpost = 20, 8
mask = np.ones((N, T), bool)                                    # True = observed (control)
mask[:Ntreat, T - Tpost:] = False                              # treated-and-post block = to impute
true_cf = L[:Ntreat, T - Tpost:]                              # the untreated counterfactual we want


def two_way_fe(Y, mask, iters=500):                            # bespoke additive estimator
    mu = Y[mask].mean()
    a, b = np.zeros(N), np.zeros(T)
    for _ in range(iters):
        R = Y - mu - b[None, :]
        a = np.array([R[i, mask[i]].mean() if mask[i].any() else 0.0 for i in range(N)])
        R = Y - mu - a[:, None]
        b = np.array([R[mask[:, j], j].mean() if mask[:, j].any() else 0.0 for j in range(T)])
    return mu + a[:, None] + b[None, :]


def soft_impute(Y, mask, lam, iters=500):                     # imported recsys solver
    Z = np.where(mask, Y, 0.0)
    for _ in range(iters):
        filled = np.where(mask, Y, Z)
        Uu, s, Vt = np.linalg.svd(filled, full_matrices=False)
        s = np.maximum(s - lam, 0.0)
        Znew = (Uu * s) @ Vt
        if np.linalg.norm(Znew - Z) / (np.linalg.norm(Z) + 1e-9) < 1e-6:
            return Znew
        Z = Znew
    return Z


fe = two_way_fe(Y, mask)
rmse_fe = np.sqrt(((fe[:Ntreat, T - Tpost:] - true_cf) ** 2).mean())

# choose the soft-threshold lambda by holding out a fifth of the OBSERVED entries (no peeking at treated)
obs = np.argwhere(mask)
val = rng.choice(len(obs), size=len(obs) // 5, replace=False)
vmask = mask.copy()
for k in val:
    vmask[tuple(obs[k])] = False
best = None
for lam in np.linspace(0.5, 7.0, 14):
    Z = soft_impute(Y, vmask, lam)
    e = np.sqrt(np.mean([(Z[tuple(obs[k])] - Y[tuple(obs[k])]) ** 2 for k in val]))
    best = (e, lam) if best is None or e < best[0] else best
lam = best[1]
mc = soft_impute(Y, mask, lam)
rmse_mc = np.sqrt(((mc[:Ntreat, T - Tpost:] - true_cf) ** 2).mean())

print(f"synthetic panel: {N} units x {T} periods, true rank {rank}; treated block "
      f"{Ntreat} units x {Tpost} periods held out as the counterfactual\n")
print("                                                  counterfactual RMSE")
print(f"  bespoke two-way fixed effects (additive)        : {rmse_fe:.3f}")
print(f"  imported SoftImpute matrix completion (rank {np.linalg.matrix_rank(mc)}, lam {lam:.1f}): {rmse_mc:.3f}")
print(f"\nimporting the recsys completion solver cuts counterfactual error by "
      f"{100*(rmse_fe-rmse_mc)/rmse_fe:.0f}% vs the bespoke additive estimator, by using the low-rank "
      f"structure\nthat fixed effects cannot represent (Athey et al.'s result, reproduced offline).")
