#/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import time
import math

#读取数据存入[50][384][384]的三维数组
f = open('/home/zhouhuibo/FM2_160222_03.ascii', 'r')
data = f.readlines()   
assert len(data) == 385 * 50 + 1   
data = data[1:]
all_array = []
for i in range(50):
    temp = data[i*385+1 : (i+1)*385]
    pixel_array = []
    for j in range(384):
        array = [int(kk, base=16) for kk in temp[j].split()]
        assert len(array) == 384
        pixel_array.append(array)
    pixel_array = np.array(pixel_array)       
    all_array.append(pixel_array)
all_array = np.array(all_array)

#取数组l的中位数
def nlogn_median(l):
    l=sorted(l);
    if len(l)%2==1:
        return l[math.floor(len(l)/2)];
    else:
        return l[math.floor(len(l)/2)-1];

#将数组l按照chunk_size进行分割
def chunked(l,chunk_size):
    return [l[i:i+chunk_size] for i in range(0,len(l),chunk_size)];    


#nlogn trivial select
def trivialSelect(l,k):
     l=sorted(l);
     return l[k];

#O(n) k-select                      
def select(l,k,Q):
    if len(l)<Q:
        return trivialSelect(l,k);  

    chunks=chunked(l,Q);  
    full_chunks=[chunk for chunk in chunks if len(chunk)==Q];    
    sorted_groups=[sorted(chunk) for chunk in full_chunks];     
    if Q%2==1:
        medians=[chunk[math.floor(Q/2)] for chunk in sorted_groups];       
    else:
        medians=[chunk[math.floor(Q/2)-1] for chunk in sorted_groups];   

    if len(medians)%2==1:
        rM=math.floor(len(medians)/2);
    else:
        rM=math.floor(len(medians)/2)-1;                     #取medians所在位置

    median_of_medians=select(medians,rM,Q); #recursive call  #rM 位置
    return median_of_medians;

def median(l,Q):
    if len(l)%2==1:
        rM=math.floor(len(l)/2);
    else:
        rM=math.floor(len(l)/2)-1;
    return select(l,rM,Q);

all_medians=[];
all_M_medians=[];
all_rM=[];
all_order=[];
Q=5;

for i in range(50):
    for j in range(384):
        line=all_array[i][j];
        for k in range(3):
            A=line[128*k:128*(k+1)];
            med=median(A,Q);
            B=sorted(A);

            chunks=chunked(A,Q);
            full_chunks=[chunk for chunk in chunks if len(chunk)==Q];
            sorted_groups=[sorted(chunk) for chunk in full_chunks];
            if Q%2==1:
               meds=[chunk[math.floor(Q/2)] for chunk in sorted_groups];
            else:
               meds=[chunk[math.floor(Q/2)-1] for chunk in sorted_groups];

            if len(meds)%2==1:
               rM=math.floor(len(meds)/2);
            else:
               rM=math.floor(len(meds)/2)-1;

            medM=select(meds,rM,Q); #median of medians 

            order=B.index(medM);

            all_medians.append(med);
            all_M_medians.append(medM);
            all_order.append(order);


print(np.mean(all_medians));
print(np.mean(all_M_medians));
print(np.mean(all_order));

plt.hist(all_order, bins=50, color='steelblue', normed=True )
plt.show()

            

