import numpy as np
import matplotlib.pyplot as plt

x=[0,1,2,3]
y=[0,1,4,9]

#plt.plot(x,y)
#plt.show()

x=np.linspace(-5,5,100)
#plt.plot(x,x**2,'g')
#plt.show()

plt.style.use('seaborn-v0_8-poster')
plt.figure(figsize=(10,6))
x=np.linspace(-5,5,100)
plt.plot(x,x**2,'r',label='Quadratic')
plt.plot(x,x**3,'g',label='Cubic')
plt.title(f"Plot of various polynomials from {x[0]} to {x[-1]}")
plt.xlabel("X-axis",fontsize=18)
plt.ylabel('Y axis', fontsize = 18)
plt.legend(loc = 2)
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.grid()
#plt.show()

x = np.arange(11)
y = x**2

plt.figure(figsize = (14, 8))

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title('Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 3, 2)
plt.scatter(x,y)
plt.title('Scatter')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 3, 3)
plt.bar(x,y)
plt.title('Bar')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.subplot(2, 3, 4)
plt.loglog(x,y)
plt.title('Loglog')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(which='both')

plt.subplot(2, 3, 5)
plt.semilogx(x,y)
plt.title('Semilogx')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(which='both')

# plt.subplot(2, 3, 6)
# plt.semilogy(x,y)
# plt.title('Semilogy')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid()

plt.subplot(2,3,6)
plt.plot(x,x**3)
plt.title('Quadratic')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.tight_layout()

plt.show()