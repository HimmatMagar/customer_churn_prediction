import os
import pickle
import pandas as pd
from pathlib import Path
from churn_prediction import logger
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from churn_prediction.entity import DataTransformationConfig
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder, StandardScaler


class DataTransformation:

      def __init__(self, config: DataTransformationConfig):
            self.config = config
      

      def load_data(self):
            try:
                  df = pd.read_csv(Path(self.config.data_source))
                  return df
            except FileExistsError as e:
                  raise e
      
      def split_data(self):
            df = self.load_data()
            df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

            numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
            categorical_features = ['TechSupport', 'Contract', 'Partner', 'OnlineSecurity', 'InternetService']
            X = df[numeric_features + categorical_features]

            print(X.head())

            y_raw = df['Churn']
            target_encoder = LabelEncoder()
            y = target_encoder.fit_transform(y_raw)

            X_train, X_test, y_train, y_test = train_test_split(
                  X, y, test_size=0.3, random_state=42
            )

            transformer = ColumnTransformer(
                  transformers = [
                        ('numeric', Pipeline([
                              ('impute', SimpleImputer(strategy='mean')),
                              ('scaler', StandardScaler())
                        ]), [0, 1, 2]),
                        ('encoder', OrdinalEncoder(), [5]),
                        ('OHE', OneHotEncoder(drop='first', handle_unknown='ignore'), [3, 4, 6, 7])
                  ],
                  remainder='passthrough'
            )

            full_pipeline = Pipeline([
                  ("preprocessing", transformer)
            ])

            pickle.dump(full_pipeline, open(os.path.join(self.config.root_dir, "pipeline.pkl"), 'wb'))

            xTrain = full_pipeline.fit_transform(X_train)
            xTest = full_pipeline.transform(X_test)

            sm = SMOTE(random_state=42)

            xTrainRes, yTrainRes  = sm.fit_resample(xTrain, y_train)

            logger.info(f"Data split: Train={len(xTrainRes)}, Test={len(xTest)}")

            pickle.dump(xTrainRes, open(os.path.join(self.config.root_dir, "xTrain.pkl"), "wb"))
            pickle.dump(xTest, open(os.path.join(self.config.root_dir, "xTest.pkl"), "wb"))
            pickle.dump(yTrainRes, open(os.path.join(self.config.root_dir, "yTrain.pkl"), "wb"))
            pickle.dump(y_test, open(os.path.join(self.config.root_dir, "yTest.pkl"), "wb"))

            logger.info("train and pipeline saved successfully")
