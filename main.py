from churn_prediction import logger
from churn_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from churn_prediction.pipeline.data_transform_pipeline import DataTransformPipeline

STAGE_NAME = "Data Ingestion stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Data Transformation stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataTransformPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e