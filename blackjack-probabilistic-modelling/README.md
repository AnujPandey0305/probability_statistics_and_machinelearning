# Blackjack — Probabilistic Modelling and Strategy Optimisation

**University of Manchester — BSc Mathematics | 2025**

**Research Project Grade: 81%**

Collaborative mathematical research project investigating probabilistic decision-making, expected payoff maximisation and stopping strategies in Blackjack.

## 1. Mathematical Framework

Developed a probabilistic framework for analysing composition-dependent Blackjack strategies under a specified four-deck game configuration.

- Modelled a 208-card shoe and conditional card probabilities.
- Derived payoff functions for different player actions.
- Analysed dealer outcome distributions using recursive probability formulations.
- Investigated expected payoffs for hitting, standing, doubling down and splitting.
- Examined decision-making under incomplete information.

## 2. Computational Probability Modelling

Implemented a Python probability calculator to enumerate possible dealer card sequences and aggregate terminal outcome probabilities.

The implementation incorporated:

- Conditional probabilities based on initially observed cards.
- Enumeration of possible dealer card sequences.
- Dynamic adjustment of ace values.
- Probability aggregation across terminal states.
- Expected payoff calculations.

### Results

For a player holding 10 and 7 against a dealer showing 6, the computational model produced the following approximate distribution:

| Dealer outcome | Probability |
|---|---:|
| Bust | 42.01% |
| 17 | 16.71% |
| 18 | 10.69% |
| 19 | 10.68% |
| 20 | 10.20% |
| 21 | 9.72% |

## 3. Expected Value and Decision Optimisation

Compared the expected payoffs associated with alternative player actions.

For the worked example above:

| Action | Estimated expected payoff |
|---|---:|
| Stand | +0.0072 |
| Hit once | -0.5020 |

The analysis demonstrated how conditional probability distributions and payoff functions can be combined to compare decisions under uncertainty.

Extended the mathematical framework to consider doubling down and splitting, outlining how expected value comparisons could be used to construct composition-dependent strategy tables.

## 4. House Edge and Stopping Strategies

Investigated the relationship between negative expected returns, short-term variance and cumulative losses.

- Examined a referenced theoretical house edge of approximately 0.3479% under the specified game configuration.
- Derived cumulative expected loss under a constant-wager, constant-house-edge model using linearity of expectation.
- Investigated the distinction between short-term outcome variability and long-term expected performance.
- Proposed an expected-loss-based stopping heuristic.

The analysis recognised that stopping rules cannot eliminate the underlying negative expectation of the game.

## 5. Model Limitations and Extensions

- The computational implementation approximates subsequent card draws using the initially adjusted shoe distribution rather than updating card frequencies along every branch.
- A fully composition-dependent implementation would track remaining card frequencies throughout the probability tree.
- The stopping heuristic was not established as a mathematically optimal stopping time.
- Further extensions could include dynamic programming, memoisation, Monte Carlo validation and formal optimal stopping analysis.

## Technical Skills

**Programming:** Python, algorithmic probability calculations, recursive modelling and numerical enumeration.

**Mathematics:** Conditional probability, combinatorics, expected value, probability distributions, stochastic modelling and decision theory.

**Research:** Mathematical derivation, computational modelling, literature review, quantitative analysis and critical evaluation of modelling assumptions.

## Academic Context

Completed as a collaborative undergraduate mathematical research project at the University of Manchester in April 2025.

This portfolio entry summarises the methodology, numerical findings and limitations without reproducing the original assessed report.

## Selected References

- Ethier, S. N. (2010). *The Doctrine of Chances: Probabilistic Aspects of Gambling*. Springer.
- Shackleford, M. *Blackjack House Edge Calculator*. Wizard of Odds.
