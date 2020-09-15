# Package imports
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import sklearn.datasets
import sklearn.linear_model
from testCases import *
from planar_utils import plot_decision_boundary, sigmoid, load_planar_dataset, load_extra_datasets, sigmod

from NNModel_2 import nn_model,predict

# 加载和查看数据集
# X, Y = load_planar_dataset()  # 加载数据集


# 参数
# x    数据点
# y    数据点
# c    颜色(这里用数组表示颜色)
# s    点的大小
# cmap 为不同的标签指定不同的颜色
#
# plt.scatter(X[0, :], X[1, :], c=Y, s=40,cmap=plt.cm.Spectral) #绘制散点图
# plt.show()

# 数据集参数
# shape_X = X.shape   #(2,400)
# shape_Y = Y.shape   #(1,400)


# 尝试用逻辑回归解决问题
# clf = sklearn.linear_model.LogisticRegressionCV() #设置分类器模型
# clf.fit(X.T,Y.T)                                  #训练分类器

# 画出逻辑回归的决策边界
# plot_decision_boundary(lambda x: clf.predict(x), X, Y) #绘制决策边界
# plt.title("Logistic Regression") #图标题
# LR_predictions  = clf.predict(X.T) #预测结果
# print ("逻辑回归的准确性： %d " % float((np.dot(Y, LR_predictions) +
# 		np.dot(1 - Y,1 - LR_predictions)) / float(Y.size) * 100) +
#        "% " + "(正确标记的数据点所占的百分比)")
# plt.show()

# 尝试用逻辑回归解决问题
# clf = sklearn.linear_model.LogisticRegressionCV() #设置分类器模型
# clf.fit(X.T,Y.T)                                  #训练分类器

# 画出逻辑回归的决策边界
# plot_decision_boundary(lambda x: clf.predict(x), X, Y) #绘制决策边界
# plt.title("Logistic Regression") #图标题
# LR_predictions  = clf.predict(X.T) #预测结果
# print ("逻辑回归的准确性： %d " % float((np.dot(Y, LR_predictions) +
# 		np.dot(1 - Y,1 - LR_predictions)) / float(Y.size) * 100) +
#        "% " + "(正确标记的数据点所占的百分比)")
# plt.show()


# 正式运行
#X, Y = load_planar_dataset()  # 加载数据集



noisy_circles, noisy_moons, blobs, gaussian_quantiles, no_structure = load_extra_datasets()

datasets = {"noisy_circles": noisy_circles,
            "noisy_moons": noisy_moons,
            "blobs": blobs,
            "gaussian_quantiles": gaussian_quantiles}

dataset = "noisy_moons"

X, Y = datasets[dataset]
X, Y = X.T, Y.reshape(1, Y.shape[0])

if dataset == "blobs":
    Y = Y % 2

#plt.scatter(X[0, :], X[1, :], c=Y, s=40, cmap=plt.cm.Spectral)

#上一语句如出现问题请使用下面的语句：
#plt.scatter(X[0, :], X[1, :], c=np.squeeze(Y), s=40, cmap=plt.cm.Spectral)
#plt.show()

# 训练模型
parameters = nn_model(X, Y, n_h=4, num_iterations=10000, print_cost=True)
plot_decision_boundary(lambda x: predict(parameters, x.T), X, Y)
plt.title("Decision Boundary for hidden layer size " + str(4))
predictions = predict(parameters, X)
print ('Accuracy: %d' % float((np.dot(Y, predictions.T) + np.dot(1 - Y, 1 - predictions.T)) / float(Y.size) * 100) + '%')

plt.show()