# libraries
import numpy as np
import matplotlib.pyplot as plt

barWidth = 0.25

bars1 = [404.9609184, 21.23109824]
bars2 = [9.789428711, 32.40392676]

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

fig, ax = plt.subplots()

ax.bar(r1, bars1, color='b', width=barWidth, edgecolor='white', label='central-index')
ax.bar(r2, bars2, color='g', width=barWidth, edgecolor='white', label='distributed-index')
# ax.bar(r3, bars3, color='y', width=barWidth, edgecolor='white', label='distributed-index-cache')
ax.grid(linestyle='dotted')
# plt.xlabel('Workload type')
# plt.ylabel('Data transfer cost (* $ price per GB)')
plt.xticks([])

# handles, labels = ax.get_legend_handles_labels()
# fig.legend(handles,labels=labels, loc='lower center', ncol=3, frameon=False)

# fig.tight_layout(rect=[0,0.05,1,1])
plt.savefig('cost.png')
plt.close()
