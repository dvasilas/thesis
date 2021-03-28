import matplotlib.pyplot as plt

rg_index_query_h_t = [1820.663581,3568.905905,6930.770076,12451.61631,17539.68764,20160.75782,22126.11278,23973.24715,31735.89223,31845.50641,30994.16664]
rg_index_query_h_rt = [1.932,1.997,2.087,2.433,4.119,7.711,14.007,25.471,40.607,78.079,228.479]

p_index_query_h_t = [38.23313016,76.33883702,153.1564581,306.5469571,616.0746846,1226.689514,2455.425708,4891.827135,9511.720678,15234.90754,15196.65371]
p_index_query_h_rt = [83.135,82.815,82.623,82.815,82.687,82.431,82.559,84.031,89.599,126.719,455.167]

p_index_cache_query_h_t = [1120.66867,2384.280187,4556.011544,7653.927111,10175.17806,11633.65355,14396.36897,16503.59664,16742.74964, 16654.45998]
p_index_cache_query_h_rt = [5.566865941,5.235901385,5.487155424,6.536157384,9.848670327,17.25705612,27.95678003,48.83390461,96.3777727, 194.2373638]

# p_index_cache_query_h_t_90 = [38.28500389,77.37241198,161.2270616,343.412639,796.71888,2248.535,9962.515331,16949.83051,24936.22127,24951.3343,24380.31582]
# p_index_cache_query_h_rt_90 = [83.839,83.583,83.327,83.263,83.007,82.815,83.775,90.815,93.119,115.711,294.655]


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

# ax.set(xlabel='Throughput [operations/s]', ylabel='Query response time [ms]')

ax.grid(linestyle='dotted')

handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles,labels=labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, frameon=False)


plt.ylim([0.0, 200.0])

plt.savefig('ycsb_responseTime_1.png')

rg_index_query_h_t = [2438.650573,4628.287061,8902.550608,15317.74317,20085.29545,22196.77425,24212.79851,30774.74443,31544.36606,29573.53863]
rg_index_query_h_rt = [2.117,2.191,2.329,3.345,6.587,13.839,25.535,36.415,63.999,162.431]

p_index_query_h_t = [72.74439507,141.9058868,286.6107845,581.6972069,1156.299311,2327.383514,4607.85604,9015.751439,14673.92117,17119.53869,17147.94867]
p_index_query_h_rt = [83.199,82.879,82.623,82.623,82.559,82.495,82.751,87.999,125.951,2246.143,811.519]


p_index_cache_query_h_t = [297.8943518,613.0289348,1227.703715,2418.015947,4612.382862,7856.078123,11087.02554,12442.03725,13618.03456]
p_index_cache_query_h_rt = [39.64260204,39.64260204,38.45767015,39.0474615,40.85994844,47.6734959,67.59914374,120.7298872,221.3533194]

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

# ax.set(xlabel='Throughput [operations/s]', ylabel='Query response time [ms]')

ax.grid(linestyle='dotted')

# handles, labels = ax.get_legend_handles_labels()
# ax.legend(handles,labels=labels, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, frameon=False)


plt.ylim([0.0, 200.0])

plt.savefig('ycsb_responseTime_2.png')
plt.close()