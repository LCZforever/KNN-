# KNN_lcz 就是LCZ写的KNN,用于生成和加载数据集
import cv2
import numpy as np


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


def min_chayi(chayi, rang):   # 计算差异列表中，n个内相近的数字个数，并返回次数最多的数字
    frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nums = []
    first = True
    for i in range(10):   # 先排序
        for j in chayi[i]:
            if first:
                nums.append([i, j])
                first = False
            else:
                k = 0
                for num in nums:
                    if j < num[1]:
                        nums.insert(k, [i, j])
                        break
                    else:
                        k += 1
                        if k == len(nums):
                            nums.append([i, j])
                            break
    print(nums)
    nums_array = np.array(nums)[:rang+1, 0]
    print(nums_array)
    for i in nums_array:            # 统计次数
            frequency[i] += 1

    print(frequency)
    times = frequency[0]
    result = 0
    n = 0
    for i in frequency:     # 选最大的数字的序号
        if times < i:
            times = i
            result = n
        n += 1
    return result



def recognition(test_img_path='test_image.bmp', sample_path='numbers.npz', rang=100):  # 总函数,参数:测试图，样本路径名，近邻范围
    num = np.load(sample_path)   # 读入样本
    image = num['nums']
    image_chayi = []  # 差异度矩阵
    res = deal_test_photo(test_img_path)   # 对测试图片进行预处理
    for i in range(10):
        j = 0
        image_chayi.append([i])
        for k in range(len(image[i])-1):          # 初始化差异度列表
            image_chayi[i].append(0)
        for img in image[i]:
            if j == 0:          # 首个是数字标签，跳过
                j += 1
                continue
            image_chayi[i][j] = chaiyi(res, img)      # 计算与每个样本的差异，存入差异列表
            j += 1
    print(image_chayi)
    the_num = min_chayi(image_chayi, rang)   # 处理差异列表，得出最终数字
    return the_num
    cv2.imshow("image", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


number = recognition('6_476.bmp')
print('结果是'+str(number))
