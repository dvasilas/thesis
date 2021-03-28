import matplotlib.pyplot as plt

local_t = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
local_rt = [98.26366667,95.087,91.635,85.76133333,80.29733333,77.34033333,75.44266667,72.23766667,69.30566667,67.52566667,69.61]

remote_corpus_t = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
remote_corpus_rt = [99.36233333,98.56966667,97.273,94.80666667,92.876,91.11566667,89.426,88.27766667,83.70233333,78.60566667,79.046]

remote_client_t = [1, 2, 8, 16, 32, 64, 128, 256, 512, 1024]
remote_client_rt = [100.0,98.56966667,95.024,93.048,91.42366667,89.53,86.94433333,83.007,79.08166667,79.778]
# cache_t = [104.9045301,216.2114933,454.9583271,1010.329599,2121.828298,4094.483671,7138.506999,6980.213014]
# cache_rt = [100,100,98.667,96.864,93.555,88.717,81.592,81.165]


f, ax = plt.subplots()

# ax.plot(local_t, local_rt, color='steelblue', marker='+', label='local w95/5')
ax.plot(local_t, local_rt, color='c', marker='o', label='replicated global index')
ax.plot(remote_corpus_t, remote_corpus_rt, color='b', marker='x', label='partitioned index')
ax.plot(remote_client_t, remote_client_rt, color='g', marker='+', label='partitioned index with cache')
# ax.plot(remote_corpus_t, remote_corpus_rt, color='forestgreen', marker='x', label='remote-corpus w95/5')
# ax.plot(remote_client_t, remote_client_rt, color='slateblue', linestyle='dotted', marker='o', label='remote-client w95/5')
# ax.plot(cache_t, cache_rt, color='peru', linestyle='dotted', marker='s', label='remote-client-cache w95/5')


# ax.set(xlabel='Client threads', ylabel='Queries that returned the most recent version [%]')


ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 105.0])

# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles,labels=labels, loc='lower left')

plt.savefig('freshness_throughput_9505_clients.png')
plt.close()