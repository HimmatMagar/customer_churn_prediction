from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      source_url: str
      zip_file: Path
      unzip_file: Path
      

@dataclass(frozen=True)
class DataTransformationConfig:
      root_dir: Path
      data_source: Path


@dataclass(frozen=True)
class ModelBuildingConfig:
      root_dir: Path
      xTrain_data: Path
      yTrain_data: Path
      model_path: str
      C: int
      gamma: str
      kernel: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
      root_dir: Path
      xTest_data: Path
      yTest_data: Path
      model_path: Path
      metric: Path
