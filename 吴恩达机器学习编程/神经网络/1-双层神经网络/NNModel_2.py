import numpy as np


#sigmod 函数
def sigmod(z):
    '''
       参数：
          z - 任何大小的标量或numpy数组
       返回：
          sigmod(z)函数值,如果是数组，则相当于对每个元素进行sigmod计算
    '''
    return 1/(1+np.exp(-z))

# 定义神经网络结构
def layer_sizes(X, Y):
    """
        Arguments:
        X -- 输入数据集的维度 (特征数量,样本数量)
        Y -- 标签维度 (输出数量, 样本数量)

        Returns:
        n_x -- 输入层大小 即特征数量
        n_h -- 隐藏层大小   （设为4）
        n_y -- 输出层大小
    """
    n_x = X.shape[0]  # 输入数据集的行数（每一行代表一个特征值）
    n_h = 4  # 四个隐藏单元
    n_y = Y.shape[0]  # 标签集的行数 （每一行代表一个输出值）

    return n_x, n_h, n_y


# 初始化模型参数
def initialize_parameters(n_x, n_h, n_y):
    """
      Argument:
      n_x -- 输入层大小
      n_h -- 隐藏层大小
      n_y -- 输出层大小

      Returns:
      parameters -- 包含模型参数的字典:
                      W1 -- 维度 (n_h, n_x)
                      b1 -- 维度 (n_h, 1)
                      W2 -- 维度 (n_y, n_h)
                      b2 -- 维度 (n_y, 1)
    """
    np.random.seed(2)  # 指定一个随机种子
    W1 = np.random.randn(n_h, n_x) * 0.01
    b1 = np.zeros(shape=(n_h, 1))
    W2 = np.random.randn(n_y, n_h) * 0.01
    b2 = np.zeros(shape=(n_y, 1))

    # 使用断言确保我的数据格式是正确的
    assert (W1.shape == (n_h, n_x))
    assert (b1.shape == (n_h, 1))
    assert (W2.shape == (n_y, n_h))
    assert (b2.shape == (n_y, 1))

    parameters = {
        "W1": W1,
        "b1": b1,
        "W2": W2,
        "b2": b2,
    }

    return parameters


# 循环
# -------

# 前向传播计算A2和代价
def forward_propagation(X, parameters):
    """
        Argument:
        X -- 输入数据 (n_x, m)
        parameters -- 模型参数 (initialization function的输出)

        Returns:
        A2 -- 第二层(输出层)的激活值 (1, number of examples)
        cache -- 字典： "Z1", "A1", "Z2" and "A2"
    """
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
    # 前向传播计算A2
    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)  # 隐藏层使用tanh激活函数
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmod(Z2)  # 输出层使用sigmod激活函数

    # 使用断言确保我的数据格式是正确的
    assert (A2.shape == (1, X.shape[1]))
    cache = {
        "Z1": Z1,
        "A1": A1,
        "Z2": Z2,
        "A2": A2,
    }

    return A2, cache


"""
    Arguments:
    A2 -- 第二层(输出层)的激活值 (1, number of examples)
    Y -- "true" 标签向量 (1, number of examples)
    parameters -- 模型参数 (initialization function的输出)

    Returns:
    cost -- 交叉熵代价
"""


# 计算代价函数
def compute_cost(A2, Y):
    """
    Arguments:
    A2 -- 第二层(输出层)的激活值 (1, number of examples)
    Y -- "true" 标签向量 (1, number of examples)
    parameters -- 模型参数 (initialization function的输出)

    Returns:
    cost -- 交叉熵代价
    """
    # Y的列数 样本数量
    m = Y.shape[1]

    logprobs = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
    cost = - np.sum(logprobs) / m
    cost = np.squeeze(cost)

    return cost


# 反向传播计算梯度
def backward_propagation(parameters, cache, X, Y):
    """
    Arguments:
    parameters -- 模型参数 (initialization function的输出)
    cache -- 字典： "Z1", "A1", "Z2" and "A2"
    X -- 输入数据 (n_x, m)
    Y -- "true" 标签向量 (1, number of examples)

    Returns:
    grads -- 字典：包含不同参数的梯度
    """

    m = Y.shape[1]  # 样本数量
    # W1 = parameters["W1"]
    W2 = parameters["W2"]
    A1 = cache["A1"]
    A2 = cache["A2"]

    dZ2 = A2 - Y
    dW2 = (1 / m) * np.dot(dZ2, A1.T)
    db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)  # 将每一行的元素相加,将矩阵压缩为一列 保持矩阵的二维特性
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))  # 数组和矩阵对应位置相乘
    dW1 = (1 / m) * np.dot(dZ1, X.T)
    db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)

    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    return grads


# 更新参数（梯度下降算法）
def update_parameters(parameters, grads, learning_rate=1.2):
    """
    Arguments:
    parameters -- 模型参数 (initialization function的输出)
    grads -- 字典：包含不同参数的梯度

    Returns:
    parameters -- 更新后的模型参数
     parameters -- 包含模型参数的字典:
                      W1 -- 维度 (n_h, n_x)
                      b1 -- 维度 (n_h, 1)
                      W2 -- 维度 (n_y, n_h)
                      b2 -- 维度 (n_y, 1)
    """
    # 获取原来的参数
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    # 获取参数的梯度
    dW1 = grads['dW1']
    db1 = grads['db1']
    dW2 = grads['dW2']
    db2 = grads['db2']
    # 更新参数
    W1 = W1 - dW1 * learning_rate
    b1 = b1 - db1 * learning_rate
    W2 = W2 - dW2 * learning_rate
    b2 = b2 - db2 * learning_rate

    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    return parameters


# 创建双层神经网络
def nn_model(X, Y, n_h, num_iterations=10000, print_cost=False):
    """
        Arguments:
        X -- 数据集 (特征数量,样本数量)
        Y -- 标签 (输出数量, 样本数量)
        n_h -- 隐藏层大小   （设为4）
        num_iterations -- 梯度下降循环中的迭代次数
        print_cost -- 如果为True，则每1000次迭代打印一次成本数值

        Returns:
        parameters -- 模型学习的参数，它们可以用来进行预测
    """
    np.random.seed(3)  # 指定随机种子
    n_x = layer_sizes(X, Y)[0]  # 输入层大小 即特征数量
    n_y = layer_sizes(X, Y)[2]  # 输出层大小

    # 初始化模型参数
    parameters = initialize_parameters(n_x, n_h, n_y)
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']

    # 梯度下降循环
    for i in range(0, num_iterations):
        # 前向传播
        A2, cache = forward_propagation(X, parameters)
        cost = compute_cost(A2, Y)  # 计算代价

        # 反向传播
        grads = backward_propagation(parameters, cache, X, Y)  # 计算梯度
        parameters = update_parameters(parameters, grads)  # 更新参数

        if print_cost and i % 1000 == 0:
            print("第 ", i, " 次循环，成本为：" + str(cost))
    return parameters

# 预测结果
def predict(parameters, X):
    """
    Arguments:
    parameters -- 你训练后的模型参数
    X -- 数据集 (特征数量,样本数量)

    Returns
    predictions -- 预测结果向量 (red: 0 / blue: 1)
    """
    # 以0.5为阈值
    A2 , cache = forward_propagation(X,parameters)
    predictions = np.round(A2)
    return predictions