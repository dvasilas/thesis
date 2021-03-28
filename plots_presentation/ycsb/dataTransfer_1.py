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

ax.bar(r1, bars1, color='c', width=barWidth, edgecolor='white', label='replicated global index')
ax.bar(r2, bars2, color='b', width=barWidth, edgecolor='white', label='partitioned index')
ax.bar(r3, bars3, color='g', width=barWidth, edgecolor='white', label='partitioned index w/ caching')
# ax.bar(r3, bars3, color='y', width=barWidth, edgecolor='white', label='distributed-index-cache')
ax.grid(linestyle='dotted')
# plt.xlabel('Workload type')
# plt.ylabel('Data transfer cost (* $ price per GB)')
plt.xticks([])

handles, labels = ax.get_legend_handles_labels()
fig.legend(handles,labels=labels, loc='lower center', ncol=3, frameon=False)

# fig.tight_layout(rect=[0,0.05,1,1])
plt.savefig('datatransfer_2.png')
plt.close()
