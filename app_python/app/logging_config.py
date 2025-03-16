import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Save logs to 'app.log'
            logging.StreamHandler()  # Also output logs to console
        ]
    )
    return logging.getLogger(__name__)
