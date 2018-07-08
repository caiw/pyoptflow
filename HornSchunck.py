#!/usr/bin/env python
"""
./HornSchunck.py data/box/box
./HornSchunck.py data/office/office
./HornSchunck.py data/rubic/rubic
./HornSchunck.py data/sphere/sphere
"""
from logging import getLogger
import imageio
from matplotlib.pyplot import show
from scipy.ndimage.filters import gaussian_filter
#
from .pyoptflow import HornSchunck, getimgfiles
from .pyoptflow.plots import compareGraphs

logger = getLogger(__name__)

FILTER = 7


def horn_schunck(stem, pat:str, g_filter:int=FILTER):
    flist = getimgfiles(stem, pat)
    logger.info(f"Found {len(flist)} files")

    for i in range(len(flist)-1):
        fn1 = flist[i]
        logger.info(f"Loading file {fn1}")
        im1 = imageio.imread(fn1, as_gray=True)

        fn2 = flist[i+1]
        im2 = imageio.imread(fn2, as_gray=True)

        im1 = gaussian_filter(im1, g_filter)
        im2 = gaussian_filter(im2, g_filter)

        U,V = HornSchunck(im1, im2, 1., 100)
        compareGraphs(U,V, im2, fn=fn2.name, scale=10)

    return U,V


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='Pure Python Horn Schunck Optical Flow')
    p.add_argument('stem',help='path/stem of files to analyze')
    p.add_argument('pat',help='glob pattern of files',default='*.bmp')
    p = p.parse_args()

    U,V = horn_schunck(p.stem, p.pat)

    show()
