import numpy as np
import math
from scipy.stats import chi2
def Bayes_classify(sample,test):
    # sample为样本集，n为种类数
    G1 = np.mat(sample[0:6])
    G2 = np.mat(sample[6:15])
    n1 = G1.shape[0]
    n2 = G2.shape[0]
    N = n1+n2     #样本个数
    n = np.mat(sample).shape[1]   #特征数
    K = 2 #类别数目
    f = n * (n + 1) * (K - 1) / 2  #统计量自由度
    d = (2 * n ^ 2 + 3 * n - 1) * (1 / (n1 - 1) + 1 / (n2 - 1) - 1 / (N - K)) / (6 * (n + 1) * (K - 1))
    S1 = np.cov(G1.T)
    S2 = np.cov(G2.T)
    S = ((n1-1)*S1 + (n2-1)*S2)/(N-K)
    Z = (N - K) * math.log(np.linalg.det(S)) - ((n1 - 1) * math.log(np.linalg.det(S1)) + (n2 - 1) * math.log(np.linalg.det(S2)))
    T = (1 - d) * Z
    a = 0.05
    C = chi2.ppf(1 - a, f)
    if T < C:
        print('三类样本协方差矩阵相等')
    else:
        print('三类样本协方差矩阵不全相等')

    # 以上部分代码判断各类样本的协方差矩阵是否相等，下部分将进行判别

    pw1 = n1 / n
    pw2 = n2 / n #先验概率
    m1 = np.mean(G1,0).T
    m2 = np.mean(G2,0).T
    g1 = m1.T * np.linalg.inv(S) * test - 1 / 2 * m1.T * np.linalg.inv(S) * m1 + math.log(pw1)
    g2 = m2.T * np.linalg.inv(S) * test - 1 / 2 * m2.T * np.linalg.inv(S) * m2 + math.log(pw2)
    compare_list = [g1,g2]
    if(g1 == max(compare_list)):
        print('样本属于Apf类')
    if (g2 == max(compare_list)):
        print('样本属于Af类')


if __name__ == '__main__':
    sample =[[1.14,1.78],[1.18,1.96],[1.20,1.86],[1.26,2.00],[1.30,2.00],[1.28,1.96],
             [1.24, 1.72],[1.36, 1.74],[1.38, 1.64],[1.38, 1.82],[1.38, 1.90],[1.40, 1.70],[1.48, 1.82],[1.54, 2.08],[1.56, 1.78]]
    test1 = np.mat([1.24,1.80]).T
    test2 = np.mat([1.28,1.84]).T
    test3 = np.mat([1.40,2.04]).T
    Bayes_classify(sample,test1)
    Bayes_classify(sample, test2)
    Bayes_classify(sample, test3)