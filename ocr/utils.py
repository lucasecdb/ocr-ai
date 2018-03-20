import os
import re
import numpy as np

from skimage.io import imread
from skimage.feature import hog


def get_dataset(base_path):
    data_labels = []
    hog_features = []

    for path, dir, files in os.walk(base_path):
        for file in files:
            label = re.search('0+(.+?)-', file)
            features = hog(image=imread(os.path.join(path, file)), orientations=4,
                           block_norm='L2', pixels_per_cell=(4, 4), cells_per_block=(2, 2))
            hog_features.append(features)
            if label:
                data_labels.append(label.group(1))

    return (np.array(hog_features), data_labels)
