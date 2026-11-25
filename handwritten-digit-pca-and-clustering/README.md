# Handwritten Digit Recognition — PCA and Unsupervised Learning

**University of Manchester — BSc Mathematics | November 2025**

**Language: R**

Statistical machine learning project investigating dimensionality reduction, unsupervised clustering and image reconstruction using high-dimensional handwritten digit data.

## Key Results

- Achieved **97.83% clustering accuracy** using Ward's hierarchical clustering after matching clusters to true digit labels.
- Reduced feature dimensionality from 784 to 20, representing a **97.45% reduction in dimensionality**.
- Reduced clustering errors by **86.23%** compared with K-means.
- Analysed 3,000 handwritten digit images across three digit classes.

## 1. Dataset

The dataset consisted of 3,000 grayscale handwritten images of the digits 5, 6 and 7.

| Dataset characteristic | Value |
|---|---:|
| Observations | 3,000 |
| Digit classes | 3 |
| Observations per class | 1,000 |
| Image resolution | 28 × 28 |
| Original feature dimensions | 784 |
| Reduced feature dimensions | 20 |

## 2. Principal Component Analysis

Implemented PCA directly using covariance matrix eigendecomposition rather than relying on a dedicated PCA function.

The methodology involved:

- Mean-centring high-dimensional pixel data.
- Computing the covariance matrix.
- Extracting eigenvalues and eigenvectors.
- Projecting observations onto principal component directions.
- Analysing eigenvalue decay using scree plots.
- Visualising class separation in the reduced feature space.

The original 784-dimensional feature space was reduced to 20 principal components for subsequent clustering.

## 3. Unsupervised Machine Learning

Investigated five clustering approaches using the reduced-dimensional representations:

- K-means clustering.
- Ward's hierarchical clustering.
- Average linkage hierarchical clustering.
- Complete linkage hierarchical clustering.
- Single linkage hierarchical clustering.

Hierarchical clustering was performed using Euclidean distances between PCA representations.

Ward's method produced the strongest separation between the three digit classes.

### Performance Comparison

| Digit | K-means | Ward's method |
|---|---:|---:|
| 5 | 59.90% | 95.10% |
| 6 | 94.20% | 98.80% |
| 7 | 98.70% | 99.60% |
| **Overall** | **84.27%** | **97.83%** |

### Ward's Clustering Results

| True digit | Cluster 1 | Cluster 2 | Cluster 3 |
|---|---:|---:|---:|
| 5 | 951 | 46 | 3 |
| 6 | 12 | 988 | 0 |
| 7 | 4 | 0 | 996 |

Ward's hierarchical clustering correctly grouped 2,935 of the 3,000 observations after matching clusters to digit labels.

Dendrogram analysis further demonstrated the separation of observations into three principal groups.

## 4. Image Reconstruction

Derived the inverse PCA transformation using the orthogonality of the eigenvector matrix.

Investigated low-rank image reconstruction using:

- 1 principal component.
- 2 principal components.
- 5 principal components.
- 10 principal components.

This component of the project explored the relationship between dimensionality reduction, information loss and image reconstruction quality.

## 5. Limitations and Potential Extensions

- Clustering performance was evaluated on the analysed dataset rather than an independent test set.
- The dataset was restricted to three digit classes.
- Reconstruction requires correct feature-wise restoration of the mean pixel intensities.
- Further extensions could investigate additional digit classes, alternative dimensionality reduction methods, clustering stability and quantitative reconstruction error.

## Technical Skills

**Programming:** R, matrix computation, statistical computing and data visualisation.

**Mathematics:** Linear algebra, eigendecomposition, covariance matrices, orthogonal transformations and low-rank approximations.

**Machine Learning:** PCA, unsupervised learning, K-means, hierarchical clustering, feature extraction and model evaluation.

## Academic Context

Completed as an individual undergraduate statistical computing project at the University of Manchester.

This portfolio entry summarises the methodology and principal findings without reproducing the original assessed coursework or dataset.
