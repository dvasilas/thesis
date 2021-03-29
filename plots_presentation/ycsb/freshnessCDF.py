import matplotlib.pyplot as plt

rg_index_query_h_t = [0 ,1, 2, 3, 4]
rg_index_query_h_rt = [67.52566667, 91.36133333, 99.614, 100.0, 100.0]

p_index_query_h_t = [0 ,1, 2, 3, 4]
p_index_query_h_rt = [83.70233333,97.13066667,99.918,100, 100.0]

p_index_cache_query_h_t = [0 ,1, 2, 3, 4]
p_index_cache_query_h_rt = [83.007, 97.02066667, 99.91933333, 100, 100.0]

# p_index_cache_query_h_t_90 = [38.28500389,77.37241198,161.2270616,343.412639,796.71888,2248.535,9962.515331,16949.83051,24936.22127,24951.3343,24380.31582]
# p_index_cache_query_h_rt_90 = [83.839,83.583,83.327,83.263,83.007,82.815,83.775,90.815,93.119100,115.711,294.655]


# plt.rcParams["figure.figsize"] = (10,6)
# plt.rcParams["figure.dpi"] = 200.0

f, ax = plt.subplots()

ax.plot(rg_index_query_h_t, rg_index_query_h_rt, color='c', marker='o', label='rg-index')
# ax.plot(rg_index_balanced_t, rg_index_balanced_rt, color='c', marker='o', linestyle='dashed', label='rg-index w80/20')
# ax.plot(rg_index_update_h_t, rg_index_update_h_rt, color='c', marker='o', linestyle='dotted', label='rg-index w60/40')

ax.plot(p_index_query_h_t, p_index_query_h_rt, color='b', marker='x', label='p-index')
# ax.plot(p_index_balanced_t, p_index_balanced_rt, color='b', marker='x', linestyle='dashed', label='p-index w80/20')
# ax.plot(p_index_update_h_t, p_index_update_h_rt, color='b', marker='x', linestyle='dotted', label='p-index w60/40')

ax.plot(p_index_cache_query_h_t, p_index_cache_query_h_rt, color='g', marker='+', label='p-index-cache')

# ax.plot(p_index_cache_query_h_t_90, p_index_cache_query_h_rt_90, color='g', marker='+', label='p-index-cache')

# ax.plot(p_index_cache_balanced_t, p_index_cache_balanced_rt, color='g', marker='+', linestyle='dashed', label='p-index-cache w80/20')
# ax.plot(p_index_cache_update_h_t, p_index_cache_update_h_rt, color='g', marker='+', linestyle='dotted', label='p-index-cache w60/40')

ax.set(xlabel='Throughput [operations/s]', ylabel='CDF [%]')

ax.grid(linestyle='dotted')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, frameon=False)

ax.set_xlim(left=1)
plt.ylim([0.0, 105.0])
ticks = [0 ,1, 2, 3, 4]
labels = ["1", "2", "3-4", "4-8", ">8"]
plt.xticks(ticks, labels)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='lower right')

plt.savefig('freshness_cdf_9505.png')


rg_index_query_h_t = [0 ,1, 2, 3, 4]
rg_index_query_h_rt = [14.861, 29.84866667, 55.606, 91.443, 100]

p_index_query_h_t = [0 ,1, 2, 3, 4]
p_index_query_h_rt = [23.28766667,43.46533333,72.51733333,96.627,100]

p_index_cache_query_h_t = [0 ,1, 2, 3, 4]
p_index_cache_query_h_rt = [22.49433333,42.33933333,71.738,96.65166667,100]

# p_index_cache_query_h_t_50 = [71.22948264,147.2228764,307.6078567,643.212722,1478.740423,4145.925324,13816.27202,21511.59629,24957.23696,24089.047]
# p_index_cache_query_h_rt_50 = [82.4332622,80.84648484,77.98148638,73.55949671,64.22031353,45.75520735,26.9158474,34.12004359,58.93067202,151.2874734]
# plt.rcParams["figure.figsize"] = (10,6)
# plt.rcParams["figure.dpi"] = 200.0

f, ax = plt.subplots()

ax.plot(rg_index_query_h_t, rg_index_query_h_rt, color='c', marker='o', label='rg-index')
# ax.plot(rg_index_balanced_t, rg_index_balanced_rt, color='c', marker='o', linestyle='dashed', label='rg-index w80/20')
# ax.plot(rg_index_update_h_t, rg_index_update_h_rt, color='c', marker='o', linestyle='dotted', label='rg-index w60/40')

ax.plot(p_index_query_h_t, p_index_query_h_rt, color='b', marker='x', label='p-index')
# ax.plot(p_index_balanced_t, p_index_balanced_rt, color='b', marker='x', linestyle='dashed', label='p-index w80/20')
# ax.plot(p_index_update_h_t, p_index_update_h_rt, color='b', marker='x', linestyle='dotted', label='p-index w60/40')

ax.plot(p_index_cache_query_h_t, p_index_cache_query_h_rt, color='g', marker='+', label='p-index-cache')

# ax.plot(p_index_cache_query_h_t_50, p_index_cache_query_h_rt_50, color='g', marker='+', linestyle='dashed', label='p-index-cache')
# ax.plot(p_index_cache_balanced_t, p_index_cache_balanced_rt, color='g', marker='+', linestyle='dashed', label='p-index-cache w80/20')
# ax.plot(p_index_cache_update_h_t, p_index_cache_update_h_rt, color='g', marker='+', linestyle='dotted', label='p-index-cache w60/40')

ax.set(xlabel='Throughput [operations/s]', ylabel='CDF [%]')

ax.grid(linestyle='dotted')

ax.set_xlim(left=1)
plt.ylim([0.0, 105.0])
ticks = [0 ,1, 2, 3, 4]
labels = ["1", "2", "3-4", "4-8", ">8"]
plt.xticks(ticks, labels)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='lower right')

plt.savefig('freshness_cdf_5050.png')
plt.close()