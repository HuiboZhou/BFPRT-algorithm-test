
         
#/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import random



all_array=[]
#all_array = np.array(np.random.rand(500,384,384))                   #小数
all_array=np.random.randint(0,4095,size=[10,384,384])                 #整数

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
Q=3;
all_zhongzhi=[];
all_A=[];
last=[];

for i in range(1):
    for j in range(384):
        line=all_array[i][j];
        for k in range(6):
            A=line[64*k:64*(k+1)];

            med=median(A,Q);
            B=sorted(A);
            zhongzhi=B[31];

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
            all_zhongzhi.append(zhongzhi); 
            all_A.append(A);         
            np.savetxt('median_array64.txt',all_zhongzhi,fmt='%d',delimiter='\n')
            np.savetxt('data_10_dec_array64.txt',all_A,fmt='%d',delimiter='\n')  
            np.savetxt('Order_array64.txt',all_order,fmt='%d',delimiter='\n')



plt.xlabel('pivot')
plt.ylabel('persentage')
plt.hist(all_order, bins=50, color='steelblue', normed=True )
plt.show()

            
           

