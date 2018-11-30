# 相当于草稿本，随便写点什么
# 用于测试整个程序，生成准确率和错误信息
# 最后这里面向给用户
import cv2
from KNN_lcz import recognition

name = '6_476.bmp'
e1 = cv2.getTickCount()
number = recognition(name)
print('结果是'+str(number))
print('读取时间为:' + str((cv2.getTickCount() - e1) / cv2.getTickFrequency()) + 's')  # 读取时间
img = cv2.imread(name)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
