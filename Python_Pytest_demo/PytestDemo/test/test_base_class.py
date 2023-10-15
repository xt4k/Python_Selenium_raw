import inspect
import logging


class BaseClass:
    def get_logger(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        file_handler = logging.FileHandler("log_file.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
