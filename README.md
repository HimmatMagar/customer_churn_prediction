# Customer Churn Prediction

An end-to-end machine learning pipeline for predicting customer churn using telecom customer data. This project implements a complete ML workflow with data versioning, experiment tracking, and production-ready deployment artifacts.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Stages](#pipeline-stages)
- [MLflow Integration](#mlflow-integration)
- [Research & Experiments](#research--experiments)
- [Configuration](#configuration)
- [Artifacts](#artifacts)
- [License](#license)

## Overview

This project predicts customer churn for a telecommunications company using various machine learning algorithms. The pipeline includes:

- **Data Ingestion**: Automated data collection and preparation
- **Data Transformation**: Feature engineering, encoding, and scaling with SMOTE for class imbalance
- **Model Training**: Multiple ML algorithms with hyperparameter tuning
- **Model Evaluation**: Comprehensive metrics and MLflow tracking
- **Prediction**: Ready-to-use prediction pipeline

## Features

- **End-to-End ML Pipeline**: Complete workflow from raw data to predictions
- **Data Version Control**: DVC integration for reproducible experiments
- **Experiment Tracking**: MLflow integration with DagsHub for remote tracking
- **Class Imbalance Handling**: SMOTE (Synthetic Minority Over-sampling Technique)
- **Multiple Algorithms**: Logistic Regression, SVM, KNN, Random Forest, Gradient Boosting, XGBoost
- **Hyperparameter Tuning**: GridSearchCV for optimal parameter selection
- **Prevention of Data Leakage**: Proper train/test split before transformations

## Project Structure

```
customer_churn_prediction/
├── config/
│   └── config.yaml              # Pipeline configuration
├── params.yaml                  # Model hyperparameters
├── dvc.yaml                     # DVC pipeline definition
├── dvc.lock                     # DVC lock file
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
├── README.md                    # Project documentation
├── research/
│   └── research.ipynb           # Jupyter notebook for experiments
├── src/
│   └── churn_prediction/
│       ├── components/
│       │   ├── data_ingestion.py      # Data download and extraction
│       │   ├── data_transform.py      # Data preprocessing and SMOTE
│       │   ├── model.py               # Model training component
│       │   └── model_eval.py          # Model evaluation component
│       ├── pipeline/
│       │   ├── data_ingestion_pipeline.py
│       │   ├── data_transform_pipeline.py
│       │   ├── model_pipeline.py
│       │   ├── model_eval_pipeline.py
│       │   └── prediction_pipeline.py # Production prediction
│       ├── utils/
│       │   └── mlflow_config.py       # MLflow configuration
│       └── __init__.py
└── artifact/                    # Generated artifacts (gitignored)
    ├── data_ingestion/
    ├── data_transformation/
    ├── model_building/
    └── model_evaluation/
```

## Installation

### 1. Create Conda Environment

```bash
conda create -p venv python=3.12 -y
conda activate venv
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Package in Development Mode

```bash
pip install -e .
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```
MLFLOW_TRACKING_URI=https://dagshub.com/HimmatMagar/customer_churn_prediction.mlflow
DAGSHUB_USERNAME=your_username
DAGSHUB_TOKEN=your_token
```

## Usage

### Run Full Pipeline with DVC

```bash
# Run all stages
dvc repro

# Run specific stage
dvc repro data_ingestion
dvc repro data_transformation
dvc repro model_building
dvc repro model_evaluation
```

### Run Individual Components

```bash
# Data Ingestion
python src/churn_prediction/pipeline/data_ingestion_pipeline.py

# Data Transformation
python src/churn_prediction/pipeline/data_transform_pipeline.py

# Model Training
python src/churn_prediction/pipeline/model_pipeline.py

# Model Evaluation
python src/churn_prediction/pipeline/model_eval_pipeline.py
```

### Make Predictions

```python
from churn_prediction.pipeline.prediction_pipeline import PredictionPipeline

# Initialize pipeline
predictor = PredictionPipeline()

# Prepare input data (DataFrame with same columns as training)
input_data = pd.DataFrame({
    'tenure': [12],
    'MonthlyCharges': [65.50],
    'TotalCharges': [786.00],
    'TechSupport': ['No'],
    'Contract': ['Month-to-month'],
    'Partner': ['Yes'],
    'OnlineSecurity': ['No'],
    'InternetService': ['Fiber optic']
})

# Get prediction
probability = predictor.predict_churn(input_data)
print(f"Churn Probability: {probability}")
```

## Pipeline Stages

### 1. Data Inestion

Downloads the telecom customer churn dataset from GitHub and extracts it.

- **Input**: Remote URL (ZIP file)
- **Output**: `artifact/data_ingestion/WA_Fn-UseC_-Telco-Customer-Churn.csv`

### 2. Data Transformation

Preprocesses the data with proper handling to prevent data leakage:

1. Handles missing values in `TotalCharges`
2. Encodes target variable (`Churn`) using LabelEncoder
3. Splits data into train/test sets (stratified)
4. Applies ColumnTransformer:
   - Numeric features: StandardScaler
   - Categorical features: OneHotEncoder
5. Applies SMOTE to balance classes

**Features Used:**
- Numeric: `tenure`, `MonthlyCharges`, `TotalCharges`
- Categorical: `TechSupport`, `Contract`, `Partner`, `OnlineSecurity`, `InternetService`

**Outputs:**
- `xTrain.pkl`, `xTest.pkl` - Transformed features
- `yTrain.pkl`, `yTest.pkl` - Encoded labels
- `pipeline.pkl` - Fitted preprocessor

### 3. Model Building

Trains an SVM classifier with configurable hyperparameters.

**Parameters (from `params.yaml`):**
- `C`: Regularization parameter
- `kernel`: Kernel type (rbf, linear, poly, sigmoid)
- `gamma`: Kernel coefficient

**Outputs:**
- `model.pkl` - Trained model
- `run_id.txt` - MLflow run ID for tracking

### 4. Model Evaluation

Evaluates the trained model on test data and logs metrics.

**Metrics:**
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

**Output:** `artifact/model_evaluation/mertic.json`

## MLflow Integration

All experiments are tracked on DagsHub MLflow:

**Experiment Names:**
- `Customer_Churn_Classic_ML` - Classic ML algorithms comparison
- `Customer_Churn_Ensemble_ML` - Ensemble methods (Random Forest, Gradient Boosting, XGBoost)
- `Customer_Churn_Hyperparameter_Tuning` - GridSearchCV results

**View Experiments:**
```
https://dagshub.com/HimmatMagar/customer_churn_prediction.mlflow/
```

## Research & Experiments

The `research/research.ipynb` notebook contains comprehensive experiments:

### Experiment 1: Classic ML Algorithms
- Logistic Regression
- SVM (Support Vector Machine)
- KNN (K-Nearest Neighbors)
- Naive Bayes
- Decision Tree

### Experiment 2: Ensemble Learning
- Random Forest
- Gradient Boosting
- XGBoost

### Experiment 3: Model Selection
- Comparison of best performers (SVM vs Gradient Boosting)

### Experiment 4: Hyperparameter Tuning
- GridSearchCV for SVM with parameters: C, kernel, gamma, class_weight
- GridSearchCV for Gradient Boosting with parameters: n_estimators, max_depth, learning_rate, min_samples_split, min_samples_leaf
- Confusion matrix visualization for both models

## Configuration

### config.yaml

```yaml
data_ingestion:
  source_url: "https://github.com/HimmatMagar/datae/raw/refs/heads/main/WA_Fn-UseC_-Telco-Customer-Churn.zip"
  zip_file: artifact/data_ingestion/data.zip
  
data_transformation:
  data_source: artifact/data_ingestion/WA_Fn-UseC_-Telco-Customer-Churn.csv

model_building:
  model_path: model.pkl
```

### params.yaml

```yaml
params:
  C: 10
  gamma: 'scale'
  kernel: 'rbf'
```

## Artifacts

All generated files are stored in the `artifact/` directory (ignored by git):

| Artifact | Description |
|----------|-------------|
| `data_ingestion/` | Raw downloaded data |
| `data_transformation/` | Processed train/test data and preprocessor |
| `model_building/` | Trained model and run IDs |
| `model_evaluation/` | Evaluation metrics JSON |

## Requirements

Key dependencies (see `requirements.txt` for full list):

```
pandas
numpy
scikit-learn
xgboost
imbalanced-learn
mlflow
dagshub
dvc
notebook
matplotlib
seaborn
```

## Dataset

The dataset used is the [Telco Customer Churn](https://github.com/HimmatMagar/datae/raw/refs/heads/main/WA_Fn-UseC_-Telco-Customer-Churn.zip) dataset containing:

- **7,043** customer records
- **21** features (demographics, services, billing)
- **Target**: Churn (Yes/No)
- **Class Distribution**: ~73% No Churn, ~27% Churn (imbalanced)

## Author

- **Himmat Magar**
- GitHub: [@HimmatMagar](https://github.com/HimmatMagar)
- Email: himmatmagar007@gmail.com

## License

This project is open source.
