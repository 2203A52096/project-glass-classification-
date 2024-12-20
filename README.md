# Glass Classification using Machine Learning

This project focuses on building a machine learning model to classify glass types based on their physical and chemical composition. 
The classification can be useful in various industries, such as manufacturing, recycling, forensic analysis and so on...

---

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Technologies Used](#technologies-used)
4. [Project Workflow](#project-workflow)
5. [How to Run the Project](#how-to-run-the-project)
6. [Attribution](#attribution)
7. [Acknowledgments](#acknowledgments)

---

## Introduction

Glass classification is a multi-class classification problem,
The goal is to predict the type of glass based on its featues. 
This project uses a supervised learning approach with models like Logistic regression, KNN and SVM to achieve accurate predictions.

---

## Dataset

The dataset is used from https://www.kaggle.com/datasets/uciml/glass
The dataset includes the following features:
- Refractive Index
- Sodium (Na)
- Magnesium (Mg)
- Aluminum (Al)
- Silicon (Si)
- Potassium (K)
- Calcium (Ca)
- Barium (Ba)
- Iron (Fe)

The target variable represents the glass type (e.g., building windows, containers, tableware, etc.).

### Key Statistics
- Total Samples: 214
- Features: 10
- Classes: 7

---

## Technologies Used
- **Python**: Core language for development.
- **Libraries**:
  - Pandas and NumPy: Data manipulation and analysis.
  - Scikit-learn: Model building and evaluation.
  - Matplotlib and Seaborn: Visualization.
- **Streamlit**: For deploying the project as a web application.

---

## Project Workflow

1. **Data Preprocessing**:
   - Handling missing values (if any).
   - Normalizing or scaling the features.
   - Splitting data into training and testing sets.

2. **Exploratory Data Analysis (EDA)**:
   - Visualizing feature distributions .
   - Identifying patterns and relationships in the data.

3. **Model Selection**:
   - Training and evaluating multiple classifiers (logistic regression, SVM, KNN).
   - Selecting the best-performing model based on accuracy, F1 score, and other metrics.
   - Bootstrap Method is used on all models to see Mean Accuracy, Standard Deviation of Accuracy, Confidence Interval
     and estimate the quality of a machine learning model at predicting data that is not included in the training data.

4. **Model Deployment**:
   - Creating an interactive web app using Streamlit.
   - Allowing users to input values and get predictions.

