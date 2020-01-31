import numpy as np
import matplotlib.pyplot as plt

L=np.pi # value chosen for the critical length
s=101 # number of steps in x
t=10002 # number of timesteps
ds=L/(s-1) # step in x
dt=0.0001 # time step
D=1 # diffusion constant, set equal to 1
C=1 # creation rate of neutrons, set equal to 1
Alpha=(D*dt)/(ds*ds) # constant for diffusion term
Beta=C*dt # constant for u term

x = np.linspace(-L/2, 0, num=51)
x = np.concatenate([x, np.linspace(x[-1] - x[-2], L/2, num=50)]) # setting x in the specified interval

u=np.zeros(shape=(s,t)) #setting the function u
u[50,0]=1/ds # delta function
for k in range(0,t-1):
    u[0,k]=0 # boundary conditions
    u[s-1,k]=0
    for i in range(1,s-1):
        u[i,k+1]=(1+Beta-2*Alpha)*u[i,k]+Alpha*u[i+1,k]+Alpha*u[i-1,k] # numerical solution  
    if k == 50 or k == 100 or k == 250 or k == 500 or k == 1000 or k == 10000: # plotting at times
        plt.plot(x,u[:,k])

plt.title('Numerical Solution of the Diffusion equation over time')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.show()