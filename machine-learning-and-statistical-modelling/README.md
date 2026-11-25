# Machine Learning and Statistical Modelling

**University of Manchester — BSc Mathematics | 2026**

A collection of mathematical and computational investigations into supervised learning, statistical modelling, sparse regression, natural language processing and financial time-series forecasting.

## 1. Financial Time-Series Forecasting

Developed a multi-output Ridge regression model to forecast next-day GBP/EUR and GBP/USD exchange rates.

### Methodology

- Constructed lagged features using the previous 10 trading days.
- Predicted eight outputs simultaneously, covering opening, closing, high and low exchange rates for both currency pairs.
- Applied feature standardisation and L2 regularisation.
- Evaluated performance using a chronological 80/20 train-test split.
- Compared predictions against a naive persistence baseline using 1,108 test trading days.

### Results

| Metric | Persistence baseline | Ridge regression | Error reduction |
|---|---:|---:|---:|
| MAE | 0.003761 | 0.003192 | 15.15% |
| RMSE | 0.005371 | 0.004704 | 12.42% |

The model achieved lower prediction errors than the persistence baseline over the evaluated historical period. These results measure forecasting accuracy rather than trading profitability.

## 2. Natural Language Processing and Multiclass Classification

Developed a probabilistic classifier for categorising newsgroup documents across 20 topics.

### Methodology

- Analysed a corpus of 11,314 documents.
- Constructed 500-dimensional word-frequency feature vectors.
- Implemented a standardised multinomial logistic regression pipeline.
- Generated class probability predictions.
- Evaluated accuracy and multiclass logarithmic loss using a stratified 80/20 split.

### Results

| Metric | Result |
|---|---:|
| Training observations | 9,051 |
| Test observations | 2,263 |
| Classification accuracy | 60.23% |
| Majority-class baseline | 5.30% |
| Absolute accuracy improvement | 54.93 percentage points |
| Log loss | 2.0174 |

Evaluation limitation: the vocabulary was constructed before splitting the dataset, introducing potential feature-selection leakage.

## 3. Sparse Regression and Numerical Linear Algebra

Implemented two iterative thresholding algorithms for sparse least-squares regression from scratch using NumPy.

- Computed minimum-norm least-squares solutions using the Moore–Penrose pseudoinverse.
- Implemented simultaneous elimination of coefficients below a specified threshold.
- Implemented sequential elimination of the smallest coefficient.
- Investigated the relationship between sparsity, threshold selection and coefficient of determination using the diabetes dataset.

## 4. Supervised Learning Algorithms

Implemented fundamental machine learning algorithms from scratch using Python and NumPy.

- Empirical risk minimisation under L1 loss.
- Optimal predictions using componentwise medians.
- K-nearest neighbours with a custom distance function.
- Deterministic neighbour ordering and classification tie-breaking.
- Astronomical object classification using KNN and decision trees.
- Feature standardisation and model hyperparameter selection.

## 5. Statistical Analysis of UK Housing Markets

Conducted exploratory statistical analysis of historical UK housing market data using pandas and NumPy.

- Data cleaning and missing-value handling.
- Regional sales aggregation.
- Historical house price analysis.
- Quantile-based comparisons of regional property prices.
- Construction of normalised regional house price indices.
- Investigation of seasonal patterns in flat prices.

## Technical Skills

**Languages:** Python

**Libraries:** NumPy, pandas, scikit-learn

**Mathematical methods:** Empirical risk minimisation, regularisation, numerical linear algebra, sparse regression, probability estimation, statistical learning and time-series forecasting.

**Machine learning:** Ridge regression, logistic regression, K-nearest neighbours, decision trees, feature engineering, model evaluation and NLP.

## Academic Context

Completed as part of undergraduate mathematics coursework at the University of Manchester. This portfolio entry summarises the implemented methods and experimental results without reproducing the original assessment materials.
