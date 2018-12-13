import numpy as np

epsilon=.1
num=2



#1.(n) but not n;2.(n) but not (1,n);3.dtype="int" is necessary
S_DIM=2
A_DIM=3
n=S_DIM+A_DIM
arrType=np.ones((n), dtype="int32") * num;print(np.hstack((arrType,S_DIM)))
#print(arrType.ndim)


arr=np.zeros(arrType)
#print(arr.shape)
arr2List=np.arange(num**n)
QTable=arr2List.reshape(arrType)
#print(QTable)

#QTable[1,0,1] is like QTable(1,0,1) in math;QTable[[1,0,1]] is like QTable[1]||QTable[0]||QTable[1]
#print(QTable[1,0,1])



#treat QTable as a one-dimension list returning scaler number not a vector
#a one-dimension list is like scaler number which is one-dimension not a multi-dimension vector
#use logical expression to find the location of the max

#it's best for QTable[1,0] to be the referrence copy of QTable not the value one of QTable
#QTable[1,0]=15

#the expression is not so good if many element are the max
###QTable[1,0][QTable[1,0].argmax()]=100

#the index returned by QTable[1,0]==QTable[1,0].min() is about QTable[1,0] not QTable!!!
###QTable[1,0][QTable[1,0]==QTable[1,0].min()]=-100



#print(QTable)



#the expression is not so good if many elements are the max
#QTable[0].argmax()==3,and QTable[0][QTable[0].argmax()] doesn't work
#QTable[0][QTable[0].argmax()]=200

#the index returned by QTable[1,0]==QTable[1,0].min() is about QTable[1,0] not QTable!!!
###QTable[0][QTable[0]==QTable[0].min()]=-200

#print(QTable)



#print(False*QTable)



#print(np.random.random(np.shape(QTable)));


flag=np.random.random()<epsilon
randAction=np.random.random(np.shape(QTable))

#to pick one
A=flag*randAction+(not flag)*QTable
# ~True=-2 not True is ok

#rand(2,2) is ok but random([2,2]) not, why???
#np.random.random(np.shape(QTable)) is ok but rand(np.shape(QTable)) not, why???
i=0;j=0;k=0;tNum=10000;
for t in range(tNum):
	test=np.random.random([2,2])
	random=np.random.random(np.shape(QTable))
	if random.argmax()==0:
		k=k+1;
	#else print();
	
	if test[1,0]<.2:
		i=i+1;
	if test[1,0]<test[0,1]:
		j=j+1;


#print(i);print(j);
#print(k*1.0/tNum);



r=np.random.randint(0,2,arrType)
#print(r);

rr=np.random.randint(3,6,(5))

#print(rr)
#print(rr%2)


A=np.random.randint(0,num,(A_DIM))
transA2S=np.random.randint(0,num,(A_DIM,S_DIM))

SS=np.dot(A,transA2S)

#print(A)
#print(SS)





aa=np.arange(8).reshape(2,2,2)
aa=np.array([1,1,1,2,2,2,3,3,3]).reshape(3,3)

index=np.array(np.where(aa==aa.min())).T[2]

print(index)
print("testtesttest",aa[index])#tuple where(aa) is different from where(aa==aa)
#print(np.argwhere(aa==aa).reshape(2,2,2,3))#3 wei hebing!!!

#print((np.argwhere(aa==aa)[[1,2]]+1).dot([1,2,1]))# yuanlai bushi yige biaoliang wei zuixiao yunsuan danweile
#yuanyinshi xiangliang yunsuan huifenkuai ,duiyu feixiangliang yunsuan buyiding





#print(tuple(np.argwhere(aa==aa)))




S0=np.random.randint(0,num,(S_DIM));
S0=tuple(S0);#pay attention to the difference between tuple and array!!!
print("\nS0=\n",S0)


index=np.argwhere(QTable==QTable);#print(index);
print("\nQTable=\n",QTable)


transA2S=np.random.randint(0,num,(A_DIM+S_DIM,S_DIM));#print(transA2S);
SS=np.dot(index,transA2S)%num;#print((SS));#print(SS.reshape(2,2,2,S_DIM));
###SS=SS.reshape(2,2,2,S_DIM);#print(QTable[1,0,1]);print(SS[1,0,1]);
SS=SS.reshape(np.hstack((arrType,S_DIM)));#print(QTable[1,0,1]);
#(tuple(arrType),S_DIM) and [arrType,S_DIM] are all not allowed when SS=SS.reshape().You can try to print each for detail
print("\nSS=\n",SS)


reward=np.random.randint(0,num,arrType)
print("\nreward=\n",reward)



print("\nhhh\n",tuple(SS[S0].reshape(-1,S_DIM).T))#QTable[tuple(SS[S0].T)].SS[S0]guanyu A, yaoshi A duowei, shifou xuyao bianwei xianxing zai tuple(SS[S0].T)???yaoshi yao bianxianxing, haidei reshape!!!
#SS[S0].reshape(-1,S_DIM) flatten() reval()










arrTypeA=np.ones((A_DIM), dtype="int32") * num;#print("over",tuple(np.hstack((-1,arrTypeA))))
tupleOut=tuple(np.hstack((-1,arrTypeA)))
tupleIn=tuple(arrTypeA)
axisA=tuple(np.arange(1,A_DIM+1))

print("axisA=",axisA)


print("\nQTable[S0]=\n",QTable[tuple(SS[S0].reshape(-1,S_DIM).T)].reshape(tupleOut))
#print("\nQTable[S0]=\n",QTable[tuple(SS[S0].reshape(-1,S_DIM).T)].reshape(-1,2,2))#2 kinds of index. one is [(),(),()];the other is ([],[])!!! 
#QTable[tuple(SS[S0].T)].SS[S0]guanyu A, yaoshi A duowei, shifou xuyao bianwei xianxing zai tuple(SS[S0].T)???yaoshi yao bianxianxing, haidei reshape!!!


#print("\nQTable[S0]=\n",QTable[tuple(SS[S0].reshape(-1,S_DIM).T)].reshape(tupleOut).max(axis=axisA))
#print("\nQTable[S0]=\n",QTable[tuple(SS[S0].reshape(-1,S_DIM).T)].reshape(-1,2,2).max(axis=(1,2)))
###############!!!!!!!!!reshape(-1,2,2).max(axis=(1,2))) 1.reshape(-1,2,2) zuilimian shi 2,2 yejiushi SS[S0] limiandezhi;2.axis=(1,2) yaodui zuidade jige qiuhe;3.zuihou haiyao reshape()(sihu duoge reshape() keyi huajian, danshi axis=(1,2) yeyao xiangyingde gai);4.shixian cunchu yixie yuanzu yongyu reshape()!!!




print("\nQTable[S0]=\n",QTable[tuple(SS[S0].reshape(-1,S_DIM).T)].reshape(tupleOut).max(axis=axisA).reshape(tupleIn))







print("\nSS[S0]=\n",SS[S0])#zhuyikan print("\nSS[S0]=\n",SS[[S0]])shide baocuo
#kan shenmeyangde bianliang(tuple?) shihedang suoyin
#if S0 is darray, SS[S0] will be like QTable[[1,0,1]]!!!


print("\nreward[S0]=\n",reward[S0])

QTable[tuple(SS[S0].T)].max(axis=1)+reward[S0] #qiu zuida


#QTable[SS[S0],:]



#shejidao np.hstack()de xuyao kaolv xianhoushunxu, ru QTable[SS[S0]]jiu zuiwaiceng guanyu action limian guanyu state




#henduo yibanqingkuangde biaodashi doushi yong guinafa shichulaide, yikaishi buyao jiuxiangzhe cong yibanrushou


	
	
	
	
	
	
	
	






















