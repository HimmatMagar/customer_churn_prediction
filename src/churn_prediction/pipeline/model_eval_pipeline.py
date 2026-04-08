import mlflow
from churn_prediction import logger
from churn_prediction.config import ConfigManager
from churn_prediction.components.model_eval import ModelEval
from churn_prediction.utils.mlflow_config import configure_mlflow, load_run_id


STAGE_NAME = "Model Evaluation stage"

class ModelEvalPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigManager()
            eval_config = config.getModelEvalConfig()

            configure_mlflow(experiment_name="churn-prediction-model")

            run_id = load_run_id()
            try:
                  with open("artifact/model_id.txt", 'r') as f:
                        model_id = f.read()
            except FileNotFoundError as e:
                  raise e

            with mlflow.start_run(run_id=run_id):
                  model_eval = ModelEval(eval_config)
                  metrics = model_eval.EvaluationModel()

                  mlflow.log_metrics({
                        "accuracy": metrics["accuracy"],
                        "roc_auc_score": metrics['roc_auc_score'],
                        "class0_precision": metrics["Class_0"]["precision"],
                        "class0_recall":    metrics["Class_0"]["recall"],
                        "class0_f1":        metrics["Class_0"]["f1-score"],
                        "class1_precision": metrics["Class_1"]["precision"],
                        "class1_recall":    metrics["Class_1"]["recall"],
                        "class1_f1":        metrics["Class_1"]["f1-score"]
                  })

                  if metrics["Class_0"]["f1-score"] > 0.60:
                        model = mlflow.register_model(
                              model_uri = f"models:/{model_id}",
                              name = "Churn-Prediction-Model"
                        )
                        logger.info("Model register successfull in model registry")

                        client = mlflow.tracking.MlflowClient()
                        client.transition_model_version_stage(
                              name="Churn-Prediction-Model",
                              version=model.version,
                              stage="staging"
                        )

                        logger.info("Model stage improved into stagging stage")
                  else:
                        logger.warning("Failed to register due to Low F1 score")
            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelEvalPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e