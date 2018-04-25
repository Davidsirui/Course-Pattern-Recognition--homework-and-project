import numpy as np
import math
from scipy.stats import chi2
def Bayes_classify(sample,test):
    # sample为样本集，n为种类数
    G1 = np.mat(sample[0:11])
    G2 = np.mat(sample[11:18])
    G3 = np.mat(sample[18:23])
    n1 = G1.shape[0]
    n2 = G2.shape[0]
    n3 = G3.shape[0]
    N = n1+n2+n3      #样本个数
    n = np.mat(sample).shape[1]   #特征数
    K = 3 #类别数目
    f = n * (n + 1) * (K - 1) / 2  #统计量自由度
    d = (2 * n ^ 2 + 3 * n - 1) * (1 / (n1 - 1) + 1 / (n2 - 1) + 1 / (n3 - 1) - 1 / (N - K)) / (6 * (n + 1) * (K - 1))
    S1 = np.cov(G1.T)
    S2 = np.cov(G2.T)
    S3 = np.cov(G3.T)
    S = ((n1 - 1) * S1 + (n2 - 1) * S2 + (n3 - 1) * S3) / (N - K)
    Z = (N - K) * math.log(np.linalg.det(S)) - ((n1 - 1) * math.log(np.linalg.det(S1)) + (n2 - 1) * math.log(np.linalg.det(S2)) + (n3 - 1) * math.log(np.linalg.det(S3)))
    T = (1 - d) * Z
    a = 0.05
    C = chi2.ppf(1 - a, f)
    if T < C:
        print('三类样本协方差矩阵相等')
    else:
        print('三类样本协方差矩阵不全相等')

    # 以上部分代码判断各类样本的协方差矩阵是否相等，下部分将进行判别

    pw1 = n1 / n
    pw2 = n2 / n
    pw3 = n3 / n  #先验概率
    m1 = np.mean(G1,0).T
    m2 = np.mean(G2,0).T
    m3 = np.mean(G3,0).T
    g1 = m1.T * np.linalg.inv(S) * test - 1 / 2 * m1.T * np.linalg.inv(S) * m1 + math.log(pw1)
    g2 = m2.T * np.linalg.inv(S) * test - 1 / 2 * m2.T * np.linalg.inv(S) * m2 + math.log(pw2)
    g3 = m3.T * np.linalg.inv(S) * test - 1 / 2 * m3.T * np.linalg.inv(S) * m3 + math.log(pw3)
    compare_list = [g1,g2,g3]
    if(g1 == max(compare_list)):
        print('样本属于第一类')
    if (g2 == max(compare_list)):
        print('样本属于第二类')
    if (g3 == max(compare_list)):
        print('样本属于第三类')


if __name__ == '__main__':
    sample =[[261.01 ,7.36],
              [185.39 ,5.99],
              [249.58 ,6.11],
              [137.13 ,4.35],
              [231.34 ,8.79],
              [231.38 ,8.53],
              [260.25 ,10.02],
              [259.51 ,9.79],
              [273.84 ,8.79],
              [303.59 ,8.53],
              [231.03 ,6.15],
              [308.90 ,8.49],
              [258.69 ,7.16],
              [355.54 ,9.43],
              [476.69 ,11.32],
              [316.12 ,8.17],
              [274.57 ,9.67],
              [409.42 ,10.49],
              [330.34 ,9.61],
              [331.47 ,13.72],
              [352.50 ,11.00],
              [347.31 ,11.19],
              [189.59 ,5.46]]
    test = np.mat([380.20,9.08]).T
    Bayes_classify(sample,test)