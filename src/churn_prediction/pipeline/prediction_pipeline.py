import mlflow
import pickle
from pathlib import Path
from churn_prediction import logging
from churn_prediction.utils.mlflow_config import load_run_id


class PredictionPipeline:

      def __init__(self):
            try:
                  # self.model = mlflow.pyfunc.load_model(
                  #       "models:/Churn-Prediction-Model/Production"
                  # )

                  model_path = "artifact/model_building/model.pkl"
                  with open(model_path, "rb") as f:
                        self.model = pickle.load(f)

                  artifact_path = mlflow.artifacts.download_artifacts(
                        run_id=load_run_id(),
                        artifact_path="artifact/pipeline.pkl"
                  )

                  with open(artifact_path, "rb") as f:
                        self.pipeline = pickle.load(f)
                  logging.info("Pipeline loaded successfully")

            except Exception as e:
                  raise e
      

      def predict_churn(self, data):

            try:
                  x = self.pipeline.transform(data)
                  prediction = self.model.predict_proba(x)

                  return prediction

            except Exception:
                  raise Exception