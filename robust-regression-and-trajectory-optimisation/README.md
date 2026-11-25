# Robust Regression and Trajectory Optimisation

**Imperial College London — MSc Applied Mathematics | 2026**

Collaborative academic project investigating convex and non-convex optimisation methods for parameter estimation in the presence of noisy and corrupted observations.

## Robust Regression

- Compared ordinary least squares with Huber loss regression.
- Investigated numerical conditioning using Legendre and monomial polynomial bases.
- Implemented gradient descent with a theoretically motivated constant step size.
- Analysed local Hessian eigenvalues, convergence rates and sensitivity to the Huber parameter.
- Identified six outliers using residual analysis.

### Results

| Metric | Result |
|---|---:|
| Least squares validation MSE | 0.345717 |
| Best Huber regression validation MSE | 0.000269 |
| Validation MSE reduction | 99.92% |
| Condition number improvement using Legendre basis | Approximately 444× |

## Non-Convex Trajectory Optimisation

- Investigated moving target localisation using noisy range measurements.
- Analysed stationary points, Hessian definiteness and non-convex objective functions.
- Compared linearised least squares with nonlinear gradient-based optimisation.
- Introduced temporal regularisation to improve trajectory estimation.
- Investigated reflection ambiguity, initialisation sensitivity and regularisation trade-offs.

### Results

| Method | Checkpoint error |
|---|---:|
| Linearised least squares | 1.0387 |
| Gradient descent | 0.4253 |
| Regularised trajectory estimation | 0.1463 |

Temporal regularisation reduced checkpoint error by approximately 85.9% relative to linearised least squares.

## Mathematical Methods

Convex optimisation, non-convex optimisation, gradient descent, numerical linear algebra, robust statistics, Hessian analysis, regularisation and convergence analysis.

## Academic Context

This project was completed collaboratively as part of the Optimisation module at Imperial College London. The results reported above relate to the coursework datasets and experiments.
