import numpy as np


#def __init__(self, S_DIM=1, S_NUM, A_DIM=1, A_NUM):
#	s_arrType
#	a_arrType
class QTable:
	QTable=None
	countTable=None
	epsilon=.1

	#__init__ cannot use customized return value and it is without the expression of "return"(we can take __init__ as return None),only construct an object and return the object;while __new__ can return customized value but not the object itself
	#def __new__(self, s_arrType, a_arrType):
	def __init__(self, s_arrType, a_arrType):
		if not isinstance(s_arrType,tuple):
			np.array(s_arrType)
			tuple()
			print("budui")
		s_arrType=np.array(s_arrType)		
		
		#print("aArray=",np.array(a_arrType).ndim)
		if not isinstance(a_arrType,tuple):
			print("hh",tuple(np.array(a_arrType)))
		a_arrType=np.array(a_arrType)

		
		#if s_arrType=(21,21) a_arrType=(2,) then np.array([s_arrType,a_arrType]).ravel()=[(21,21),(2,)] but not [21,21,2] !!!!!
		#if s_arrType=[21,21] a_arrType=[2] then np.array([s_arrType,a_arrType]).ravel()=[[21,21],[2]] but not [21,21,2] !!!!!
		#arrType=np.array([s_arrType,a_arrType]).ravel()#flatten
		arrType=np.hstack((s_arrType,a_arrType))

		print("arrType=",arrType)
		self.QTable=np.zeros(arrType)
		self.countTable=np.zeros(arrType)
		#print(self.QTable)
		#return self.QTable


	def getMaxQ(self,S):
		
		flag=np.random.random()<self.epsilon
		randAction=np.random.random(np.shape(self.QTable[S]))

		#print("QTable[S]",np.shape(self.QTable[S]))

		#to pick one
		QTable_of_A=flag*randAction+(not flag)*self.QTable[S]
		# ~True=-2 not True is ok

		#print("QTable_of_A",np.shape(QTable_of_A))
		
		A_s=np.array(np.where(QTable_of_A==QTable_of_A.max())).T
		num_of_A_s=np.shape(A_s)[0]
		A=A_s[np.random.randint(num_of_A_s)]
		#print("SA",S,A)
		return A, self.QTable[S][tuple(A)]
		
		
	
	def setQ(self,Q,S,A):
		self.QTable[S][A]=Q
	
	def getCountByIndex(self,index):
		self.countTable[index]+=1
		return self.countTable[index]-1

	#def setCountByIndex(self,count,index):
		#self.countTable[index]=count
	
	
	






















