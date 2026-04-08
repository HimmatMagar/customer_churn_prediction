import mlflow
from churn_prediction import logger
from churn_prediction.config import ConfigManager
from churn_prediction.components.model import ModelBuilding
from churn_prediction.utils.mlflow_config import configure_mlflow, save_run_id


STAGE_NAME = "Model Building stage"

class ModelBuildingPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigManager()
            model_config = config.getModelBuildingConfig()

            configure_mlflow(experiment_name="churn-prediction-model")
            with mlflow.start_run(run_name="svc") as run:
                  try:
                        mlflow.log_params({
                              "c": model_config.C,
                              "gamma": model_config.gamma,
                              "kernel": model_config.kernel
                        })

                        model = ModelBuilding(model_config)
                        svc_model = model.model()

                        logging_model = mlflow.sklearn.log_model(
                              sk_model=svc_model,
                              artifact_path="model"
                        )
                        logger.info("Model saved successfully in mlflow")

                        with open("artifact/model_id.txt", "w") as f:
                              f.write(logging_model.run_id)
                        logger.info("Model id saved successfully in artifact/model_id.txt")

                        pipeline_path = "artifact/data_transformation/pipeline.pkl"
                        mlflow.log_artifact(
                              local_path = pipeline_path,
                              artifact_path="artifact"
                        )

                        save_run_id(run.info.run_id)
                  
                  except Exception as e:
                        raise e
            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelBuildingPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e