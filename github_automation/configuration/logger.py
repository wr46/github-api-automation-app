from __future__ import annotations
import logging

from github_automation.configuration.config import APP_NAME, LOG_LEVEL


class LogFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Log(object):
    logger: logging.Logger

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Log, cls).__new__(cls)
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            handler.setFormatter(LogFormatter())
            cls.logger = logging.getLogger(APP_NAME)
            cls.logger.setLevel(LOG_LEVEL)
            cls.logger.addHandler(handler)
        return cls.instance

    def get_logger(self) -> logging.Logger:
        return self.logger


instance = Log()
