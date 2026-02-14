import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits as mplot3d

figure=plt.figure(figsize=(10,7))
ax=plt.axes(projection='3d')
ax.grid()
t = np.arange(0, 10*np.pi, np.pi/50)
x = np.sin(t)
y = np.cos(t)

ax.plot3D(x,y,t)
ax.set_title('3D Plotting')
ax.set_xlabel('X axis',labelpad=50)
ax.set_ylabel('Y axis',labelpad=50)
ax.set_zlabel('Z axis',labelpad=50)

x=[1,2,3,4]
y=[4,5,6]

X,Y=np.meshgrid(x,y)
print(X)
print(Y)

fig=plt.figure(figsize=(10,8))
ax=plt.axes(projection='3d')

x=np.arange(-5,5,0.2)
y=np.arange(-5,5,0.2)

X,Y=np.meshgrid(x,y)
Z=np.sin(X)*np.cos(Y)

surf=ax.plot_surface(X,Y,Z,cmap=plt.cm.cividis)
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

fig.colorbar(surf, shrink=0.5, aspect=8)


fig=plt.figure(figsize=(12,6))
ax=fig.add_subplot(1,2,1,projection='3d')
ax.plot_wireframe(X,Y,Z)
ax.set_title('Wireframe')

ax=fig.add_subplot(1,2,2,projection='3d')
ax.plot_surface(X,Y,Z)
ax.set_title('Surface')

plt.tight_layout()

plt.show()