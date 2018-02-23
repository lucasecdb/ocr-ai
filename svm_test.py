from skimage.io import imread
from skimage.feature import hog

from sklearn.svm import LinearSVC

import numpy as np

s1 = imread('./data/GoodImg/Bmp/Sample001/img001-00001.png', as_grey=True)
s2 = imread('./data/GoodImg/Bmp/Sample002/img002-00002.png', as_grey=True)

(x1, y1) = s1.shape
(x2, y2) = s2.shape

x_diff = x1 - x2
y_diff = y1 - y2

s2 = np.pad(s2, ((x_diff, 0), (y_diff, 0)), 'constant')

hi1 = hog(image=s1, block_norm='L2-Hys', pixels_per_cell=(4, 4))
hi2 = hog(image=s2, block_norm='L2-Hys', pixels_per_cell=(4, 4))

agent = LinearSVC()

agent.fit([hi1, hi2], [1, 2])

print(agent.predict([[0 for _ in range(len(hi1))]]))
