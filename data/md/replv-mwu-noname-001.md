# Efficient and Optimal Fixed-Time Regret with Two Experts

## Abstract

Prediction with expert advice is a foundational problem in online learning. In instances with $T$ rounds and $n$ experts, the classical Multiplicative Weights Update method suffers at most $\sqrt{(T/2)\ln n}$ regret when $T$ is known beforehand. Moreover, this is asymptotically optimal when both $T$ and $n$ grow to infinity. However, when the number of experts $n$ is small/fixed, algorithms with better regret guarantees exist. Cover showed in 1967 a dynamic programming algorithm for the two-experts problem restricted to $\{0,1\}$ costs that suffers at most $\sqrt{T/2\pi}+O(1)$ regret with $O(T^{2})$ pre-processing time. In this work, we propose an optimal algorithm for prediction with two experts’ advice that works even for costs in $[0,1]$ and with $O(1)$ processing time per turn. Our algorithm builds up on recent work on the experts problem based on techniques and tools from stochastic calculus.
