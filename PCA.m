k1=1;
k2=2; %����������kά��������  
X=[0 0 0;                     %��������  
      1 0 0;   
      1 0 1;   
      1 1 0;  
      0 0 1;   
      0 1 0;  
      0 1 1;  
      1 1 1]  ;
[Row, Col]=size(X);  
covX=cov(X);                                    %��������Э�������ɢ���������(n-1)��ΪЭ�������  
[V, D]=eigs(covX);                               %��Э������������ֵD����������V  
meanX=mean(X);                                  %������ֵm  
%��������X��ȥ������ֵm���ٳ���Э�������ɢ�����󣩵���������V����Ϊ���������ɷ�SCORE  
tempX= repmat(meanX,Row,1);  
SCORE=(X-tempX)*V ;  %���ɷݣ�SCORE  
pcaData1=SCORE(:,1:k1)  ;%����������1ά
pcaData2=SCORE(:,1:k2)  ;%����������2ά
disp(pcaData1);
disp(pcaData2);