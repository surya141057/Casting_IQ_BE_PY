import logging
import os

def setup_logger(name: str, log_file: str = "castingiq.log", level=logging.INFO):
    # Absolute path for the log file (near manage.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    manage_dir = os.path.dirname(base_dir)
    log_path = os.path.join(manage_dir, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Check if handlers are already set (to avoid duplicate logs)
    if not logger.handlers:
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
