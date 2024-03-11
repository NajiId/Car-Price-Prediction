# Car Price Prediction

This repository contains code for predicting car prices using various machine learning algorithms. The prediction is based on features such as manufacturer, model, production year, mileage, engine volume, etc.

## Introduction

The goal of this project is to develop a machine learning model that accurately predicts car prices based on their attributes. The dataset used for training and testing the model contains information about thousands of cars, including their prices, specifications, and other relevant details.

## Getting Started

To run the code and reproduce the results, follow these steps:

1. Clone the repository to your local machine:
2. Install the required dependencies listed in the `requirements.txt` file:

3. Download the dataset `car_price_prediction.csv` and place it in the root directory of the project.

4. Run the provided Python script or Jupyter Notebook to explore the data, preprocess it, train machine learning models, and evaluate their performance.

## Analysis

The analysis section includes exploratory data analysis (EDA) to understand the distribution of various features, correlation analysis, visualization of top manufacturers and their average prices, detection of outliers, and more.

## Data Processing

In this step, the raw data is processed by handling missing values, transforming categorical variables into numerical ones using label encoding, removing outliers, and preparing the dataset for model training.

## Modeling

Several machine learning algorithms including Linear Regression, Decision Tree Regressor, Random Forest Regressor, Gradient Boosting Regressor, XGBRF Regressor, and Support Vector Regressor are trained and evaluated using the processed data. The performance metrics such as R-squared score and RMSE (Root Mean Squared Error) are calculated for each model.

## Results

The results of each model are summarized in a DataFrame and visualized using line plots to compare the R-squared scores and RMSE values. The Random Forest Regressor achieved the highest R-squared score and lowest RMSE among the tested models.

## Using Model for Prediction

The best performing model (Random Forest Regressor) is saved as a pickle file (`Cars_Predictions.sav`) for future use. This model can be used to predict car prices for new data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.


