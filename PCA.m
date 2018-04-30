k1=1;
k2=2; %将样本降到k维参数设置  
X=[0 0 0;                     %样本矩阵  
      1 0 0;   
      1 0 1;   
      1 1 0;  
      0 0 1;   
      0 1 0;  
      0 1 1;  
      1 1 1]  ;
[Row, Col]=size(X);  
covX=cov(X);                                    %求样本的协方差矩阵（散步矩阵除以(n-1)即为协方差矩阵）  
[V, D]=eigs(covX);                               %求协方差矩阵的特征值D和特征向量V  
meanX=mean(X);                                  %样本均值m  
%所有样本X减去样本均值m，再乘以协方差矩阵（散步矩阵）的特征向量V，即为样本的主成份SCORE  
tempX= repmat(meanX,Row,1);  
SCORE=(X-tempX)*V ;  %主成份：SCORE  
pcaData1=SCORE(:,1:k1)  ;%将特征降到1维
pcaData2=SCORE(:,1:k2)  ;%将特征降到2维
disp(pcaData1);
disp(pcaData2);