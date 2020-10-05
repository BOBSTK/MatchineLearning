import numpy as np
import time
import h5py
import matplotlib.pyplot as plt
from lr_utils import load_dataset #引入load_dataset方法
from dnn_utils import *
from PIL import  Image
import  scipy
from scipy import  ndimage

np.random.seed(1)

# 加载数据 (cat/non-cat)
# train_x_orig ：保存的是训练集里面的图像数据（本训练集有209张64x64的图像）
# train_y ：保存的是训练集的图像对应的分类值（【0 | 1】，0表示不是猫，1表示是猫）
# test_x_orig ：保存的是测试集里面的图像数据（本训练集有50张64x64的图像）
# test_y ： 保存的是测试集的图像对应的分类值（【0 | 1】，0表示不是猫，1表示是猫）
# classes ： 保存的是以bytes类型保存的两个字符串数据，数据为：[b’non-cat’ b’cat’]
# _orig 图片需要预处理，而标签不用
train_x_orig, train_y, test_x_orig, test_y, classes = load_dataset()

#计算样本参数
m_train = train_x_orig.shape[0]
num_px = train_x_orig.shape[1]
m_test = test_x_orig.shape[0]
# 训练集的数量: m_train = 209
# 测试集的数量: m_test = 50
# 每张图片的宽/高: num_px = 64
# 每张图片的大小: (64, 64, 3)
# train_x_orig 的维数: (209, 64, 64, 3)
# train_y 的维数: (1, 209)
# test_x_orig 的维数: (50, 64, 64, 3)
# test_y 的维数: (1, 50)

#将[64,64,3]的图片数据重新构造为 [64*64*3]的列向量 每列代表一个图像
train_x_flatten  = train_x_orig.reshape(train_x_orig.shape[0],-1).T
test_x_flatten  = test_x_orig.reshape(test_x_orig.shape[0],-1).T
#为每个像素指定RGB 标准化我们的数据集
train_x = train_x_flatten / 255
test_x = test_x_flatten/ 255
# train_x's shape: (12288, 209)
# test_x's shape: (12288, 50)

