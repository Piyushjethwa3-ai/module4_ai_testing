import logging

logging.basicConfig(
    filename="reports/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message):
    logging.info(message)