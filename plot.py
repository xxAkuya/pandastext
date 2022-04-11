"""
画出散点图
"""
import matplotlib.pyplot as plt

from getdata import *

#       ----画图-----
list = [i for i in range(143)]  # x轴seq

#           1
plt.plot(list, [0.7] * 143, label='目标一')
plt.plot(list, [0.571] * 143, label='目标一')
plt.scatter(list, df.iloc[5:148, 4], c='red', label='目标一')
plt.xlabel("student num", fontdict={'size': 16})
plt.ylabel("access", fontdict={'size': 16})
plt.title("goal1", fontdict={'size': 20})
plt.show()

#           2
plt.plot(list, [0.7] * 143, label='目标二')
plt.plot(list, [0.591] * 143, label='目标二')
plt.scatter(list, df.iloc[5:148, 9], c='blue', label='目标二')
plt.xlabel("student num", fontdict={'size': 16})
plt.ylabel("access", fontdict={'size': 16})
plt.title("goal2", fontdict={'size': 20})
plt.show()

#           3
plt.plot(list, [0.7] * 143, label='目标三')
plt.plot(list, [0.554] * 143, label='目标三')
plt.scatter(list, df.iloc[5:148, 14], c='yellow', label='目标三')
plt.xlabel("student num", fontdict={'size': 16})
plt.ylabel("access", fontdict={'size': 16})
plt.title("goal3", fontdict={'size': 20})
plt.show()

#           4
plt.plot(list, [0.7] * 143, label='目标四')
plt.plot(list, [0.710] * 143, label='目标四')
plt.scatter(list, df.iloc[5:148, 21], c='green', label='目标四')
plt.xlabel("student num", fontdict={'size': 16})
plt.ylabel("access", fontdict={'size': 16})
plt.title("goal4", fontdict={'size': 20})
plt.show()
