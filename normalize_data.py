import os

from skimage.io import imread, imsave
from skimage.exposure import equalize_hist
from skimage.transform import resize

out_dir = './data/normalized'

MEDIAN_HEIGHT = 87
MEDIAN_WIDTH = 62

for path, dir, files in os.walk('./data'):
    for file in files:
        image = imread(os.path.join(path, file), as_grey=True)

        image = resize(image, (MEDIAN_HEIGHT, MEDIAN_WIDTH))
        image = equalize_hist(image)

        imsave(os.path.join(out_dir, file), image)
