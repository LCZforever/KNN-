# 相当于草稿本，随便写点什么
# 用于测试整个程序，生成准确率和错误信息
# 最后这里面向给用户
import cv2
import numpy as np

sample_path='numbers.npz'
num = np.load(sample_path)  # 读入样本
image = num['nums']

cv2.imshow("image", image[2][8])
cv2.waitKey(0)
cv2.destroyAllWindows()
