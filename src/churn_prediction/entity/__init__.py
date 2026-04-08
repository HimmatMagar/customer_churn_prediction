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