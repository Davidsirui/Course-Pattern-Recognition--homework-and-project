import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

dirtybit = 0 #迭代结束标志为权向量没有经过一次修改
iterate_numbers = 0 #迭代次数
w1 = np.mat([1,1,1]).T #初始权向量

def Add_colum(A):     #将A矩阵变成增广矩阵
     return A+([1])

def Test_of_sample(x,w,p,sample_class):  #对单个样本进行一次处理的判别函数
    if sample_class > 0:
         result = int(w.T*x)
         p = p
    else:
         result = (-int(w.T*x))
         p = -p
    global dirtybit
    if result>0:
         w = w
    else:
         w = w + p*x
         dirtybit = dirtybit + 1
    return w

def Iteration():#迭代函数
     global iterate_numbers
     global w1
     global  dirtybit
     dirtybit = 0
     for i in range(0,n):
               x = np.mat(Add_colum((train_sample[i]))).T
               sampleclass = sample_class[i]
               w1 = Test_of_sample(x,w1,pk,sampleclass)
               i = i+1
     iterate_numbers = iterate_numbers + 1


if __name__ == '__main__':
    pk = 1
    
    n = 4    #样本个数
    i = 0 #内层循环哨兵
    train_sample = [([0,0]),([0,1]),([1,0]),([1,1])]#训练集
    sample_class = [(1),(1),(-1),(-1)]#训练集对应的标签或类别
    while (iterate_numbers<=99):
        Iteration()
        if(dirtybit == 0):
              break;
    if(iterate_numbers<100): #若目标函数在规定的最大迭代次数内可以收敛
       print('迭代次数为：',iterate_numbers)
       print('最终的解向量为', '\n', w1)
    else:#若目标函数在规定的最大迭代次数内无法收敛
       print('迭代次数为：',iterate_numbers)
       print('无法收敛，其中一个解向量为', '\n', w1)
    #实现数据可视化
    # 创建 3D 图形对象
    fig = plt.figure()
    ax = Axes3D(fig)
    # 生成数据
    X = np.arange(-2, 2, 0.1)
    Y = np.arange(-2, 2, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = 3 * X
    # 绘制曲面图，并使用 cmap 着色
    ax.scatter(0, 1, 1, c='y')
    ax.scatter(0, 0, 1, c='y')
    ax.scatter(1, 0, 1, c='r')
    ax.scatter(1, 1, 1, c='r')
    ax.plot_surface(X, Y, Z, cmap=plt.cm.winter)

    plt.show()