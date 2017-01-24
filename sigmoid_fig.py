# coding:utf-8
# Python 绘图

# sigmoid 函数
import numpy as np
import matplotlib
matplotlib.use('Agg')   # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt

X = np.linspace(-6, 6, 200)
Y = 1 / (1 + np.exp(-X))

fig = plt.figure()
plt.plot(X, Y, color = "blue", linewidth = 2.5, linestyle = "-")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# plt.xlim(X.min()*1.1, X.max()*1.1)
# plt.ylim(Y.min()*1.1,Y.max()*1.1)
plt.grid(True)
plt.xlabel("$z$")
plt.yticks([0.5, 1], [r'$0.5$', r'$1$'])
plt.text(-4, 0.7, r'$\sigma(z)=\frac{1}{1+e^{-z}}$', fontsize = 24)

plt.show()

fig.savefig("sigmoid_fig.pdf")
fig.savefig("sigmoid_fig.png")


