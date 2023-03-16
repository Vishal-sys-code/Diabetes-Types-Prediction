# Diabetes and it's type prediction

This is a machine learning model that uses K-means clustering to classify diabetes based on glucose levels, age, and number of pregnancies. The model can be used to predict the type of diabetes a person has, which can be useful for doctors in determining the appropriate treatment plan.

## Data

The data used in this model is from the NC State University diabetes dataset, which contains information on glucose levels, age, pregnancies, and other factors related to diabetes.

## Methodology

* To classify whether diabetes is present or not, the entire NCSU Diabetes Dataset was used. The dataset contains information about 769 patients, including their demographic information, medical history, medications, and laboratory test results. The dataset was preprocessed to handle missing values and irrelevant features were removed. The classification problem was approached as a binary classification problem, where the goal was to predict whether a patient has diabetes or not based on the available features.

* After the classification task, K-means clustering algorithm was used to group the patients into three clusters based on their age, pregnancies, and glucose levels. These three features were selected as they were found to have a strong correlation with diabetes. The number of clusters was set to three, which was determined by using the elbow method and silhouette score.

Overall, the methodology involved preprocessing the dataset, performing binary classification to determine if diabetes is present or not, and using K-means clustering to group patients into three clusters based on their age, pregnancies, and glucose levels. The goal of this approach was to gain insights into the relationships between the features and diabetes, which could be useful for developing targeted interventions and treatment plans.

## Evaluation of the Model

We can evaluate the performance of our clustering model using the Silhouette score and Calinski-Harabasz index.

The Silhouette score measures the quality of the clustering results by computing the average distance between each data point and all other data points in the same cluster, as well as the average distance between each data point and all data points in the nearest neighboring cluster. The score ranges from -1 to 1, with a higher score indicating better clustering results.

The Calinski-Harabasz index is another metric for evaluating the quality of clustering results. It measures the ratio of the between-cluster variance to the within-cluster variance. A higher Calinski-Harabasz index indicates better separation between clusters.

To compute these metrics, we can use the ```silhouette_score``` and ```calinski_harabasz_score``` functions from the ```sklearn.metrics``` module, respectively. We would need to provide the original dataset and the cluster assignments as inputs to both functions.

## Requirements

This model requires the following packages to be installed:
* pandas
* numpy
* matplotlib
* scikit-learn

## Usage

To use this model, run the ```diabetes-prediction-and-it-s-types.ipynb``` notebook. This will load the dataset, perform K-means clustering, and predict the type of diabetes for each data point.

You can modify the number of clusters used by changing the ```n_clusters``` parameter in the ```KMeans``` function.

## Web Application

This model can be integrated into a web application using React.js or other web frameworks. The application can take input from the user, such as glucose levels, age, and number of pregnancies, and use the model to predict the type of diabetes.

To use this model in a web application, you will need to export the model as a JSON file using the ```pickle``` library. This file can then be loaded into your web application and used to make predictions.

