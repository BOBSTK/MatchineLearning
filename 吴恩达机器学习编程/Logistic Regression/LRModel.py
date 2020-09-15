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

#初始化参数
def initialize_with_zeros(dim):
    '''
        此函数创建一个维度为(dim,1)的0向量w，并将b初始化为0
        参数：
           dim：w向量的维度
        返回：
           w - 维度为(dim,1)的0向量
           b - 初始化标量(对应偏差)
    '''
    w = np.zeros((dim,1))
    b = 0
    # 使用断言来确保我要的数据是正确的
    assert (w.shape == (dim, 1))  #w的维度是(dim,1)
    assert (isinstance(b, float) or isinstance(b, int)) #b的类型是float或者是int
    return w, b

#使用前向传播和后向传播计算代价函数和梯度
def propagate(w,b,X,Y):
    '''
        此函数创建一个维度为(dim,1)的0向量w，并将b初始化为0
        参数：
            w -- 权重, a numpy array of size (num_px * num_px * 3, 1)
            b -- 偏差, 一个标量
            X -- data of size (num_px * num_px * 3, 训练数据数量)
            Y -- 正确的 "label" vector (containing 0 if non-cat, 1 if cat) of size (1, 训练数据数量)
            返回：
            代价 -- negative log-likelihood cost for logistic regression
            dw -- gradient of the loss with respect to w, thus same shape as w
            db -- gradient of the loss with respect to b, thus same shape as b
    '''
    m = X.shape[1] #样本数量
    # 前向传播 (从 X 计算 COST)
    z = np.dot(w.T,X)+b
    A = sigmod(z)  #m * 1

    cost = (- 1 / m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))

    # 反向传播 (计算梯度)
    dz = A- Y
    db = (1/m)* np.sum(dz)
    dw = (1/m)* np.dot(X,dz.T)

    # 使用断言确保数据格式是正确的
    assert (dw.shape == w.shape)
    assert (db.dtype == float)
    cost = np.squeeze(cost)   #从数组的形状中删除单维条目
    assert (cost.shape == ())
    # 创建一个字典，把dw和db保存起来
    grads = {"dw": dw,
             "db": db}

    return grads, cost

#使用梯度下降来优化参数
def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost = False):
    """
        此函数通过运行梯度下降算法来优化w和b

        参数:
            w -- 权重, a numpy array of size (num_px * num_px * 3, 1)
            b -- 偏差, 一个标量
            X -- data of size (num_px * num_px * 3, 训练数据数量)
            Y -- 正确的 "label" vector (containing 0 if non-cat, 1 if cat) of size (1, 训练数据数量)
            num_iterations -- 优化循环迭代次数
            learning_rate -- 学习率
            print_cost -- 每循环100次输出一次代价值

        返回:
        params -- 包含权重w和偏差b的字典
        grads -- 包含权重和偏差相对于成本函数的梯度的字典
        costs -- 优化期间计算的所有成本列表，将用于绘制学习曲线

        提示：
        我们需要写下两个步骤并遍历它们：
        1）计算当前参数的成本和梯度，使用propagate（）
        2）使用w和b的梯度下降法则更新参数。
        """
    costs = []
    #迭代次数循环
    for i in range(num_iterations):
        grads , cost = propagate(w,b,X,Y)  #计算当前代价和梯度
        dw = grads["dw"]
        db = grads["db"]
        #更新参数
        w = w - learning_rate * dw
        b = b - learning_rate * db
        #没迭代100次记录一次代价值
        if(i%100 == 0):
            costs.append(cost)
        if(print_cost and i%100 == 0):
            print("Cost after iteration %i: %f" % (i, cost)) #输出代价值
    #字典存放最新的参数
    params = {"w":w,
              "b":b
                  }
    grads = { "dw":dw,
              "db":db}
    return params,grads,costs

# 预测
def predict(w,b,X):
    '''
        根据学习到的参数（w,b）预测样本是属于标签0还是标签1

        参数:
            w -- 权重, a numpy array of size (num_px * num_px * 3, 1)
            b -- 偏差, 一个标量
            X -- data of size (num_px * num_px * 3, 测试数据数量)

        返回:
        Y_prediction -- 包含X中所有图片的所有预测【0 | 1】的一个numpy数组（向量）
    '''
    m = X.shape[1]  #测试集数据数量
    Y_prediction = np.zeros((1, m)) #测试集
    w = w.reshape(X.shape[0], 1) # m*1 向量
    #计算猫出现在图片中的概率
    z = np.dot(w.T,X)+b
    A = sigmod(z)
    #遍历A中的每一个概率值
    for i in range(A.shape[1]):
        # 将概率a [0，i]转换为实际预测p [0，i]并存入Y_prediction
        Y_prediction[0,i] = 1 if(A[0,i]>0.5) else 0
    # 使用断言确定输出合法性
    assert (Y_prediction.shape == (1, m))

    return Y_prediction

#逻辑回归整合函数
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    """
        实现逻辑回归的函数，梯度下降算法

        参数:
        X_train -- 训练集，维度为（num_px * num_px * 3，m_train）
        Y_train -- 训练标签集，维度为（1，m_train）
        X_test -- 测试集，维度为（num_px * num_px * 3，m_test）
        Y_test -- 测试标签集，维度为（1，m_test）
        num_iterations -- 优化迭代次数
        learning_rate -- 学习率
        print_cost -- 每迭代100次打印迭代成本

        返回:
        d -- 包含有关模型信息的字典
    """
    #初始化参数
    w,b = initialize_with_zeros(X_train.shape[0])
    #学习参数
    params,grads,costs = optimize(w,b,X_train,Y_train,num_iterations,learning_rate,print_cost)
    #获取参数
    w = params["w"]
    b = params["b"]
    # 预测测试/训练集的例子
    Y_prediction_test = predict(w,b,X_test)
    Y_prediction_train = predict(w,b,X_train)
    #打印训练后准确性
    print("训练集准确性:{}%".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100) )
    print("测试集准确性: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))
    d = {
        "costs": costs,                                  #代价值字典
        "Y_prediction_test": Y_prediction_test,          #测试集结果
        "Y_prediciton_train": Y_prediction_train,        #训练集结果
        "w": w,
        "b": b,
        "learning_rate": learning_rate,
        "num_iterations": num_iterations
    }
    return d