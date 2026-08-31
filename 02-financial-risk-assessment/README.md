# Financial Risk Assessment and Risk Rating Prediction

## Overview

This project explores the use of machine learning to predict the financial risk rating of borrowers based on financial, demographic, employment, and loan-related information.

The objective was to build a classification pipeline that could categorize borrowers into three risk levels:

- Low
- Medium
- High

I chose this project independently because I was interested in finance and wanted to explore how data analysis and machine learning could be applied to a financial problem.

The project also helped me understand an important practical issue in machine learning: a model can have reasonable overall accuracy while still performing poorly on less represented classes.

---

## Project Details

- **Type:** Individual project
- **Field:** Financial Risk Analysis / Machine Learning
- **Dataset size:** 15,000 records
- **Number of variables:** 20
- **Target variable:** Risk Rating
- **Risk categories:** Low, Medium, High
- **Development environment:** Jupyter Notebook

---

## Dataset

The dataset contains financial and demographic information about borrowers.

The variables include:

- Age
- Gender
- Education Level
- Marital Status
- Income
- Credit Score
- Loan Amount
- Loan Purpose
- Employment Status
- Years at Current Job
- Payment History
- Debt-to-Income Ratio
- Assets Value
- Number of Dependents
- City
- State
- Country
- Previous Defaults
- Marital Status Change
- Risk Rating

The dataset contained missing values in several numerical variables, including income, credit score, loan amount, assets value, number of dependents, and previous defaults.

---

## Objective

The primary objective was to investigate whether borrower characteristics could be used to predict their financial risk rating.

The project involved:

1. Exploring the dataset and understanding its structure.
2. Identifying and handling missing values.
3. Examining distributions and relationships between variables.
4. Preparing categorical and numerical variables for machine learning.
5. Building classification models.
6. Investigating the effect of class imbalance.
7. Experimenting with techniques such as SMOTE.
8. Comparing different machine learning approaches.
9. Evaluating models using multiple classification metrics.

---

## Exploratory Data Analysis

The first stage involved understanding the structure and quality of the dataset.

The dataset was examined for:

- Number of observations and variables
- Data types
- Missing values
- Numerical distributions
- Risk-rating distribution
- Relationships between financial variables and risk rating
- Potential outliers

The dataset contained 15,000 observations across 20 variables.

Visualizations were created using Matplotlib and Seaborn to explore the data and identify patterns.

---

## Data Preprocessing

### Missing Values

Missing values were identified in several numerical columns.

The missing numerical values were handled using mean imputation.

The affected variables included:

- Income
- Credit Score
- Loan Amount
- Assets Value
- Number of Dependents
- Previous Defaults

### Outlier Analysis

Outlier analysis was performed using the Interquartile Range (IQR) method.

Income was specifically examined for potential outliers as part of the exploratory analysis.

### Categorical Variables

Categorical variables were converted into numerical representations using one-hot encoding.

These included variables such as:

- Gender
- Education Level
- Marital Status
- Loan Purpose
- Employment Status
- Payment History
- City
- State
- Country

### Target Encoding

The target variable, Risk Rating, was converted into numerical classes:

- Low = 0
- Medium = 1
- High = 2

### Feature Scaling

Numerical features were standardized using `StandardScaler`.

### Train-Test Split

The data was divided into training and testing sets using an 80:20 split.

Stratified sampling was used so that the distribution of the risk-rating classes was maintained between the training and testing sets.

---

## Machine Learning Models

### Random Forest

A Random Forest classifier was used as the initial machine learning model.

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification report

The initial model achieved approximately 60% accuracy.

However, the results showed that the model performed substantially better on the Low-risk class than on the Medium- and High-risk classes.

This highlighted the importance of examining class-specific metrics instead of relying only on overall accuracy.

---

## Handling Class Imbalance

The risk-rating classes were not equally represented in the test data.

The test set contained approximately:

- 1,800 Low-risk observations
- 900 Medium-risk observations
- 300 High-risk observations

Because of this imbalance, the model was more effective at identifying the Low-risk class.

To investigate whether balancing the classes could improve the model, SMOTE (Synthetic Minority Over-sampling Technique) was used.

A Random Forest model was then trained using the SMOTE-balanced data.

The SMOTE-based Random Forest achieved approximately 54% accuracy.

Although the overall accuracy decreased compared with the initial model, the experiment provided a useful understanding of the trade-offs involved when attempting to improve minority-class performance.

---

## XGBoost

XGBoost was also explored as an alternative classification approach.

The model was evaluated against the same financial risk classification problem.

The XGBoost experiment achieved approximately 51.6% accuracy.

The project therefore demonstrated that simply switching to a different machine learning algorithm did not automatically solve the underlying class imbalance and classification challenges.

---

## Hyperparameter Tuning

Hyperparameter tuning was explored using `GridSearchCV`.

The experimentation considered parameters such as:

- Number of estimators
- Maximum tree depth
- Learning rate
- Gamma
- Minimum child weight

The purpose was to investigate whether changing model parameters could improve classification performance.

---

## Model Evaluation

Multiple evaluation metrics were considered rather than relying only on accuracy.

These included:

- Accuracy
- Precision
- Recall
- F1-score
- Classification reports
- ROC-AUC experimentation

One of the main observations from the project was that accuracy alone could give an incomplete picture of model performance.

For a financial risk classification problem, correctly identifying Medium- and High-risk borrowers is important, so class-specific precision, recall, and F1-scores also need to be considered.

---

## Key Results

| Model / Approach | Approx. Accuracy |
|---|---:|
| Initial Random Forest | 60% |
| SMOTE + Random Forest | 54% |
| XGBoost | 51.6% |

The results showed that the initial Random Forest produced the highest overall accuracy among the experiments documented in the notebook.

However, the most important learning from the experiments was not simply which model had the highest accuracy.

The project showed how class imbalance can cause a model to favor the majority class and why model performance needs to be evaluated at the individual class level.

---

## Challenges

The main challenge encountered during the project was the imbalance between the three risk-rating classes.

The initial Random Forest model was considerably better at predicting Low-risk borrowers than Medium- and High-risk borrowers.

Several approaches were therefore explored, including:

- SMOTE
- Changes to Random Forest parameters
- XGBoost
- Hyperparameter tuning
- Multiple evaluation metrics

The experiments also involved troubleshooting issues encountered during model evaluation and experimentation.

---

## Key Learnings

This project helped me develop practical experience in several areas of data science and machine learning.

### Data Analysis

- Working with a relatively large dataset containing 15,000 records.
- Understanding dataset structure and variable types.
- Identifying missing values.
- Exploring relationships between variables through visualization.

### Data Preprocessing

- Handling missing numerical data.
- Identifying potential outliers using the IQR method.
- Converting categorical variables into numerical features.
- Standardizing numerical variables.
- Creating stratified training and testing datasets.

### Machine Learning

- Building classification models using Random Forest.
- Experimenting with XGBoost.
- Understanding the effect of class imbalance.
- Using SMOTE to address minority classes.
- Exploring hyperparameter tuning with GridSearchCV.

### Model Evaluation

One of the most important lessons from the project was that overall accuracy does not always provide a complete picture of model performance.

In an imbalanced classification problem, a model can achieve reasonable accuracy while still performing poorly on minority classes.

This made me pay more attention to precision, recall, F1-score, and class-specific performance when evaluating classification models.

---

## Technologies and Libraries

The project was developed using Python and Jupyter Notebook.

Main libraries used include:

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- imbalanced-learn
- SHAP

---

## Project Structure

```text
02-financial-risk-assessment/
│
├── README.md
├── requirements.txt
│
├── notebook/
│   └── financial_risk_assessment.ipynb
│
├── data/
│   └── financial_risk_assessment.csv
│
└── screenshots/
    ├── 01-dataset-overview.png
    ├── 02-risk-rating-distribution.png
    ├── 03-credit-score-analysis.png
    ├── 04-random-forest-results.png
    ├── 05-smote-results.png
    └── 06-xgboost-results.png
