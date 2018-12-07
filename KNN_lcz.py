# KNN_lcz 就是LCZ写的KNN,用于生成和加载数据集
import cv2
import numpy as np
import heapq
from collections import Counter

def fan_se(image):   # 反色
    height, width = image.shape
    num_0 = 0
    copy_image = image.copy()
    # print(str(height) + ',' + str(width))
    for i in range(height):
        for j in range(width):
            if image[i][j]:
                num_0 += 1
            image[i][j] = 255-image[i][j]
    if num_0 < height*width*0.5:      # 判断是黑底还是白底，黑底返回原图
        return copy_image
    else:
        return image


def deal_test_photo(image_path):
    image = cv2.imread(image_path, 0)   # 黑白读取
    if image is None:
        return None
    ret, img = cv2.threshold(image, 175, 255, cv2.THRESH_BINARY)  # 二值
    res = cv2.resize(img, (28, 28), interpolation=cv2.INTER_CUBIC)   # 缩放
    out = fan_se(res)  # 反色
    return out


def chaiyi(image_a,image_b):   # 计算两张图的差异度,这里使用最简单的做法，即统计相同相同位置上相同像素的个数
    chayi_num = 0
    for i in range(28):
        for j in range(28):
            if image_a[i][j] != image_b[i][j]:
                chayi_num += 1
    return chayi_num


def change_list_form(lis):   # 改变列表的形状：10*n -> (10*n)*(2*1)
    new_lis = []
    for i,li in zip(range(len(lis)), lis):
        for j in li:
            new_lis.append([i, j])
    return new_lis


def min_chayi(chayi, rang):   # 计算差异列表中，range个内相近的数字的个数，并返回次数最多的数字
    chayi_s = change_list_form(chayi)
    cheap = heapq.nsmallest(100, chayi_s, key=lambda s: s[1])  # 通过索引找出最大的几个单位组成列表
    nums_array = np.array(cheap)[:, 0]
    num_counts = Counter(nums_array)    # 选取列表中出现次数最多的数字以及其出现的次数
    top_num = num_counts.most_common(10)
    return top_num[0][0]


def recognition(test_img_path='test_image.bmp', sample_path='numbers.npy', rang=100):  # 总函数,参数:测试图，样本路径名，近邻范围
    res = deal_test_photo(test_img_path)   # 对测试图片进行预处理
    if res is None:
        return None
    image = np.load(sample_path)   # 读入样本
    image_chayi = []  # 差异度矩阵
    for i in range(10):
        j = 0
        image_chayi.append([i])
        for k in range(len(image[i])-1):          # 初始化差异度列表
            image_chayi[i].append(0)
        e1 = cv2.getTickCount()
        for img in image[i]:
            if j == 0:          # 首个是数字标签，跳过
                j += 1
                continue
            image_chayi[i][j] = chaiyi(res, img)      # 计算与每个样本的差异，存入差异列表
            j += 1
        #print('读取时间为:' + str((cv2.getTickCount() - e1) / cv2.getTickFrequency()) + 's')  # 读取时间
    #print(image_chayi)
    e1 = cv2.getTickCount()
    the_num = min_chayi(image_chayi, rang)   # 处理差异列表，得出最终数字
    print('读取时间为:' + str((cv2.getTickCount() - e1) / cv2.getTickFrequency()) + 's')  # 读取时间
    return the_num



