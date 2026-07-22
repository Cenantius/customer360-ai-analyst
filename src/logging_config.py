import logging

from config import LOG_LEVEL

def configure_logging() -> None:
    """
    Configures application-wide logging.
    """

    logging.basicConfig(
        level=LOG_LEVEL,
        format=(
            # time
            "%(asctime)s | "
            # log level
            "%(levelname)s | "
            # from which module did the msg come from
            "%(name)s | "
            # log message
            "%(message)s | "
        ),
        datefmt="%Y-%m-%d %H:%M:%S"
    )