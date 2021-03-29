# libraries
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25

bars1 = [189.1671494, 1897.656173]
bars2 = [37224.90692, 18570.32776]
bars3 = [2375.964763, 9291.396153]

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

fig, ax = plt.subplots()

ax.bar(r1, bars1, color='c', width=barWidth, edgecolor='white', label='rg-index')
ax.bar(r2, bars2, color='b', width=barWidth, edgecolor='white', label='p-index')
ax.bar(r3, bars3, color='g', width=barWidth, edgecolor='white', label='p-index-cache')
# ax.bar(r3, bars3, color='y', width=barWidth, edgecolor='white', label='distributed-index-cache')
ax.grid(linestyle='dotted')
# plt.xlabel('Workload type')
plt.ylabel('Data transfer [GB/month]')
ticks = [0 ,1]
labels = ["w95/5", "w50/50"]
plt.xticks(ticks, labels)


handles, labels = ax.get_legend_handles_labels()
fig.legend(handles,labels=labels, loc='lower center', ncol=3, frameon=False)

# fig.tight_layout(rect=[0,0.05,1,1])
plt.savefig('ycsb_datatransfer.png')
plt.close()
