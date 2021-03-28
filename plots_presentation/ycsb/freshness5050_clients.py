import matplotlib.pyplot as plt

local_t = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
local_rt = [76.77633333,57.918,42.53466667,27.35,21.55366667,20.94133333,18.323,17.15966667,14.861,11.14233333,11.99966667]

remote_corpus_t = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
remote_corpus_rt = [90.95966667,84.974,79.758,72.23933333,65.701,62.08733333,48.40033333,35.71166667,23.28766667,18.627,19.59966667]

remote_client_t = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
remote_client_rt = [92.05233333,80.67266667,80.84333333,70.45733333,65.49566667,57.31133333,44.91166667,31.61233333,22.49433333,17.07166667,18.621]


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

plt.savefig('freshness_throughput_5050_clients.png')
plt.close()