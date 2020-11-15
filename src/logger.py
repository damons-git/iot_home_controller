import logging
import datetime


class Logger:
    # Log class to produce system log
    __log_name      = "home_controller"
    __output_name   = None
    __output_dir    = None
    __log_level     = logging.DEBUG

    @classmethod
    def output_dir(cls, output_dir: str):
        cls.__output_dir = output_dir


    @classmethod
    def output_name(cls, output_name: str):
        cls.__output_name = output_name


    @staticmethod
    def setup():
        # Output filepath
        current_time = datetime.datetime.now()
        file_prefix = str(current_time.strftime("%Y%m%d_%H-%M-%S"))
        filepath = "{0}{1}_{2}".format(Logger.__output_dir, file_prefix, Logger.__output_name)

        # Root logger
        root = logging.getLogger()
        root.setLevel(Logger.__log_level)

        # Custom logger
        logger = logging.getLogger(Logger.__log_name)

        # Create handlers
        cli_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(filepath)
        cli_handler.setLevel(Logger.__log_level)
        file_handler.setLevel(Logger.__log_level)

        # Custom formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        cli_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to loggers
        logger.addHandler(cli_handler)
        logger.addHandler(file_handler)

        logger.info("Custom logger configured, writing to: \"{0}\"".format(filepath))


    def __new__(cls):
        return logging.getLogger(Logger.__log_name)


