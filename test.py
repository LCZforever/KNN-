# 相当于草稿本，随便写点什么
# 用于测试整个程序，生成准确率和错误信息
# 最后这里面向给用户
import cv2
from KNN_lcz import recognition
import time
# 检测准确率步骤：
# 将测试图一一测试，如果对，则正确数加一，最后正确数除以总数即为正确率

def test():
    right_sum = 0
    all_sum = 0
    for i in range(10):
        i_s = str(i)
        for j in range(501, 1000):
            time_1 =time.time()
            j_s = str(j)
            name = 't10k-images/' + i_s + '_' + j_s + '.bmp'
            number = recognition(name)
            if number is None:
                print('break in', j_s)
                break
            else:
                all_sum += 1
                if number == i:
                    print('Right', number, time.time()-time_1,'s')
                    right_sum += 1
                else:
                    print('Wrong')
                    print(name)
    print(right_sum,all_sum)
    return right_sum/all_sum


e1 = cv2.getTickCount()
right_lv = test()
print('读取时间为:' + str((cv2.getTickCount() - e1) / cv2.getTickFrequency()) + 's')  # 读取时间
print('准确率为', right_lv)
img = cv2.imread('6_476.bmp')
if not img.all() :
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

