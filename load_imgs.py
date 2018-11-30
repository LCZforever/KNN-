# 读取图片并保存
import cv2
from multiprocessing import Pool
import numpy as np

def deal_input_photo(image):
    ret, img = cv2.threshold(image, 175, 255, cv2.THRESH_BINARY)  # 二值
    res = cv2.resize(img, (28, 28), interpolation=cv2.INTER_CUBIC)   # 图片矩阵的缩放
    return res


def load_num_pic(num):
    img = [num]
    i_s = str(num)
    for j in range(1200):
        j_s = str(j)
        image = cv2.imread('t10k-images/' + i_s + '_' + j_s + '.bmp', 0)
        if image is None:
            print('break in ' + 't10k-images/' + i_s + '_' + j_s + '.bmp')
            break
        else:
            image = deal_input_photo(image)
            img.append(image)
    return img


if __name__ == '__main__':
    e1 = cv2.getTickCount()
    pool = Pool()       # 使用多进程
    result_list = pool.map(load_num_pic, [i for i in range(10)])    # 返回所有返回值的列表，注意是乱序
    print('读取时间为:'+str((cv2.getTickCount() - e1) / cv2.getTickFrequency())+'s')   # 读取时间
    image = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]  # 用于按顺序存放数字图片矩阵,从一开始
    for i in range(10):   # 重新排序
        image[result_list[i][0]] = result_list[i]

    np.savez('numbers.npz', nums=image)


