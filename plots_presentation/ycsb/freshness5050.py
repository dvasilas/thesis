import matplotlib.pyplot as plt

local_t = [2925.375758,5639.334017,10494.88244,17530.22349,23766.01713,26713.6674,28902.8739,36977.99875]
local_rt = [76.77633333,57.918,42.53466667,27.35,21.55366667,20.94133333,18.323,17.15966667]

remote_corpus_t = [71.18237674,150.4944067,284.7447477,579.4492848,1160.582849,2318.671723,4658.982036,9269.978294,17741.18322,26958.55155]
remote_corpus_rt = [90.95966667,84.974,79.758,72.23933333,65.701,62.08733333,48.40033333,35.71166667,23.28766667,18.627]

remote_client_t = [83.85581895,184.0417301,368.3567044,774.8864827,1511.152695,2985.928846,5760.56584,10588.54349,16654.83895,23180.76405,]
remote_client_rt = [92.05233333,80.67266667,80.84333333,70.45733333,65.49566667,57.31133333,44.91166667,31.61233333,22.49433333,17.07166667]
# cache_t = [104.9045301,216.2114933,454.9583271,1010.329599,2121.828298,4094.483671,7138.506999,6980.213014]
# cache_rt = [100,100,98.667,96.864,93.555,88.717,81.592,81.165]


f, ax = plt.subplots()

# ax.plot(local_t, local_rt, color='steelblue', marker='+', label='local w95/5')
ax.plot(local_t, local_rt, color='c', marker='o', label='rg-index w50/50')
ax.plot(remote_corpus_t, remote_corpus_rt, color='b', marker='x', label='p-index w50/50')
ax.plot(remote_client_t, remote_client_rt, color='g', marker='+', label='p-index-cache w50/50')
# ax.plot(remote_corpus_t, remote_corpus_rt, color='forestgreen', marker='x', label='remote-corpus w95/5')
# ax.plot(remote_client_t, remote_client_rt, color='slateblue', linestyle='dotted', marker='o', label='remote-client w95/5')
# ax.plot(cache_t, cache_rt, color='peru', linestyle='dotted', marker='s', label='remote-client-cache w95/5')


ax.set(xlabel='Throughput [operations/s]', ylabel='Queries that returned the most recent version [%]')

ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 105.0])

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='lower left')

plt.savefig('freshness_throughput_5050.png')
plt.close()