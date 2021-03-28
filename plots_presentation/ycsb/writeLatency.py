import matplotlib.pyplot as plt

throughput_local_w95 = [797.525,1611.319434,3225.45,5961.53077,8783.247906,10157.7895,11266.70832,12151.38566,15027.63411,16069.14283,15890.65809]
write_rt_local_w95 = [1.186,1.075,1.027,0.938,0.94,1.218,1.759,2.611,3.909,4.639,4.791]
throughput_local_w80 = [855.975,1729,3386.340341,6032.124197,8498.537537,9487.038472,10387.93362,12088.43078,13715.43923,13661.36725,13382.40727]
write_rt_local_w80 = [0.796,0.742,0.743,0.752,0.838,1.354,2.453,3.817,5.043,6.575,7.023]
throughput_local_w60 = [975.5262237,1906.702332,3656.425768,6354.482276,8701.563358,9813.4,10372.62842,13441.72975,13091.53347,12701.52799,12795.65314]
write_rt_local_w60 = [0.697,0.714,0.728,0.741,0.952,1.768,3.395,4.779,6.791,8.479,10.855]

f, ax = plt.subplots()

ax.plot(throughput_local_w95, write_rt_local_w95, color='black', label='w95/5')
ax.plot(throughput_local_w80, write_rt_local_w80, color='black', linestyle='dashed', label='w80/20')
ax.plot(throughput_local_w60, write_rt_local_w60, color='black', linestyle='dotted', label='w60/40')

ax.set(xlabel='Throughput [operations/s]', ylabel='95-th %-ile client update response time [ms]')

ax.grid(linestyle='dotted')

ax.set_ylim(bottom=0)
plt.ylim([0.0, 30.0])

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels=labels, loc='upper left')

plt.savefig('ycsb_write_latency.png')
plt.close()