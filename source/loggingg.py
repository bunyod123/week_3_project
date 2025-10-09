# src/logger.py
import logging

# LOG_DIR = "logs"
# os.makedirs(LOG_DIR, exist_ok=True)
# LOG_FILE = os.path.join(LOG_DIR, "ml_pipeline.log")

logging.basicConfig(
    filename=r"C:\Users\bunyo\OneDrive\Desktop\3_week_project\log\otherInfo.log",
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("otherInfo.log")


