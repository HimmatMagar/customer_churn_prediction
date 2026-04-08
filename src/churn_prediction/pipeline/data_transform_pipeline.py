from churn_prediction import logger
from churn_prediction.config import ConfigManager
from churn_prediction.components.data_transform import DataTransformation


STAGE_NAME = "Data Transformation stage"

class DataTransformPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigManager()
            data_transform_config = config.getDataTransformationConfig()
            data_transform = DataTransformation(data_transform_config)
            data_transform.split_data()
            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataTransformPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e