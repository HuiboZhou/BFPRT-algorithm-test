#/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import random

#all_array = np.array(np.random.rand(500,384,384))                   #小数
all_array=np.random.randint(0,5000,size=[1,384,384])                 #整数




def nlogn_median(l):
    l=sorted(l);
    if len(l)%2==1:
        return l[math.floor(len(l)/2)];
    else:
        return l[math.floor(len(l)/2)-1];

#将数组l按照chunk_size进行分割
def chunked(l,chunk_size):
    return [l[i:i+chunk_size] for i in range(0,len(l),chunk_size)];    


#trivial select  
def trivialSelect(meds):
     meds.append(last);
     meds=sorted(meds);
     return meds[1];
#没毛病

                      
def select(l,Q):

    if len(l)<4:
       return  trivialSelect(l);
  
   
    chunks=chunked(l,Q);  
    full_chunks=[chunk for chunk in chunks if len(chunk)==Q];    
    sorted_groups=[sorted(chunk) for chunk in full_chunks];     
    if Q%2==1:
        medians=[chunk[math.floor(Q/2)] for chunk in sorted_groups];       
    else:
        medians=[chunk[math.floor(Q/2)-1] for chunk in sorted_groups];   #Nmedians=21/3=7

    if len(medians)%2==1:
        rM=math.floor(len(medians)/2);
    else:
        rM=math.floor(len(medians)/2)-1;                     #取medians所在位置
    if len(medians)==7:
       global last;
       last=medians[6];
       medians.pop();           #Nmedians=6

    median_of_medians=select(medians,Q); #recursive call Nmedians=2
    return median_of_medians;


def median(l):
    if len(l)%2==1:
        rM=math.floor(len(l)/2);
    else:
        rM=math.floor(len(l)/2)-1;
    return rM;

all_medians=[];
all_M_medians=[];
all_rM=[];
all_order=[];
Q=4;

for i in range(1):
    for j in range(384):
        line=all_array[i][j];
        for k in range(6):
            A=line[64*k:64*(k+1)];

            
            B=sorted(A);
            med=median(B);   #64个pixel值中取median

            chunks=chunked(A,Q);   #64/4=16
            full_chunks=[chunk for chunk in chunks if len(chunk)==Q];
            sorted_groups=[sorted(chunk) for chunk in full_chunks];

            if Q%2==1:
               meds=[chunk[math.floor(Q/2)] for chunk in sorted_groups];
            else:
               meds=[chunk[math.floor(Q/2)-1] for chunk in sorted_groups]; #Nmeds=16
 


            medM=select(meds,Q);       
            
            order=B.index(medM);

            all_medians.append(med);
            all_M_medians.append(medM);
            all_order.append(order);


print(np.mean(all_medians));
print(np.mean(all_M_medians));
print(np.mean(all_order));



plt.hist(all_order, bins=50, color='steelblue', normed=True )
plt.show()

            

