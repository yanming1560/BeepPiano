import winsound
import time
import numpy as np


ALL = [int(round(440 * (2 ** (1 / 12)) ** (i - 49), 0)) for i in range(1, 89)]      # 所有键盘频率
num_C4 = 39     # C4位置开头
num_A4 = 48     # F4位置
natural_major = [-1, 0, 2, 4, 5, 7, 9, 11, 12]      # 自然大调间隔


def get(base):
    # 1=C4的音符计算
    nn = [ALL[base + i] for i in natural_major]       # 中央组
    nnl1 = [ALL[base + i - 12] for i in natural_major]    # 低1组
    nnh1 = [ALL[base + i + 12] for i in natural_major]    # 高1组
    return nn, nnl1, nnh1


def run(f):
    duration = 500  # 一个音拍0.5s
    for i in f:
        for j in i:
            winsound.Beep(j, duration)

def run_speed(f, s):
    for i, val1 in enumerate(f):
        for j, val in enumerate(val1):
            winsound.Beep(val, int(s[i][j] * 500))


def nshen():
    nn, nnl1, nnh1 = get(base=num_C4)
    f = [[nn[3], nn[3], nn[4], nn[5]], [nn[5], nn[4], nn[3], nn[2]], [nn[1], nn[1], nn[2], nn[3]], [nn[3], nn[2], nn[2], nn[2]]]
    run(f)


def sky():
    nn, nnl1, nnh1 = get(base=num_C4)
    f = [[nnl1[6], nnl1[7]], [nn[1], nnl1[7], nn[1], nn[3]], [nnl1[7], nnl1[3]], [nnl1[6], nnl1[5], nnl1[6], nn[1]], [nnl1[5], nnl1[3]]]
    s = [[0.5, 0.5], [1.5, 0.5, 1, 1], [3, 1], [1.5, 0.5, 1, 1], [3, 1]]

    run_speed(f, s)

sky()
