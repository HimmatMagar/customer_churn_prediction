import os
import json
import yaml
import pickle
from typing import Any
from pathlib import Path
from churn_prediction import logger
from ensure import ensure_annotations
from box.config_box import ConfigBox
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml_file(filePath: Path) -> ConfigBox:
      try:
            with open(filePath, "r") as f:
                  content = yaml.safe_load(f)
                  return ConfigBox(content)
            logger.info(f"Yaml file read successfully from {filePath}")
      except BoxValueError:
            raise ValueError("Yaml file is empty")
      except Exception:
            raise


@ensure_annotations
def create_dir(file_dir: list, verbose = True) -> None:
      for filename in file_dir:
            os.makedirs(filename, exist_ok=True)

      if verbose:
            logger.info("File directory created successfully")



@ensure_annotations
def save_json(filePath: Path, data:dict) -> None:
      try:
            with open(filePath, "w") as f:
                  json.dump(data, f)
      except FileNotFoundError as e:
            raise e
      except Exception:
            raise


@ensure_annotations
def save_pkl_file(filePath: Path, data:Any) -> None:
      try:
            with open(filePath, "wb") as f:
                  pickle.dump(data, f)
            logger.info(f"{filePath} saved successfully")
      except Exception as e:
            raise e


@ensure_annotations
def load_pkl_file(filePath: Path) -> Any:
      try:
            with open(filePath, "rb") as f:
                  data = pickle.load(f)
            logger.info(f"data loaded from {filePath} successfully")
            return data
      except Exception as e:
            raise e