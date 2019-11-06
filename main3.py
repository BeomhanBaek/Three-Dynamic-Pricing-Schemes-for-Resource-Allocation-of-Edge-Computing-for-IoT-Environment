import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from buyer import Buyer
from manager1 import Manager1
from manager2 import Manager2
from manager3 import Manager3
from matplotlib.ticker import FixedFormatter, LinearLocator
import pdb

fig1 = plt.figure(figsize=(15, 10), dpi=1000)
ax1 = fig1.add_subplot(111)
fig2 = plt.figure(figsize=(15, 10), dpi=1000)
ax2 = fig2.add_subplot(111)
fig3 = plt.figure(figsize=(15, 10), dpi=1000)
ax3 = fig3.add_subplot(111)

Avg1_Utility = []
Avg2_Utility = []
Avg3_Utility = []
Avg1_Time = []
Avg2_Time = []
Avg3_Time = []
Avg1_Payment = []
Avg2_Payment = []
Avg3_Payment = []

CPU_Cycle = []

for i in range(2, 9):
    Rs = [1, 2, 8, 10, 15]
    for j in range(len(Rs)):
        Rs[j] = Rs[j] * 8
    mus = [1, 1.5, 2, 3, 5]
    num_users = 5
    Fmax = 1000 * i
    Cs = [20000, 20000, 31680, 31680, 2640]
    users1, users2, users3 = [], [], []
    CPU_Cycle.append(i)
    avg1_utility = 0
    avg2_utility = 0
    avg3_utility = 0
    avg1_time = 0
    avg2_time = 0
    avg3_time = 0
    avg1_payment = 0
    avg2_payment = 0
    avg3_payment = 0

    for j in range(num_users):
        users1.append(Buyer(Rs[j], mus[j], Cs[j], Fmax))
        users2.append(Buyer(Rs[j], mus[j], Cs[j], Fmax))
        users3.append(Buyer(Rs[j], mus[j], Cs[j], Fmax))

    Mana1 = Manager1(Fmax, users1)
    Mana2 = Manager2(Fmax, users2)
    Mana3 = Manager3(Fmax, users3, 3.5)

    Mana1.solve()
    Mana2.solve()
    Mana3.solve()

    for j in range(num_users):
        avg1_utility += Mana1.users[j].utility
        avg2_utility += Mana2.users[j].utility
        avg3_utility += Mana3.users[j].utility
        avg1_time += Mana1.users[j].R * Mana1.users[j].C / Mana1.users[j].F
        avg2_time += Mana2.users[j].R * Mana2.users[j].C / Mana2.users[j].F
        avg3_time += Mana3.users[j].R * Mana3.users[j].C / Mana3.users[j].F
        avg1_payment += Mana1.users[j].w
        avg2_payment += Mana2.users[j].w
        avg3_payment += Mana3.users[j].w

    avg1_utility /= num_users
    avg2_utility /= num_users
    avg3_utility /= num_users
    avg1_time /= num_users
    avg2_time /= num_users
    avg3_time /= num_users
    avg1_payment /= num_users
    avg2_payment /= num_users
    avg3_payment /= num_users
    Avg1_Utility.append(avg1_utility)
    Avg2_Utility.append(avg2_utility)
    Avg3_Utility.append(avg3_utility)
    Avg1_Time.append(avg1_time)
    Avg2_Time.append(avg2_time)
    Avg3_Time.append(avg3_time)
    Avg1_Payment.append(avg1_payment)
    Avg2_Payment.append(avg2_payment)
    Avg3_Payment.append(avg3_payment)

print(Avg1_Payment)
print(Avg2_Payment)
print(Avg3_Payment)

ax1.plot(CPU_Cycle, Avg1_Utility, 'r*-', label = 'Average Utility of BID-PRAM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.plot(CPU_Cycle, Avg2_Utility, 'b^-', label = 'Average Utility of UNI-PRIM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.plot(CPU_Cycle, Avg3_Utility, 'gv-', label = 'Average Utility of FAID-PRIM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.set_xlabel('CPU Cycles of Edge Cloud (GHz)', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax1.set_ylabel('Average Utility', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax1.legend(prop = {'family' : 'Arial', 'size':20}, loc = 2)

for tick in ax1.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax1.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)

ax2.plot(CPU_Cycle, Avg1_Time, 'r*-', label = 'Average Time of BID-PRAM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax2.plot(CPU_Cycle, Avg2_Time, 'b^-', label = 'Average Time of UNI-PRIM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax2.plot(CPU_Cycle, Avg3_Time, 'gv-', label = 'Average Time of FAID-PRIM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax2.set_xlabel('CPU Cycles of Edge Cloud (GHz)', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax2.set_ylabel('Average Time', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax2.legend(prop = {'family' : 'Arial', 'size':20}, loc = 2)

for tick in ax2.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax2.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)

ax3.plot(CPU_Cycle, Avg1_Payment, 'r*-', label = 'Average Payment of BID-PRAM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax3.plot(CPU_Cycle, Avg2_Payment, 'b^-', label = 'Average Payment of UNI-PRIM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax3.plot(CPU_Cycle, Avg3_Payment, 'gv-', label = 'Average Payment of FAID-PRIM', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax3.set_xlabel('CPU Cycles of Edge Cloud (GHz)', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax3.set_ylabel('Average Payment', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax3.legend(prop = {'family' : 'Arial', 'size':20}, loc = 2)

for tick in ax3.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax3.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)


fig1.savefig('fig7.pdf')
fig2.savefig('fig8.pdf')
fig3.savefig('fig9.pdf')
