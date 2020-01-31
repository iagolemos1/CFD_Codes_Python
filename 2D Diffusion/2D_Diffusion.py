#2D Diffusion Equation Solver
#hypothesis: No external forces acting on the flow (dp and g equal to 0), uncompressible flow.
#Dirichlet boundary condition 
#Importing libraries
import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D ##library for 3d projection plots


#Defining the domain, simulation time, and fluid propertie
domain = open('domain.txt','r')
dom = []
for line in domain:
    dom.append(line.split())
L = float(dom[0][2]); W = float(dom[1][2]); nx = int(dom[2][2]); ny = int(dom[3][2]); 
ts = float(dom[4][2]); v = float(dom[5][2]); z = float(dom[6][2]); xmin = float(dom[7][2])
xmax = float(dom[8][2]); ymin = float(dom[9][2]); ymax = float(dom[10][2])

dx = float(L/(nx + 1))
dy = float(W/(ny + 1)) 
x = numpy.linspace(0, L, nx)
y = numpy.linspace(0, W, ny)

#Defining the time step using the condition of convergence and the number of timesteps
dt = 0.25 * dx * dy / v

#Initializing matrixes and initial conditions
u = numpy.zeros((nx, ny)) 
un = numpy.zeros((nx, ny))
u[int(xmin/dx):int((xmax)/dx + 1),int((ymin)/dy):int((ymax)/dy + 1)] = z

# ---- Plotting intial condition ----
fig1 = pyplot.figure()
ax = fig1.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u, rstride=1, cstride=1, cmap=cm.viridis,
        linewidth=0, antialiased=True)
pyplot.title('Initial Conditions')

def diffuse(ts):
    nt = int(ts/dt)
    print(nt)
    for n in range(nt+1):
        un = u.copy()
        u[0,:] = u[1,:]   
        u[-1,:] = u[-2,:] 
        u[:,0] = u[:,1]  
        u[:,-1] = u[:,-2]
        u[1:-1,1:-1] = un[1:-1,1:-1] + ((dt*v)/(dx**2))*((un[2:,1:-1]) - 2*un[1:-1,1:-1] + un[0:-2,1:-1]) + ((dt*v)/(dy**2))*(un[1:-1,2:] - 2*un[1:-1,1:-1] + un[1:-1,0:-2]) 
        
    fig2 = pyplot.figure()
    ax = fig2.gca(projection='3d')
    surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=cm.viridis,
        linewidth=0, antialiased=True)
    ax.set_zlim(0, z)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    pyplot.colorbar(surf)
    pyplot.show()

diffuse(2)
