import numpy as np
import matplotlib.pyplot as plt
from buyer import Buyer
from manager1 import Manager1
from manager2 import Manager2
from manager3 import Manager3

Fmax, C = 100, 10
Rmax, mumax = 10, 10
Rs, mus = [], []
UnitPrice_AVG1, UnitPrice_AVG2, UnitPrice_AVG3_min, UnitPrice_AVG3_max, UnitPrice_AVG3_avg = [], [], [], [], []
Utility_AVG1, Utility_AVG2, Utility_AVG3 = [], [], []


number = 10000

for k in range(4, 15):
    num_users = k
    for n in range(number):
        avg1, avg2, avg3 = 0, 0, [0, 0]
        avg1_utility, avg2_utility, avg3_utility = 0, 0, 0
        for i in range(num_users):
            Rs.append(Rmax*np.random.random())
            mus.append(mumax*np.random.random())

        users1, users2, users3 = [], [], []

        for i in range(num_users):
            users1.append(Buyer(Rs[i], mus[i], C, Fmax))
            users2.append(Buyer(Rs[i], mus[i], C, Fmax))
            users3.append(Buyer(Rs[i], mus[i], C, Fmax))

        Mana1 = Manager1(Fmax, users1)
        Mana2 = Manager2(Fmax, users2)
        Mana3 = Manager3(Fmax, users3, 3.5)
        Mana1.solve()
        Mana2.solve()
        Mana3.solve()
        avg1 += Mana1.unit_price
        avg2 += Mana2.unit_price
        avg3[0] += Mana3.unit_price[0]
        avg3[1] += Mana3.unit_price[1]
        revenue = 0
        for user in Mana3.users:
            revenue += user.w
        for i in range(num_users):
            avg1_utility += Mana1.users[i].utility / num_users
            avg2_utility += Mana2.users[i].utility / num_users
            avg3_utility += Mana3.users[i].utility / num_users

    avg1 /= number
    avg2 /= number
    avg3[0] /= number
    avg3[1] /= number
    revenue /= number
    avg1_utility /= number
    avg2_utility /= number
    avg3_utility /= number
    UnitPrice_AVG1.append(avg1)
    UnitPrice_AVG2.append(avg2)
    UnitPrice_AVG3_min.append(avg3[1])
    UnitPrice_AVG3_max.append(avg3[0])
    UnitPrice_AVG3_avg.append(revenue / Fmax)
    Utility_AVG1.append(avg1_utility)
    Utility_AVG2.append(avg2_utility)
    Utility_AVG3.append(avg3_utility)

print(UnitPrice_AVG1, UnitPrice_AVG2, UnitPrice_AVG3_min, UnitPrice_AVG3_max, UnitPrice_AVG3_avg)
f = open("data.txt", 'w')
f.write("UnitPrice_AVG1 \n")
for i in range(len(UnitPrice_AVG1)):
    f.write(str(UnitPrice_AVG1[i])+'\n')
f.write('\n')
f.write("UnitPrice_AVG2 \n")
for i in range(len(UnitPrice_AVG2)):
    f.write(str(UnitPrice_AVG2[i])+'\n')
f.write('\n')
f.write("UnitPrice_AVG3_min \n")
for i in range(len(UnitPrice_AVG3_min)):
    f.write(str(UnitPrice_AVG3_min[i])+'\n')
f.write('\n')
f.write("UnitPrice_AVG3_max \n")
for i in range(len(UnitPrice_AVG3_max)):
    f.write(str(UnitPrice_AVG3_max[i])+'\n')
f.write('\n')
f.write("UnitPrice_AVG3_avg \n")
for i in range(len(UnitPrice_AVG3_avg)):
    f.write(str(UnitPrice_AVG3_avg[i])+'\n')
f.write('\n')
f.write("Utility_AVG1 \n")
for i in range(len(Utility_AVG1)):
    f.write(str(Utility_AVG1[i])+'\n')
f.write('\n')
f.write("Utility_AVG2 \n")
for i in range(len(Utility_AVG2)):
    f.write(str(Utility_AVG2[i])+'\n')
f.write('\n')
f.write("Utility_AVG3 \n")
for i in range(len(Utility_AVG3)):
    f.write(str(Utility_AVG3[i])+'\n')
f.write('\n')



x = list(range(4, 15))

fig1 = plt.figure(figsize=(15, 10), dpi = 1000)
ax1 = fig1.add_subplot(111)
fig2 = plt.figure(figsize=(15, 10), dpi = 1000)
ax2 = fig2.add_subplot(111)

ax1.plot(x, UnitPrice_AVG1, 'rd-', label = 'Unit Price of Model 1', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.plot(x, UnitPrice_AVG2, 'b^-', label = 'Unit Price of Model 2', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.plot(x, UnitPrice_AVG3_avg, 'k*-', label = 'Average Unit Price of Model 3', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.plot(x, UnitPrice_AVG3_min, 'yo-.', label = 'Minimum Unit Price of Model 3', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.plot(x, UnitPrice_AVG3_max, 'go-.', label = 'Maximum Unit Price of Model 3', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax1.set_xlabel('Number of Users', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax1.set_ylabel('Unit Prices', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax1.legend(prop = {'family' : 'Arial', 'size':20}, loc = 2)

for tick in ax1.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax1.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)

ax2.plot(x, Utility_AVG1, 'rd-', label = 'Average Utility of Model 1', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax2.plot(x, Utility_AVG2, 'b^-', label = 'Average Utlity of Model 2', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax2.plot(x, Utility_AVG3, 'go-.', label = 'Average Utility of Model 3', linewidth = 1.5, markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax2.set_xlabel('Number of Users', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax2.set_ylabel('Utility', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax2.legend(prop = {'family' : 'Arial', 'size':20}, loc = 2)

for tick in ax2.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax2.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)

fig1.savefig('fig5.pdf')
fig2.savefig('fig6.pdf')
