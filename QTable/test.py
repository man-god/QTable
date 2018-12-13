import math
#import gym
from maze_env import Maze
import numpy as np
import QTableTest as QT

class test:
	QTable=None
	env=None
	#if __name__=='__main__'(self):
	def __init__(self):
		return

	#@classmethod
	def train(self):

		#self.env=gym.make('CartPole-v0')
		self.env=Maze()
		
		EPISODE_NUM=100
		#A_NUM,A_DIM
		#S_NUM,S_DIM

		#theta_threshold_radians = 12 * 2 * math.pi / 360
		#x_threshold = 2.4

		""" #test for CartPole-v0
		x_threshold = self.env.observation_space.high[0] / 2
		theta_threshold_radians = self.env.observation_space.high[2] / 2
		x_range = .1;
		x_division = .01
		theta_range = 1
		theta_division = .05
		"""
		a=.03
		r=1
		#print("x_threshold",x_threshold,theta_threshold_radians)





		#a tuple with one element is not a tuple (e.g. (2) is int;("abc") is string). we should add ","(e.g. (2,),("abc",))

		""" #test for CartPole-v0
		QTable=QT.QTable((int(round(x_range/x_division))*2+1,int(round(theta_range/theta_division))*2+1),(2,))
		"""
		#test for mofan
		QTable=QT.QTable((4,4),(4,))
		
		print(type(QTable))
		print((QTable))
		print(np.shape(QTable.QTable))


		for _episode in np.arange(EPISODE_NUM):
			observation=self.env.reset()
						
			t=0
			while True:
				t+=1
				self.env.render()
				

				""" #test for CartPole-v0
				x=min(max(observation[0], -x_threshold * x_range), x_threshold * x_range)
				theta=min(max(observation[2], -theta_threshold_radians * theta_range), theta_threshold_radians * theta_range)

				x_index=int(round((x/x_threshold-(-x_range))/x_division))
				theta_index=int(round((theta/theta_threshold_radians-(-theta_range))/theta_division))
				"""

				
				#test for mofan
				if(type(observation[0])=='str'):
					break
				x_index=int((observation[0]-5)/40)
				theta_index=int((observation[1]-5)/40)

				
				
				
				S0=[x_index,theta_index]
				A0,Q0=QTable.getMaxQ(tuple(S0))
				#A0=self.env.action_space.sample()
				#print("A0====",A0)
				observation, reward, done, info=self.env.step(A0[0])#A0 may be a list
				#print("observation",observation[0]/x_threshold,observation[2]/theta_threshold_radians)
				#print("Q0",Q0)
				#print("reward3===",reward)
				""" #test for CartPole-v0
				x=min(max(observation[0], -x_threshold * x_range), x_threshold * x_range)
				theta=min(max(observation[2], -theta_threshold_radians * theta_range), theta_threshold_radians * theta_range)

				x_index=int(round((x/x_threshold-(-x_range))/x_division))
				theta_index=int(round((theta/theta_threshold_radians-(-theta_range))/theta_division))
				"""
				
				#test for mofan
				#huidaozhi reward shizhongwei 0!!!
				if(isinstance(observation[0],str)):
					print("Episode finished after %d episode %d timestep",(_episode+1),(t+1))
					break
				x_index=int((observation[0]-5)/40)
				theta_index=int((observation[1]-5)/40)


				
				S1=[x_index,theta_index]
				A1,Q1=QTable.getMaxQ(tuple(S1))



				count=QTable.getCountByIndex(tuple(np.hstack((S0,A0))))
				a=1.0/(count+1)
				#print("r",r)
				#print("reward",reward)
				#print("Q1",Q1)
				Q0=Q0+a*(reward+r*Q1-Q0)
				QTable.setQ(Q0,tuple(S0),tuple(A0))
				#QTable.setCountByIndex(count+1,tuple(np.hstack((S0,A0))))

				#print("observation1",x, theta)
				#print("observation2",round((x/x_threshold-(-.1))/.01),round((theta/theta_threshold_radians-(-1))/.1))		


				#print("theta_threshold_radians",theta_threshold_radians)
				

				if done:
					print("Episode finished after %d episode %d timestep",(_episode+1),(t+1))
					#print("observation2",int(round((x/x_threshold-(-x_range))/x_division)), \
					#					int(round((theta/theta_threshold_radians-(-theta_range))/theta_division)))
					break

		self.QTable=QTable


	def test(self):
		#x_threshold = self.env.observation_space.high[0] / 2
		#theta_threshold_radians = self.env.observation_space.high[2] / 2
		x_range = .1
		x_division = .01
		theta_range = 1
		theta_division = .1
		a=.03
		r=1
		observation=self.env.reset()
		t=0
		while True:
			t+=1
			self.env.render()
			

			""" #test for CartPole-v0
			x=min(max(observation[0], -x_threshold * x_range), x_threshold * x_range)
			theta=min(max(observation[2], -theta_threshold_radians * theta_range), theta_threshold_radians * theta_range)

			x_index=int(round((x/x_threshold-(-x_range))/x_division))
			theta_index=int(round((theta/theta_threshold_radians-(-theta_range))/theta_division))
			"""

			#test for mofan
			if(type(observation[0])=='str'):
				break
			x_index=int((observation[0]-5)/40)
			theta_index=int((observation[1]-5)/40)



			S0=[x_index,theta_index]
			A0,Q0=self.QTable.getMaxQ(tuple(S0))
			#A0=self.env.action_space.sample()
			#print("A0====",A0)
			observation, reward, done, info=self.env.step(A0[0])#A0 may be a list
			#print("observation",observation[0]/x_threshold,observation[2]/theta_threshold_radians)




			""" #test for CartPole-v0
			x=min(max(observation[0], -x_threshold * x_range), x_threshold * x_range)
			theta=min(max(observation[2], -theta_threshold_radians * theta_range), theta_threshold_radians * theta_range)

			x_index=int(round((x/x_threshold-(-x_range))/x_division))
			theta_index=int(round((theta/theta_threshold_radians-(-theta_range))/theta_division))
			"""

			#test for mofan
			if(type(observation[0])=='str'):
				break
			x_index=int((observation[0]-5)/40)
			theta_index=int((observation[1]-5)/40)



			S1=[x_index,theta_index]
			A1,Q1=self.QTable.getMaxQ(tuple(S1))

			count=self.QTable.getCountByIndex(tuple(np.hstack((S0,A0))))
			a=1.0/(count+1)
			Q0=Q0+a*(reward+r*Q1-Q0)
			self.QTable.setQ(Q0,tuple(S0),tuple(A0))







			if done:
				print("Episode finished after {} timestep".format(t+1))
				#print("observation2",int(round((x/x_threshold-(-x_range))/x_division)), \
				#					int(round((theta/theta_threshold_radians-(-theta_range))/theta_division)))
				break














