import matplotlib.pyplot as plt

rg_index_local_query_h_t = [797.45,1603.659909,3202.069948,5926.578671,8770.111494,10136.35796,11254.70543,12311.94242,14315.3304,15805.75145]
rg_index_local_query_h_rt = [95.98367,95.26574,96.61137,97.2298,100.25369,102.10765,105.05606,110.06662,119.13074,126.76288]
rg_index_local_query_h_rt_baseline = [55.52397,54.64622,56.05639,56.39275,58.85323,59.5847,60.33704,61.10915,60.92987,62.11517]
rg_index_local_balanced_t = [861.8034549,1715.414229,3359.232038,6050.173746,8414.679266,9461.028897,10299.38025,11484.21842,13693.00722,13563.57905]
rg_index_local_balanced_rt = [97.04723,98.23051,100.01365,103.48157,109.11057,114.0717,122.50229,134.525,149.91608,181.21244]
rg_index_local_balanced_rt_baseline = [56.55185,57.64735,59.3533,62.16915,66.68661,70.18715,75.29984,78.82676,80.65493,84.92193]
rg_index_local_update_h_t = [968.7257819,1899.180041,3681.915904,6403.9899,8688.515574,9708.739563,10305.12583,12814.1394,13142.96063,12924.73306,13068.54599]
rg_index_local_update_h_rt = [97.30362,100.44086,105.121,114.48215,126.44854,136.41485,149.93139,167.21015,234.3254,450.7461,555.75381]
rg_index_local_update_h_rt_baseline = [56.81598,59.81113,64.14179,72.76518,83.34325,90.84024,98.65151,104.98136,117.44307,128.42033,129.97407]

f, ax = plt.subplots()

ax.plot(rg_index_local_query_h_t, rg_index_local_query_h_rt, color='forestgreen', marker='x', label='remote-corpus w95/5')
ax.plot(rg_index_local_query_h_t, rg_index_local_query_h_rt_baseline, color='gray', linestyle='-.', label='notification')
ax.plot(rg_index_local_balanced_t, rg_index_local_balanced_rt, color='forestgreen', marker='x', linestyle='dashed', label='remote-corpus w80/20')
ax.plot(rg_index_local_update_h_t, rg_index_local_update_h_rt, color='forestgreen', marker='x', linestyle='dotted', label='remote-corpus w60/40')

ax.set(xlabel='Throughput [operations/s]', ylabel='95-th %-ile update latency [ms]')

ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 200.0])

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='upper left')

plt.savefig('ycsb_update_latency_remote.png')
plt.close()