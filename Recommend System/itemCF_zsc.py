#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
import numpy as np
import math
import os
import time

def mkdir(path):
    # 引入模块
    
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 / 符号
    path=path.rstrip("/")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.system('chmod')
        os.makedirs("%s"%path) 
 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False
 


def String2num(String):
	return eval(String)
print("start")
start=time.time()
testUser=[]


with open('/home/zsc/recommend/big.in', 'r') as f1:#sample.txt
	list1 = f1.readlines()


array=np.zeros((len(list1)-1,3))
#print(array.shape()) 




for i in range(0, len(list1)):
	list1[i] = list1[i].rstrip('\r').rstrip('\n').rstrip(' ').split(' ')
	temp=np.array(list(map(String2num,list1[i])))
	if(i==0):
		first=temp
	elif(len(list1[i])==1):
		array=np.delete(array,array.shape[0]-1,axis=0)
		testUser.append(temp[0])
		pass
	else:
		array[i-1]=temp
	
#print(first)

#print(np.floor(array))
#index=array[:,0:2].T
#index=index.astype(np.int)
#print(tuple(index))
#index.dtype='int'


mm=np.zeros((first[0]+1,first[1]+1))-1

for i in range(0, len(array)):
	index=array[i,0:2]
	index=index.astype(np.int).T
	mm[tuple(index)]=array[i,2]

#print(mm)


similar=np.eye(first[1]+1)
#print(similar)


for i in range(1,first[1]+1):
	for j in range(i+1,first[1]+1):
		flag=mm[:,[i,j]]+1>=math.e-2
		#print(flag)
		#print(flag.all(axis=1))

		ji=(mm[:,i]-mm[:,j])*(mm[:,i]-mm[:,j])

		#print(ji[flag.all(axis=1)].sum())
		#and mm[:,5]+1>=math.e-2
		#print(1/(ji[flag.all(axis=1)].sum()+1))
		similar[i,j]=1/(ji[flag.all(axis=1)].sum()+1)
		similar[j,i]=1/(ji[flag.all(axis=1)].sum()+1)

#print(similar)
#print(testUser)

# 定义要创建的目录
mkpath="/home/zsc/recommend/003"
# 调用函数
mkdir(mkpath)
#os.mknod("/home/zsc/recommend/003/big.out")
p=open("/home/zsc/recommend/003/big.out","w")

for user in testUser:
	
	p.write("Recommendations for user %d:\n"%(user))
	#print("Recommendations for user %d:"%(user))

	userRecommend=np.zeros((first[1]))
	for item in range(1,first[1]+1):
		flag=mm[user,:]+1>=math.e-2
		if(mm[user,item]+1>=math.e-2):
			userRecommend[item-1]=-1
		elif((similar[item,:])[flag].sum()!=0):
			userRecommend[item-1]=(similar[item,:]*mm[user,:])[flag].sum()/(similar[item,:])[flag].sum()
		else:
			userRecommend[item-1]=-1
	#print(flag)
	i=0
	for index in np.argsort(-userRecommend):
		i=i+1
		if(userRecommend[index]>0 and i<=10):
			p.write("%d %.3f\n"%(index+1,userRecommend[index]))
			#print("%d %.3f"%(index+1,userRecommend[index]))
			#print(i)
	

	p.write("\n")
	#print()
#print(userRecommend)
#print(np.argsort(-userRecommend))
#print(userRecommend[np.argsort(-userRecommend)])

p.close()

end=time.time()
print(end-start)
print("end")
