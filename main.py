from churn_prediction import logger
from churn_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e