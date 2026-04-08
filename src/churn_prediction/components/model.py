import os
import pickle
from pathlib import Path
from sklearn.svm import SVC
from churn_prediction import logging
from churn_prediction.utils import load_pkl_file
from churn_prediction.entity import ModelBuildingConfig


class ModelBuilding:

      def __init__(self, config: ModelBuildingConfig):
            self.config = config
      
      def model(self):
            xTrain = load_pkl_file(Path(self.config.xTrain_data))
            yTrain = load_pkl_file(Path(self.config.yTrain_data))

            svc_model = SVC(
                  C=self.config.C,
                  gamma=self.config.gamma,
                  kernel=self.config.kernel,
                  class_weight="balanced"
            )

            svc_model.fit(xTrain, yTrain)
            model_path = os.path.join(self.config.root_dir, self.config.model_path)
            with open(model_path, "wb") as f:
                  pickle.dump(svc_model, f)
            
            logging.info(f"Model saved successfully at {model_path}")
            return svc_model
