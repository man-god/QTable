import numpy as np
import types

A=np.array([1,1])
B=(1,2)

print(type(A).mro())
print(isinstance(A,list))
print(type(B).mro())
print(isinstance(B,tuple))

if not isinstance(A,tuple):
	print("hhh")


print(np.array([(1,2),(1,3)]).ravel())
#flatten

print(np.finfo(np.float32).max)

"""
x, x_dot, theta, theta_dot = state
        force = self.force_mag if action==1 else -self.force_mag
        costheta = math.cos(theta)
        sintheta = math.sin(theta)
        temp = (force + self.polemass_length * theta_dot * theta_dot * sintheta) / self.total_mass
        thetaacc = (self.gravity * sintheta - costheta* temp) / (self.length * (4.0/3.0 - self.masspole * costheta * costheta / self.total_mass))
        xacc  = temp - self.polemass_length * thetaacc * costheta / self.total_mass
        x  = x + self.tau * x_dot
        x_dot = x_dot + self.tau * xacc
        theta = theta + self.tau * theta_dot
        theta_dot = theta_dot + self.tau * thetaacc
        self.state = (x,x_dot,theta,theta_dot)
"""






























