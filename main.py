from churn_prediction import logger
from churn_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from churn_prediction.pipeline.data_transform_pipeline import DataTransformPipeline
from churn_prediction.pipeline.model_pipeline import ModelBuildingPipeline
from churn_prediction.pipeline.model_eval_pipeline import ModelEvalPipeline

# STAGE_NAME = "Data Ingestion stage"
# try:
#       logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#       obj = DataIngestionPipeline()
#       obj.main()
#       logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e


# STAGE_NAME = "Data Transformation stage"
# try:
#       logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#       obj = DataTransformPipeline()
#       obj.main()
#       logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e

# STAGE_NAME = "Model Building stage"
# try:
#       logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
#       obj = ModelBuildingPipeline()
#       obj.main()
#       logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#       logger.exception(e)
#       raise e


STAGE_NAME = "Model Evaluation stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = ModelEvalPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e