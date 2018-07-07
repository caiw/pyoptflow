from pathlib import Path
import logging
#
from .hornschunck import HornSchunck
from .lucaskanade import LucasKanade, getPOI, gaussianWeight

logger = logging.getLogger(__name__)


def getimgfiles(stem:Path, pat:str) -> list:

    stem = Path(stem).expanduser()

    logger.info(f"searching {stem / pat}")
    flist = sorted(stem.glob(pat))

    if not flist:
        raise FileNotFoundError(f'no files found under {stem} using {pat}')

    return flist
