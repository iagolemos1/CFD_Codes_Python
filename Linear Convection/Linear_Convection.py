import numpy                      		  #here we load numpy
from matplotlib import pyplot as plt      #here we load matplotlib


endtime = float(input('Input the end time of the simulation: '))
dx = float(input('Input the length of a cell: '))
xmax = float(input('Input the domain size in the x direction: ')) #length max of the domain
c = float(input('Input the velocity of the wave: '))
C = float(input('Input the Courant-Friedrich-Lewy Value: '))
dt = C*dx / c
nx = int(xmax/dx + 1)
nt = int(endtime/dt) #nt is the number of timesteps we want to calculate


#Setting boundy conditions
u = numpy.zeros(nx) #numpy function ones()


#setting initial conditions
u1 = float(input('Set the initial condition velocity of the squared wave: '))
print('Set the position where of the inital velocity: ')
u[0:10]= u1  

plt.figure(1)
plt.title('Initial conditions')
plt.plot(numpy.linspace(0, xmax, nx), u)


un = numpy.zeros(nx) #initialize a temporary array
for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() #copy the existing values of u into un
    for i in range(1, nx):
            u[i] = un[i] - (c * (dt / dx) * (un[i] - un[i-1])) 
fig=plt.figure(2)            
plt.plot(numpy.linspace(0, xmax, nx), u)


plt.xlabel('x [m]')
plt.ylabel('u [m/s]')
plt.show()
print(u)
