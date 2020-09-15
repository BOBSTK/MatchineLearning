import numpy as np
import matplotlib.pyplot as plt
import h5py
from PIL import Image
from scipy import ndimage
from LRModel import model
from lr_utils import load_dataset #引入load_dataset方法

# 加载数据 (cat/non-cat)
# train_set_x_orig ：保存的是训练集里面的图像数据（本训练集有209张64x64的图像）
# train_set_y_orig ：保存的是训练集的图像对应的分类值（【0 | 1】，0表示不是猫，1表示是猫）
# test_set_x_orig ：保存的是测试集里面的图像数据（本训练集有50张64x64的图像）
# test_set_y_orig ： 保存的是测试集的图像对应的分类值（【0 | 1】，0表示不是猫，1表示是猫）
# classes ： 保存的是以bytes类型保存的两个字符串数据，数据为：[b’non-cat’ b’cat’]
# _orig 图片需要预处理，而标签不用
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

# Example of a picture
# index = 27
# plt.imshow(train_set_x_orig[index])
# print ("y = " + str(train_set_y[:,index]) + ", it's a '" + classes[np.squeeze(train_set_y[:,index])].decode("utf-8") +  "' picture.")
# plt.show()

#计算样本参数
m_train = train_set_y.size
m_test = test_set_y.size
num_px = train_set_x_orig.shape[1]

# 训练集的数量: m_train = 209
# 测试集的数量: m_test = 50
# 每张图片的宽/高: num_px = 64
# 每张图片的大小: (64, 64, 3)
# train_set_x的维数: (209, 64, 64, 3)
# train_set_y的维数: (1, 209)
# test_set_x的维数: (50, 64, 64, 3)
# test_set_y的维数: (1, 50)

#将[64,64,3]的图片数据重新构造为 [64*64*3]的列向量 每列代表一个图像

train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0],-1).T
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0],-1).T
# train_set_x_flatten shape: (12288, 209)
# train_set_y shape: (1, 209)
# test_set_x_flatten shape: (12288, 50)
# test_set_y shape: (1, 50)
# sanity check after reshaping: [17 31 56 22 33]
#检查train_set_x_flatten第1列的前5个元素
#print ("sanity check after reshaping: " + str(train_set_x_flatten[0:5,0]))

#为每个像素指定RGB 标准化我们的数据集
train_set_x = train_set_x_flatten / 255.
test_set_x = test_set_x_flatten / 255.

#d = model(train_set_x,train_set_y,test_set_x,test_set_y,num_iterations = 2000,learning_rate = 0.005, print_cost = True)

#绘制图
learning_rates = [0.005,0.01, 0.001, 0.0001]
models = {}
for i in learning_rates:
    print ("learning rate is: " + str(i))
    models[str(i)] = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations = 1500, learning_rate = i, print_cost = False)
    print ('\n' + "-------------------------------------------------------" + '\n')

for i in learning_rates:
    plt.plot(np.squeeze(models[str(i)]["costs"]), label= str(models[str(i)]["learning_rate"]))

plt.ylabel('cost')
plt.xlabel('iterations')

legend = plt.legend(loc='upper center', shadow=True)
frame = legend.get_frame()
frame.set_facecolor('0.90')
plt.show()




