import logging


def test_logging():
    logger = logging.getLogger(__name__)

    # file handler object
    file_handler = logging.FileHandler("log_file.log")

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.setLevel(logging.CRITICAL)

    logger.debug("Debug - internal message")
    logger.info("Information layer message taken")
    logger.warning("Warning message detected")
    logger.error("Real ERROR happen")
    logger.critical("HIGH IMPORTANCE ERROR HAPPEN!")
