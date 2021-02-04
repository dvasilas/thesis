import matplotlib.pyplot as plt

rg_index_query_h_t = [1820.663581,3568.905905,6930.770076,12451.61631,17539.68764,20160.75782,22126.11278,23973.24715,31735.89223,31845.50641,30994.16664]
rg_index_query_h_rt = [1.932,1.997,2.087,2.433,4.119,7.711,14.007,25.471,40.607,78.079,228.479]
rg_index_balanced_t = [1933.832906,3771.013509,7111.032295,12524.42002,17418.73844,19750.14438,21533.05283,23404.46187,29004.73811,30321.86524,29615.45636]
rg_index_balanced_rt = [2.036,2.119,2.257,2.783,4.763,9.423,17.311,30.927,54.271,107.583,301.823]
rg_index_update_h_t = [2262.581615,4296.797317,8114.350497,14396.66111,19454.94797,21711.33508,22728.91293,26600.73749,31175.74518,31582.51668,29552.40033]
rg_index_update_h_rt = [2.085,2.167,2.305,2.991,5.511,11.767,22.591,37.151,60.959,115.711,178.047]

p_index_query_h_t = [38.23313016,76.33883702,153.1564581,306.5469571,616.0746846,1226.689514,2455.425708,4891.827135,9511.720678,15234.90754,15196.65371]
p_index_query_h_rt = [83.135,82.815,82.623,82.815,82.687,82.431,82.559,84.031,89.599,126.719,455.167]
p_index_balanced_t = [38.23313016,76.33883702,153.1564581,306.5469571,616.0746846,1226.689514,2455.425708,4891.827135,9511.720678,15234.90754,15196.65371]
p_index_balanced_rt = [83.199,82.879,82.559,82.495,82.559,82.367,82.431,83.583,95.871,147.327,558.079]
p_index_update_h_t = [59.04494809,118.8847678,236.6011608,482.1641614,968.5745651,1934.323318,3869.437351,7657.106918,13558.33088,17682.99306,17149.35866]
p_index_update_h_rt = [83.135,82.815,82.559,82.495,82.431,82.367,82.495,85.311,106.303,188.799,688.127]

p_index_cache_query_h_t = [38.28500389,77.37241198,161.2270616,343.412639,796.71888,2248.535,9962.515331,16949.83051,24936.22127,24951.3343,24380.31582]
p_index_cache_query_h_rt = [82.23286155,81.57271229,78.28756366,73.70463856,63.33045223,44.87403037,20.22262958,23.71843492,32.25541412,64.50095426,132.4719913]
p_index_cache_balanced_t = [45.12780578,93.31832791,190.9430806,408.644789,944.9363728,2661.159415,11045.07389,16967.7977,23267.75711,24174.18968,23340.32606]
p_index_cache_balanced_rt = [82.34747209,81.17786083,78.11750074,73.32108888,63.34917336,44.76773517,21.4918759,27.87841791,40.67399775,78.4806431,163.1932563]
p_index_cache_update_h_t = [61.08344631,122.2594645,251.9142445,534.3139412,1246.713814,3497.655795,12855.55637,18392.3749,24954.65788,25288.01589,25211.608]
p_index_cache_update_h_rt = [82.51373611,81.10137219,78.33016834,73.29363537,63.56625524,45.24496011,24.23898764,33.64265102,49.6742564,97.31662456,190.7874036]

plt.rcParams["figure.figsize"] = (10,6)
plt.rcParams["figure.dpi"] = 200.0

f, ax = plt.subplots()

ax.plot(rg_index_query_h_t, rg_index_query_h_rt, color='c', marker='o', label='rg-index w95/5')
ax.plot(rg_index_balanced_t, rg_index_balanced_rt, color='c', marker='o', linestyle='dashed', label='rg-index w80/20')
ax.plot(rg_index_update_h_t, rg_index_update_h_rt, color='c', marker='o', linestyle='dotted', label='rg-index w60/40')

ax.plot(p_index_query_h_t, p_index_query_h_rt, color='b', marker='x', label='p-index w95/5')
ax.plot(p_index_balanced_t, p_index_balanced_rt, color='b', marker='x', linestyle='dashed', label='p-index w80/20')
ax.plot(p_index_update_h_t, p_index_update_h_rt, color='b', marker='x', linestyle='dotted', label='p-index w60/40')

ax.plot(p_index_cache_query_h_t, p_index_cache_query_h_rt, color='g', marker='+', label='p-index-cache w95/5')
ax.plot(p_index_cache_balanced_t, p_index_cache_balanced_rt, color='g', marker='+', linestyle='dashed', label='p-index-cache w80/20')
ax.plot(p_index_cache_update_h_t, p_index_cache_update_h_rt, color='g', marker='+', linestyle='dotted', label='p-index-cache w60/40')

ax.set(xlabel='Throughput [operations/s]', ylabel='Query response time [ms]')

ax.grid(linestyle='dotted')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='upper left')


plt.ylim([0.0, 200.0])

plt.savefig('ycsb_responseTime.png')
plt.close()