# 相当于草稿本，随便写点什么
# 用于测试整个程序，生成准确率和错误信息
from multiprocessing import Pool

def haha(num):
    return num


if __name__ == '__main__':
    pool = Pool()
    re_list = pool.map(haha, [i for i in range(10)])
    print(re_list)