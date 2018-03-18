import os
import re

from skimage.io import imread
from skimage.feature import hog

out_file = './data/dataset'

with open(out_file, 'w') as dataset_file:
    for path, dir, files in os.walk('./data/normalized'):
        for file in files:
            label = re.search('0+(.+?)-', file)
            if label == None:
                print(file)
            label = label.group(1)
            image = imread(os.path.join(path, file))
            image_hog = hog(image, block_norm='L2-Hys')

            line = label + ' ' + \
                ' '.join(['%d:%.7f' % (i + 1, image_hog[i])
                          for i in range(len(image_hog))])

            dataset_file.write(line + '\n')
