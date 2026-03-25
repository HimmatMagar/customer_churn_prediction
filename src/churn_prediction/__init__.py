import os
import sys
import logging

log_dir = "Logging"
log_file = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
      level = logging.INFO,
      format = "[%(asctime)s: %(level)s: %(module)s: %(message)s]",
      handlers=[
            logging.FileHandler(log_dir),
            logging.StreamHandler(sys.stdout(log_file))
      ]
)

logger = logging.getLogger("churn-prediction")
