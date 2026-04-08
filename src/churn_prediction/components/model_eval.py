import pickle
from pathlib import Path
from churn_prediction import logging
from box.config_box import ConfigBox
from churn_prediction.utils import save_json
from churn_prediction.utils import load_pkl_file
from churn_prediction.entity import ModelEvaluationConfig
from sklearn.metrics import classification_report, roc_auc_score


class ModelEval:

      def __init__(self, config: ModelEvaluationConfig):
            self.config = config
      

      def metrics(self, actual, pred) -> ConfigBox:
            data = classification_report(actual, pred, output_dict=True)
            return ConfigBox(data)


      def EvaluationModel(self):
            xTest = load_pkl_file(Path(self.config.xTest_data))
            yTest = load_pkl_file(Path(self.config.yTest_data))

            with open(self.config.model_path, "rb") as f:
                  model = pickle.load(f)

            yPred = model.predict(xTest)
            evaluation = self.metrics(yTest, yPred)

            Model_Performance = {
                  'Class_0': {
                        'precision': evaluation['0']['precision'],
                        'recall': evaluation['0']['recall'],
                        'f1-score': evaluation['0']['f1-score']
                  },
                  'Class_1': {
                        'precision': evaluation['1']['precision'],
                        'recall': evaluation['1']['recall'],
                        'f1-score': evaluation['1']['f1-score']
                  },
                  'accuracy': evaluation['accuracy'],
                  'roc_auc_score': roc_auc_score(yTest, yPred)
            }

            save_json(Path(self.config.metric), Model_Performance)
            logging.info(f"Model evaluation completed and report saved on {self.config.metric}")

            return Model_Performance