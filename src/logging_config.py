import logging

from rich.logging import RichHandler

from config import LOG_LEVEL


def configure_logging() -> None:
    """
    Configures application-wide logging.
    """

    logging.basicConfig(
        level=LOG_LEVEL,
        format=("%(message)s"),
        datefmt="[%X]",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                show_path=False,
            )
        ],
    )