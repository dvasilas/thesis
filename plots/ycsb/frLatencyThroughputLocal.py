import matplotlib.pyplot as plt

rg_index_local_query_h_t = [797.525,1611.319434,3225.45,5961.53077,8783.247906,10157.7895,11266.70832,12151.38566,15027.63411,16069.14283]
rg_index_local_query_h_rt = [55.60846,54.65189,56.89935,57.74043,60.48856,60.0965,63.072,70.03555,77.13516,85.76795]
rg_index_local_query_h_rt_baseline = [54.98549,54.10117,56.22309,56.67477,58.79851,57.62273,58.95855,60.26167,61.31773,61.70544]
rg_index_local_balanced_t = [855.975,1729,3386.340341,6032.124197,8498.537537,9487.038472,10387.93362,12088.43078,13715.43923,13382.40727]
rg_index_local_balanced_rt = [55.91212,57.18535,60.47296,64.07872,69.38758,74.17382,78.58608,91.61684,108.42847,122.62211]
rg_index_local_balanced_rt_baseline = [55.41082,56.56458,59.67375,62.54055,66.90231,70.17609,71.29046,77.7006,79.82591,83.87318]
rg_index_local_update_h_t = [975.5262237,3656.425768,6354.482276,8701.563358,9813.4,10372.62842,13441.72975,13091.53347,12701.52799,12795.65314]
rg_index_local_update_h_rt = [56.20677,59.32152,64.56067,72.94261,84.47909,95.06335,107.73839,127.6664,160.42876,230.11181]
rg_index_local_update_h_rt_baseline = [55.60406,58.61693,63.42452,71.22673,80.84467,88.48724,96.19935,105.76218,116.38676,125.41047]

f, ax = plt.subplots()

ax.plot(rg_index_local_query_h_t, rg_index_local_query_h_rt, color='steelblue', marker='+', label='local w95/5')
ax.plot(rg_index_local_query_h_t, rg_index_local_query_h_rt_baseline, color='gray', linestyle='-.', label='notification')
ax.plot(rg_index_local_balanced_t, rg_index_local_balanced_rt, color='steelblue', marker='+', linestyle='dashed', label='local w80/20')
ax.plot(rg_index_local_update_h_t, rg_index_local_update_h_rt, color='steelblue', marker='+', linestyle='dotted', label='local w60/40')

ax.set(xlabel='Throughput [operations/s]', ylabel='95-th %-ile update latency [ms]')

ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 200.0])

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='upper left')

plt.savefig('ycsb_update_latency_local.png')
plt.close()