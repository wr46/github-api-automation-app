from __future__ import annotations
import logging

from github_automation.configuration.config import APP_NAME, LOG_LEVEL


class LogFormatter(logging.Formatter):
    _grey = "\x1b[38;20m"
    _yellow = "\x1b[33;20m"
    _red = "\x1b[31;20m"
    _bold_red = "\x1b[31;1m"
    _reset = "\x1b[0m"
    _fmt = "%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: _grey + _fmt + _reset,
        logging.INFO: _grey + _fmt + _reset,
        logging.WARNING: _yellow + _fmt + _reset,
        logging.ERROR: _red + _fmt + _reset,
        logging.CRITICAL: _bold_red + _fmt + _reset,
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
