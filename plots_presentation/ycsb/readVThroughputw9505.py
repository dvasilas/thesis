import matplotlib.pyplot as plt

local_t = [797.4875,1607.489671,3213.759974,5944.054721,8776.6797,10147.07373,11260.70687,12231.66404,14671.48226]
local_rt = [99.99266667,99.976,99.96133333,99.91966667,99.88466667,99.86666667,99.841,99.81033333,99.75233333]
remote_corpus_t = [12.72550341,25.57250955,51.5782907,102.7580182,204.9206944,414.0796566,822.2349742,1646.423044,3283.269298,6376.004191,6351.015437]
remote_corpus_rt = [100,99.99466667,99.99066667,99.98233333,99.974,99.97,99.95966667,99.94833333,99.91966667,99.88033333,99.88166667]
remote_client_t = [104.9045301,216.2114933,454.9583271,1010.329599,2121.828298,4094.483671,7138.506999]
remote_client_rt = [99.98233333,99.974,99.08133333,97.873,95.65833333,92.41633333,87.647]
# cache_t = [104.9045301,216.2114933,454.9583271,1010.329599,2121.828298,4094.483671,7138.506999,6980.213014]
# cache_rt = [100,100,98.667,96.864,93.555,88.717,81.592,81.165]


f, ax = plt.subplots()

# ax.plot(local_t, local_rt, color='steelblue', marker='+', label='local w95/5')
ax.plot(local_t, local_rt, color='c', marker='o', label='rg-index')
ax.plot(remote_corpus_t, remote_corpus_rt, color='b', marker='x', label='p-index')
ax.plot(remote_client_t, remote_client_rt, color='g', marker='+', label='p-index-cache')
# ax.plot(remote_corpus_t, remote_corpus_rt, color='forestgreen', marker='x', label='remote-corpus w95/5')
# ax.plot(remote_client_t, remote_client_rt, color='slateblue', linestyle='dotted', marker='o', label='remote-client w95/5')
# ax.plot(cache_t, cache_rt, color='peru', linestyle='dotted', marker='s', label='remote-client-cache w95/5')


# ax.set(xlabel='Throughput [operations/s]', ylabel='Queries that returned the most recent version [%]')

ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 105.0])

# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles,labels=labels, loc='lower left')

plt.savefig('ycsb_readV_freshness_throughput_9505.png')
plt.close()