import matplotlib.pyplot as plt

rg_index_query_h_t = [1820.663581,3568.905905,6930.770076,12451.61631,17539.68764,20160.75782,22126.11278,23973.24715,31735.89223,31845.50641,30994.16664]
rg_index_query_h_rt = [1.932,1.997,2.087,2.433,4.119,7.711,14.007,25.471,40.607,78.079,228.479]
rg_index_balanced_t = [2438.650573,4628.287061,8902.550608,15317.74317,20085.29545,22196.77425,24212.79851,30774.74443,31544.36606,29573.53863]
rg_index_balanced_rt = [2.221,2.375,2.901,4.731,9.431,18.527,31.759,45.183,86.911,222.335]
# rg_index_update_h_t = [2262.581615,4296.797317,8114.350497,14396.66111,19454.94797,21711.33508,22728.91293,26600.73749,31175.74518,31582.51668,29552.40033]
# rg_index_update_h_rt = [2.085,2.167,2.305,2.991,5.511,11.767,22.591,37.151,60.959,115.711,178.047]

p_index_query_h_t = [38.23313016,76.33883702,153.1564581,306.5469571,616.0746846,1226.689514,2455.425708,4891.827135,9511.720678,15234.90754,15196.65371]
p_index_query_h_rt = [83.135,82.815,82.623,82.815,82.687,82.431,82.559,84.031,89.599,126.719,455.167]
p_index_balanced_t = [72.74439507,141.9058868,286.6107845,581.6972069,1156.299311,2327.383514,4607.85604,9015.751439,14673.92117,17119.53869,17147.94867]
p_index_balanced_rt = [83.519,83.135,82.751,82.815,82.751,82.687,83.391,91.199,138.239,272.127,1174.527]
# p_index_update_h_t = [59.04494809,118.8847678,236.6011608,482.1641614,968.5745651,1934.323318,3869.437351,7657.106918,13558.33088,17682.99306,17149.35866]
# p_index_update_h_rt = [83.135,82.815,82.559,82.495,82.431,82.367,82.495,85.311,106.303,188.799,688.127]


p_index_cache_query_h_t = [1120.66867,2384.280187,4556.011544,7653.927111,10175.17806,11633.65355,14396.36897,16503.59664,16742.74964,16654.45998]
p_index_cache_query_h_rt = [5.566865941,5.235901385,5.487155424,6.536157384,9.848670327,17.25705612,27.95678003,48.83390461,96.37777273,194.2373638]
p_index_cache_balanced_t = [297.8943518,613.0289348,1227.703715,2418.015947,4612.382862,7856.078123,11087.02554,12442.03725,13618.03456]
p_index_cache_balanced_rt = [39.64260204,39.64260204,38.45767015,39.0474615,40.85994844,47.6734959,67.59914374,120.7298872,221.3533194]
# p_index_cache_update_h_t = [61.08344631,122.2594645,251.9142445,534.3139412,1246.713814,3497.655795,12855.55637,18392.3749,24954.65788,25288.01589,25211.608]
# p_index_cache_update_h_rt = [82.51373611,81.10137219,78.33016834,73.29363537,63.56625524,45.24496011,24.23898764,33.64265102,49.6742564,97.31662456,190.7874036]

plt.rcParams["figure.figsize"] = (10,6)
plt.rcParams["figure.dpi"] = 200.0

f, ax = plt.subplots()

ax.plot(rg_index_query_h_t, rg_index_query_h_rt, color='c', marker='o', label='rg-index w95/5')
ax.plot(rg_index_balanced_t, rg_index_balanced_rt, color='c', marker='o', linestyle='dashed', label='rg-index w50/50')
# ax.plot(rg_index_update_h_t, rg_index_update_h_rt, color='c', marker='o', linestyle='dotted', label='rg-index w60/40')

ax.plot(p_index_query_h_t, p_index_query_h_rt, color='b', marker='x', label='p-index w95/5')
ax.plot(p_index_balanced_t, p_index_balanced_rt, color='b', marker='x', linestyle='dashed', label='p-index w50/50')
# ax.plot(p_index_update_h_t, p_index_update_h_rt, color='b', marker='x', linestyle='dotted', label='p-index w60/40')

ax.plot(p_index_cache_query_h_t, p_index_cache_query_h_rt, color='g', marker='+', label='p-index-cache w95/5')
ax.plot(p_index_cache_balanced_t, p_index_cache_balanced_rt, color='g', marker='+', linestyle='dashed', label='p-index-cache w50/50')
# ax.plot(p_index_cache_update_h_t, p_index_cache_update_h_rt, color='g', marker='+', linestyle='dotted', label='p-index-cache w60/40')

ax.set(xlabel='Throughput [operations/s]', ylabel='Query response time [ms]')

ax.grid(linestyle='dotted')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='upper left')


plt.ylim([0.0, 200.0])

plt.savefig('ycsb_responseTime.png')
plt.close()