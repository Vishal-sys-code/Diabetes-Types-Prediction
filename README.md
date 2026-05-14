# Unsupervised Stratification of Diabetes Subtypes via K-Means Clustering

## Overview

This repository contains the official codebase, research documentation, and experimental notebooks for our novel approach to diabetes subtype classification. Moving beyond traditional binary classification (presence/absence of diabetes), this work introduces an unsupervised learning methodology utilizing K-Means clustering to discover latent diabetes subtypes based on clinical phenotypes: glucose levels, age, and pregnancy count.

This work was developed with the rigor and analytical depth characteristic of modern clinical machine learning research, aiming to provide medical practitioners with nuanced prognostic markers for tailored therapeutic interventions.

## Repository Structure

- `diabetes-and-it-s-type-prediction-notebook-2-0.ipynb`: **[New]** The latest, most comprehensive iteration of our modeling pipeline. Includes advanced preprocessing, hyperparameter optimization for clustering (using Silhouette Score and Calinski-Harabasz Index), and robust evaluation frameworks.
- `diabetes-prediction-and-it-s-types.ipynb`: The original baseline experimental notebook detailing the initial proof-of-concept.
- `research_paper.pdf`: The official research manuscript detailing the theoretical foundation, methodology, and comprehensive experimental results. 
- `app.py`: Web application logic for clinical deployment and inference.
- `kmeans_model.pkl`: The serialized, production-ready K-Means clustering model.
- `NCSU_Dataset.csv` / `Diabetes_Medical_Dataset(India).csv`: The foundational clinical datasets utilized for model training and validation.

## Research Paper

For a deep dive into the theoretical framework, mathematical formulation of the clustering approach, and extended empirical results, please refer to our full manuscript:

📄 **[Read the Research Paper Here](./research_paper.pdf)**

## Methodology

### 1. Data Processing and Feature Representation
We leverage the NC State University (NCSU) Diabetes Dataset, comprising 769 patient records. The initial phase involves rigorous preprocessing to address missing clinical markers and isolate the most predictive features. The pipeline begins with a robust binary classification mechanism to accurately identify the presence of diabetes.

### 2. Unsupervised Subtype Discovery
Following binary classification, we apply K-Means clustering to stratify the diabetic patient population. Through empirical analysis (Elbow method and Silhouette scoring), we identified **three distinct optimal clusters (k=3)**. The clustering operates primarily on:
- Fasting Glucose Levels
- Patient Age
- Pregnancy History

These features exhibited the highest latent correlation with distinct diabetic physiological profiles.

### 3. Evaluation Metrics
The integrity of the discovered clusters is quantitatively validated using:
- **Silhouette Score**: To measure intra-cluster cohesion and inter-cluster separation.
- **Calinski-Harabasz Index**: To evaluate the ratio of between-cluster variance to within-cluster variance, ensuring statistically significant stratification.

## Getting Started

### Prerequisites

We recommend using a virtual environment. Install the necessary dependencies via:

```bash
pip install -r requirements.txt
```
*(Dependencies include `pandas`, `numpy`, `matplotlib`, and `scikit-learn`)*

### Running the Experimental Pipeline

To reproduce the findings or experiment with the architecture, launch the updated Version 2.0 notebook:

```bash
jupyter notebook diabetes-and-it-s-type-prediction-notebook-2-0.ipynb
```

### Web Application Deployment

The architecture is designed for immediate clinical integration. The serialized model (`kmeans_model.pkl`) can be served via a web framework (e.g., React.js front-end with a Flask/FastAPI back-end). The API endpoints are structured to ingest patient data (glucose, age, pregnancies) and return the predicted diabetes subtype in real-time.

## License

This project is released under the [MIT License](LICENSE).
