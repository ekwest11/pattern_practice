"""
Main.
"""
import logging
import time
from logging.handlers import RotatingFileHandler
from pathlib import Path


class SingletonLogger:
    """
    Singleton logger class.
    """

    # Stores the singleton instance.
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Instance allocator.

        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """

        # If there is no instance, allocate a new one.
        if not cls._instance:
            cls._instance = super().__new__(cls)

        # Return the instance.
        return cls._instance

    def __init__(self, pathToLogFile: str = ""):
        """
        Constructor.
        """
        if not hasattr(self, "logger"):
            self.logger = None
            self.InitializeLogger(pathToLogFile)

    def InitializeLogger(self, pathToLogFile: str):
        """
        Initializes the logger.

        :param pathToLogFile: Path to log file.
        """

        # Convert to path.
        path = Path(pathToLogFile)

        # Create formatter to log 24 characters of date/time + timezone abbreviation, along with the message.
        formatter = logging.Formatter(
            "%(asctime)-24s | %(message)s",  # Fixed-width local date/time with timezone and log message
            datefmt="%Y-%m-%d %H:%M:%S %Z"  # Format includes timezone abbreviation with %Z
        )

        # Set the formatter to local time.
        formatter.converter = time.localtime

        # Create rotating file handler that logs up to 10x, 1MB files.
        handler = RotatingFileHandler(path, mode="a", maxBytes=1024*1024, backupCount=10)
        handler.setFormatter(formatter)

        # Create the logger and set logging level.
        self.logger = logging.getLogger("SingletonLogger")
        self.logger.setLevel(logging.INFO)

        # Add rotating file handler.
        self.logger.addHandler(handler)
        self.logger.propagate = False

    def LogMessage(self, message: str) -> None:
        """
        Logs a message.
        :param message: Message to log.
        """
        self.logger.info(message)


if __name__ == "__main__":
    originalLogger = SingletonLogger(pathToLogFile="relativePath.log")
    originalLogger.LogMessage("First test message")

    newLogger = SingletonLogger()

    if newLogger is originalLogger:
        originalLogger.LogMessage("Success!")
