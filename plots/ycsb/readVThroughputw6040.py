import matplotlib.pyplot as plt

local_t = [975.5262237,1906.702332,3656.425768,6354.482276,8701.563358,9813.4,10372.62842,12701.52799,12795.65314]
local_rt = [99.915,99.852,99.689,99.427,99.087,98.795,98.512,92.496,92.234]
remote_corpus_t = [968.7257819,1899.180041,3681.915904,6403.9899,8688.515574,9708.739563,10305.12583,13068.54599]
remote_corpus_rt = [99.902,99.767,99.519,99.101,98.648,98.299,97.963,77.38]
cache_t = [39.49995009,80.68343617,165.9097714,337.0012726,712.6247505,1576.586242,3955.495684,9270.606726,14067.19014,13740.40233]
cache_rt = [100,100,98.507,93.429,85.877,71.329,45.749,21.418,13.227,13.332]
# rg_index_local_update_h_rt_baseline = [56.81598,59.81113,64.14179,72.76518,83.34325,90.84024,98.65151,104.98136,117.44307,128.42033,129.97407]
remote_client_t = [21.22446939,40.01997254,81.42436492,160.0539003,324.8639744,652.0621772,1301.35243,2593.812375,5117.768853,8668.636692,8538.446245]
remote_client_rt = [100,100,100,100,99.963,99.944,99.938,99.817,99.54,98.857,98.841]

f, ax = plt.subplots()

ax.plot(local_t, local_rt, color='steelblue', linestyle='dotted', marker='+', label='local w60/40')
ax.plot(remote_corpus_t, remote_corpus_rt, color='forestgreen', linestyle='dotted', marker='x', label='remote-corpus w60/40')
ax.plot(remote_client_t, remote_client_rt, color='slateblue', linestyle='dotted', marker='o', label='remote-client w60/40')
ax.plot(cache_t, cache_rt, color='peru', linestyle='dotted', marker='s', label='remote-client-cache w60/40')


ax.set(xlabel='Throughput [operations/s]', ylabel='Queries that returned the most recent version [%]')

ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 100.0])

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='lower left')

plt.savefig('ycsb_readV_freshness_throughput_6040.png')
plt.close()