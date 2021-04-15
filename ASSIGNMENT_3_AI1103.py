import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-8,10,10000)#displaying the graph between -8 and 10
p=1/6
def f(x): return (p-p**2)*x**2-2*p*x+6*p
plt.plot(x, f(x))
plt.title('Variance $V(X)$ for $p=1/6$')
plt.xlabel('k')
plt.ylabel('$V(X)$ or $f(k)$')