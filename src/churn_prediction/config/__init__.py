from churn_prediction.utils import *
from churn_prediction.entity import *
from churn_prediction.constants import __config__, __params__


class ConfigManager:
      
      def __init__(self, config = __config__, params = __params__):
            self.config = read_yaml_file(config)
            self.params = read_yaml_file(params)
            create_dir([self.config.dir])


      def getDataIngestionConfig(self) -> DataIngestionConfig:
            config = self.config.data_ingestion
            create_dir([config.root_dir])

            data_ingestion = DataIngestionConfig(
                  root_dir = config.root_dir,
                  source_url = config.source_url,
                  zip_file = config.zip_file,
                  unzip_file = config.unzip_file
            )
            return data_ingestion


      def getDataTransformationConfig(self) -> DataTransformationConfig:
            config = self.config.data_transformation
            create_dir([config.root_dir])

            data_transform = DataTransformationConfig(
                  root_dir = config.root_dir,
                  data_source = config.data_source
            )

            return data_transform