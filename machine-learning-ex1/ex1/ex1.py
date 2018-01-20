import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from scipy import io
from sklearn.linear_model import LinearRegression


def load_data(filename):
    '''
    读取数据，将其转换为np.array的形式，将x和y以元组形式返回，解包获取数据
    '''
    column1 = list()
    column2 = list()
    with open(filename) as fp:
        for line in fp.readlines():
            line = line.strip()
            a, b = line.split(',')
            column1.append(a)
            column2.append(b)
    column1 = np.array(column1).astype(float)
    column2 = np.array(column2).astype(float)
    return column1, column2


def plot_data(X, y, Xlabel, ylabel):
    '''
    将图像进行描绘，散点图
    '''
    plt.figure()
    plt.plot(X, y, 'rx', 'MarkerSize', 10)
    plt.xlabel(Xlabel)
    plt.ylabel(ylabel)
    # plt.show()


def compute_cost(X: np.matrix, y: np.matrix, theta: np.matrix)->float:
    m = len(y)
    # 最小二乘法计算损失
    tmp = np.dot(X, theta.T)-y
    loss = 1/(2*m)*np.dot(tmp.T, tmp)
    return loss


if __name__ == '__main__':
    # part1
    # 从文件之中读取数据
    X, y = load_data('./ex1data1.txt')
    plot_data(X, y, 'Profit in $10,000s', 'Population of City in 10,000s')
    # 使用线性回归进行模拟
    model = LinearRegression()
    # 对数据进行处理，形式变为列的形式
    train = X.T
    tmp = np.ones((X.shape[0], 1))
    train = np.concatenate((np.ones((X.shape[0], 1)), X[:, None]), axis=1)
    model.fit(train, y)
    plt.figure(1)
    predict = model.predict(train)
    plt.plot(X, predict)
    # plt.show()

    # part2
    theta1 = np.linspace(-10, 10, 100)
    theta2 = np.linspace(-1, 4, 100)
    # 存储损失，后面画出等线图
    J_all = np.zeros((len(theta1), len(theta2)))
    for i, m in enumerate(theta1):
        for j, n in enumerate(theta2):
            theta = np.array([m, n]).T
            J_all[i][j] = compute_cost(train, y, theta)
    pic = plt.figure(2)
    ax = pic.gca(projection='3d')
    surf = ax.plot_surface(theta1, theta2, J_all, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))

    pic.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
