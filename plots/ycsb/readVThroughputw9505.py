import matplotlib.pyplot as plt

local_t = [797.525,1611.319434,3225.45,5961.53077,8783.247906,10157.7895,11266.70832,12151.38566,15027.63411,16069.14283,15890.65809]
local_rt = [100,99.984,99.972,99.947,99.922,99.91,99.891,99.865,99.815,99.757,99.763]
remote_corpus_t = [797.45,1603.659909,3202.069948,5926.578671,8770.111494,10136.35796,11254.70543,12311.94242,14315.3304,15825.63104,15805.75145]
remote_corpus_rt = [99.989,99.972,99.956,99.906,99.866,99.845,99.816,99.783,99.721,99.676,99.656]
remote_client_t = [12.72550341,25.57250955,51.5782907,102.7580182,204.9206944,414.0796566,822.2349742,1646.423044,3283.269298,6376.004191,6351.015437]
remote_client_rt = [100,100,100,100,100,100,99.994,99.99,99.972,99.942,99.941]
cache_t = [104.9045301,216.2114933,454.9583271,1010.329599,2121.828298,4094.483671,7138.506999,6980.213014]
cache_rt = [100,100,98.667,96.864,93.555,88.717,81.592,81.165]


f, ax = plt.subplots()

ax.plot(local_t, local_rt, color='steelblue', marker='+', label='local w95/5')
ax.plot(remote_corpus_t, remote_corpus_rt, color='forestgreen', marker='x', label='remote-corpus w95/5')
ax.plot(remote_client_t, remote_client_rt, color='slateblue', linestyle='dotted', marker='o', label='remote-client w95/5')
ax.plot(cache_t, cache_rt, color='peru', linestyle='dotted', marker='s', label='remote-client-cache w95/5')


ax.set(xlabel='Throughput [operations/s]', ylabel='Queries that returned the most recent version [%]')

ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 100.0])

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='lower left')

plt.savefig('ycsb_readV_freshness_throughput_9505.png')
plt.close()