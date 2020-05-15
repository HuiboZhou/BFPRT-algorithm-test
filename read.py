#/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import time

def read():

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
            array = [int(kk, base=16) for kk in temp[j].split()]   #16进制转换
            assert len(array) == 384
            pixel_array.append(array)
        pixel_array = np.array(pixel_array)       
        all_array.append(pixel_array)
    all_array = np.array(all_array)

    #排序去除5组像素两端极值                                                        #排序
    rank_array=np.sort(all_array,axis=0)
    deleted_array=np.delete(rank_array,[0,1,2,3,4,45,46,47,48,49,50],axis=0)        #delete（array，[]，axis=n）对n维度[]列去除的两端极值，可根据需求进行更改[]
    aver_array= np.mean(deleted_array,axis=0)
    np.savetxt('average.txt',aver_array,fmt='%s')
    print(aver_array.shape,all_array[0,:,:].shape)

            #all_array[x,:,:] 第x帧数据赋值给i_array，其他帧可按需求更改x

    #排序查询|frame-offset|取值的范围
   # q=np.sort(i_array,axis=0)
   # print(q)

    #绘制像素分布图                                    
    fig = plt.figure()  
    plt.imshow(aver_array,vmin=0,vmax=1500,aspect='auto',origin='lower') 
    plt.colorbar()  
    plt.xlabel("X/384 pixel")
    plt.ylabel("Y/384 pixel") 
    plt.title('abnormal channel?')
    plt.show()
   
    #绘制像素子图
    fig,axes=plt.subplots(2,3,figsize=(19,10),facecolor='#ccddef') 
    fig.suptitle('abnormal pixel',fontsize=20) 
    bad_pixel1=all_array[:,130,154]
    axes[0,0].plot(bad_pixel1)
    axes[0,0].title.set_text('pixel [130][154]')
    bad_pixel2=all_array[:,131,155]
    axes[0,1].plot(bad_pixel2)
    axes[0,1].title.set_text('pixel [131][155]')
    bad_pixel3=all_array[:,133,156]
    axes[0,2].plot(bad_pixel3)
    axes[0,2].title.set_text('pixel [133][156]')
    bad_pixel4=all_array[:,131,160]
    axes[1,0].plot(bad_pixel4)
    axes[1,0].title.set_text('pixel [131][160]')
    bad_pixel5=all_array[:,133,160]
    axes[1,1].plot(bad_pixel5)
    axes[1,1].title.set_text('pixel [133][160]')
    bad_pixel6=all_array[:,129,161]
    axes[1,2].plot(bad_pixel6)
    axes[1,2].title.set_text('pixel [129][161]')
    plt.show()
    #这部分比较冗余，可更改为循环结构输出子图

    return aver_array
 

if __name__ == '__main__':
    a = read()
    print(a)
    
   
