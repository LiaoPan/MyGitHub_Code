# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
#coding:utf-8
import numpy
import string 
from numpy import *
f=open("/dev/stdin",'r')
j=f.readline()
N=int(j[2])
F=int(j[0])
a=[]
for i in range(N):
	b=f.readline()
	c=b.split()
	for item in c:
		d=string.atof(item)
		a.append(d)

#a��һ����������
#����������б�Ϊ����Ȼ���Ϊ����

in_array=numpy.array(a).reshape(N,F+1)

#��ʼ����ͨ��С���˷��������
X=in_array[:,:F]
Y=in_array[:,F]
x=mat(X)
y=mat(Y)
parameter=(x.T*x).I*x.T*(y.T)
	

#====================================================
#��ȡ������ֵ
a1=[]
m=f.readline()

T=int(m)		
for i in range(N,N+T):
	b1=f.readline()
	c1=b1.split()
	for item in c1:
		d1=string.atof(item)
		a1.append(d1)

o_array=numpy.array(a1).reshape(T,F)

house_price=mat(o_array)*parameter
for i in range(T):
    print house_price[i,0]
        