# KNN_lcz 就是LCZ写的KNN,用于生成和加载数据集
import cv2
import numpy as np


num = np.load('numbers.npz')
image = num['nums']















cv2.imshow("image", image[8][1])
cv2.waitKey(0)
cv2.destroyAllWindows()
