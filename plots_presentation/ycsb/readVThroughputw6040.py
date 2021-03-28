import matplotlib.pyplot as plt

local_t = [1029.236769,2017.249493,3875.802779,6711.786279,9196.313633,10424.94729,11724.17624,13794.56891]
local_rt = [99.859,99.73133333,99.43766667,98.9,98.23466667,97.76033333,97.126,75.81466667]
remote_corpus_t = [22.43181875,47.1349353,97.42821473,198.8768252,390.1447106,777.1512687,1551.906568,3107.035928,6056.988872]
remote_corpus_rt = [99.975,99.94133333,99.86766667,99.72866667,99.51533333,99.33433333,99.08133333,98.55366667,93.91933333]
remote_client_t = [48.34402376,404.2425755,858.1339056,1890.324834,3718.571393,6533.020633,9711.960721]
remote_client_rt = [99.94133333,92.69566667,84.88866667,73.21066667,58.257,47.72666667,42.395]
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

plt.savefig('ycsb_readV_freshness_throughput_6040.png')
plt.close()