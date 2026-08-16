# Medical Insurance Cost Prediction

This project is a Machine Learning based web application that predicts the estimated medical insurance cost for a person based on a few basic details.

I built this project while learning the complete workflow of a Machine Learning project, starting from data preprocessing and model training to saving the trained model and deploying it as a web application using Streamlit.

## Live Demo

You can try the application here:

https://medical-insurance-cost-prediction-oev5vyeybpczpmzrl2ansy.streamlit.app/

---

## About the Project

Medical insurance cost depends on different factors such as a person's age, BMI, smoking habits, number of children and region.

In this project, I used these features to train a **Linear Regression** model that predicts the estimated insurance charges.

The trained model is then connected to a Streamlit application. A user can enter their details through the web interface and get an estimated insurance cost.

This project helped me understand how a Machine Learning model can be used in a simple real-world application instead of only working inside a Jupyter Notebook.

---

## Features Used

The model uses the following information:

- **Age** – Age of the person
- **Gender** – Male or Female
- **BMI** – Body Mass Index
- **Number of Children** – Number of dependents
- **Smoker** – Whether the person smokes or not
- **Region** – Residential region

These values are provided through the Streamlit interface and passed to the trained model for prediction.

---

## Machine Learning Approach

### 1. Data Loading

The insurance dataset is stored in `insurance.csv`.

The dataset is loaded and explored using Pandas to understand the available columns, data types and values.

### 2. Data Preprocessing

Before training the model, the data is prepared for Machine Learning.

The preprocessing includes handling the categorical features and converting them into a suitable numerical form so that they can be used by the regression model.

The input features are then separated from the target variable.

### 3. Train-Test Split

The dataset is divided into training and testing data.

The training data is used to train the model, while the testing data is used to check how the model performs on unseen data.

### 4. Model Training

For this project, I used:

**Linear Regression**

Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value.

In this case, the target variable is the medical insurance cost.

### 5. Saving the Model

After training, the model is saved using **Joblib**.

The saved model is stored as:

```text
model.pkl
