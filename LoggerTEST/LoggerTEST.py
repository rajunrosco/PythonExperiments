import logging
import pathlib
import sys

_MODULEPATH = pathlib.Path(__file__).parent
_LOGFILEPATH = (_MODULEPATH / "debug.log").resolve()

logging.basicConfig(
    level=logging.INFO,
    style="{",
    format="{asctime} [{levelname}] {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(_LOGFILEPATH),
        logging.StreamHandler()
    ]
)

log = logging.getLogger(__name__)


def main(argv):
    name="Benson"
    log.setLevel(logging.INFO)
    log.debug("This is debug stuff")
    log.info(f"This is normal info log {name}")
    log.warning("This is a warning!")

if __name__ == "__main__":
    main(sys.argv)

