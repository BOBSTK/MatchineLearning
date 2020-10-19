import numpy as np
import testCases

np.random.seed(1)

def sigmoid(Z):
    """
    Implements the sigmoid activation in numpy

    Arguments:
    Z -- numpy array of any shape

    Returns:
    A -- output of sigmoid(z), same shape as Z
    cache -- returns Z as well, useful during backpropagation
    """

    A = 1/(1+np.exp(-Z))
    cache = Z

    return A, cache

def sigmoid_backward(dA, cache):
    """
    Implement the backward propagation for a single SIGMOID unit.

    Arguments:
    dA -- post-activation gradient, of any shape
    cache -- 'Z' where we store for computing backward propagation efficiently

    Returns:
    dZ -- Gradient of the cost with respect to Z
    """

    Z = cache

    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)

    assert (dZ.shape == Z.shape)

    return dZ

def relu(Z):
    """
    Implement the RELU function.

    Arguments:
    Z -- Output of the linear layer, of any shape

    Returns:
    A -- Post-activation parameter, of the same shape as Z
    cache -- a python dictionary containing "A" ; stored for computing the backward pass efficiently
    """

    A = np.maximum(0,Z)

    assert(A.shape == Z.shape)

    cache = Z
    return A, cache

def relu_backward(dA, cache):
    """
    Implement the backward propagation for a single RELU unit.

    Arguments:
    dA -- post-activation gradient, of any shape
    cache -- 'Z' where we store for computing backward propagation efficiently

    Returns:
    dZ -- Gradient of the cost with respect to Z
    """

    Z = cache
    dZ = np.array(dA, copy=True) # just converting dz to a correct object.

    # When z <= 0, you should set dz to 0 as well. 
    dZ[Z <= 0] = 0

    assert (dZ.shape == Z.shape)

    return dZ

# 初始化模型参数 两层神经网络
# LINEAR -> RELU -> LINEAR -> SIGMOID
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

# 初始化模型参数 L层神经网络
#  [LINEAR -> RELU] * (L-1) -> LINEAR -> SIGMOID
def initialize_parameters_deep(layer_dims):
    """
        Arguments:
        layer_dims -- python array (list)  包含每一层的维度

        Returns:
        parameters -- python dictionary containing your parameters "W1", "b1", ..., "WL", "bL":
                        Wl -- weight matrix of shape (layer_dims[l], layer_dims[l-1])
                        bl -- bias vector of shape (layer_dims[l], 1)
    """
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)  # 神经网络的层数

    #初始化参数
    for l in range(1,L):
        parameters['W' + str(l)] = np.random.rand(layer_dims[l],layer_dims[l-1]) * 0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
        #断言检测维度
        assert (parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l - 1])) * 0.01
        assert (parameters['b' + str(l)].shape == (layer_dims[l], 1))
    return  parameters

#计算前向传播的Linear部分 Z = W . A + b
def linear_forward(A, W, b):
    """
        Implement the linear part of a layer's forward propagation.

        Arguments:
        A -- 来自上一层的activations（或输入数据），维度为(上一层的节点数量，示例的数量）
        W -- weights matrix: 维度为（当前图层的节点数量，前一图层的节点数量）
        b -- bias vector, 维度为（当前图层的节点数量，1）

        Returns:
        Z -- the input of the activation function, also called pre-activation parameter
        cache -- a python dictionary containing "A", "W" and "b" ; 存储这些变量以有效地计算反向传播
    """
    Z = np.dot(W,A) + b
    cache = (A,W,b)
    return Z,cache


def linear_activation_forward(A_prev, W, b, activation):
    """
    实现LINEAR-> ACTIVATION 这一层的前向传播

    参数：
        A_prev - 来自上一层（或输入层）的激活值，维度为(上一层的节点数量，示例数）
        W - 权重矩阵，numpy数组，维度为（当前层的节点数量，前一层的大小）
        b - 偏向量，numpy阵列，维度为（当前层的节点数量，1）
        activation - 选择在此层中使用的激活函数名，字符串类型，【"sigmoid" | "relu"】

    返回：
        A - 激活函数的输出，也称为激活后的值
        cache - 一个包含"linear_cache,activation_cache"的字典，我们需要存储它以有效地计算后向传递

    """
    Z, linear_cache = linear_forward(A_prev, W, b)
    if activation == "sigmoid":
        # Z, linear_cache = linear_forward(A_prev, W, b)
        A,activation_cache = sigmoid(Z)
    elif activation == "relu":
        # Z, linear_cache = linear_forward(A_prev, W, b)
        A,activation_cache = relu(Z)

    assert (A.shape == (W.shape[0], A_prev.shape[1]))
    cache = (linear_cache,activation_cache)

    return A, cache

#L_model_forward
def L_model_forward(X, parameters):
    """
    实现[LINEAR-> RELU] *（L-1） - > LINEAR-> SIGMOID计算前向传播，也就是多层网络的前向传播，为后面每一层都执行LINEAR和ACTIVATION
    Arguments:
    X -- data, 维度为（输入节点数量，示例数）
    parameters -- output of initialize_parameters_deep()

    Returns:
    AL -- last post-activation value
    caches -- list of caches containing:
                linear_relu_forward（）的每个cache（有L-1个，索引为从0到L-2）
                linear_sigmoid_forward（）的cache（只有一个，索引为L-1）
    """
    caches = []
    A = X
    L = len(parameters) // 2  # number of layers in the neural network

    # Implement [LINEAR -> RELU]*(L-1). Add "cache" to the "caches" list.
    for l in range(1,L):
        A_prev = A
        A,cache = linear_activation_forward(A_prev,parameters['W'+str(l)],parameters['b'+str(l)],"relu")
        caches.append(cache)
    # Implement LINEAR -> SIGMOID. Add "cache" to the "caches" list.
    AL,cache = linear_activation_forward(A,parameters['W'+str(L)],parameters['b'+str(L)],"sigmoid")
    caches.append(cache)

    assert (AL.shape == (1, X.shape[1]))
    return AL,caches



def compute_cost(AL, Y):
    """
    计算代价函数

    参数：
        AL - 与标签预测相对应的概率向量，维度为（1，示例数量）
        Y  - 标签向量（例如：如果不是猫，则为0，如果是猫则为1），维度为（1，数量）
    返回：
        cost - 交叉熵成本
    """
    m = Y.shape[1] #样本数量
    cost = -np.sum(np.multiply(np.log(AL), Y) + np.multiply(np.log(1 - AL), 1 - Y)) / m

    cost = np.squeeze(cost)
    assert (cost.shape == ())

    return cost

def linear_backward(dZ, cache):
    """
    Implement the linear portion of backward propagation for a single layer (layer l)

    Arguments:
    dZ -- 相对于（当前第l层的）线性输出的成本梯度
    cache -- 来自当前层前向传播的值的元组（A_prev，W，b）

    Returns:
    dA_prev -- Gradient of the cost with respect to the activation (of the previous layer l-1), same shape as A_prev
    dW -- Gradient of the cost with respect to W (current layer l), same shape as W
    db -- Gradient of the cost with respect to b (current layer l), same shape as b
    """
