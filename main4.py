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

Rs = [1, 2, 8, 10, 15]
for i in range(len(Rs)):
    Rs[i] = Rs[i] * 8
mus = [1, 1.5, 2, 3, 5]
num_users = 5
Fmax = 8000 #GHz
Cs = [20000, 20000, 31680, 31680, 2640] #needed cycles per one bit
users1, users2, users3 = [], [], []

for i in range(num_users):
    users1.append(Buyer(Rs[i], mus[i], Cs[i], Fmax))
    users2.append(Buyer(Rs[i], mus[i], Cs[i], Fmax))
    users3.append(Buyer(Rs[i], mus[i], Cs[i], Fmax))

Mana1 = Manager1(Fmax, users1)
Mana2 = Manager2(Fmax, users2)
Mana3 = Manager3(Fmax, users3, 3.5)

Mana1.solve()
Mana2.solve()
Mana3.solve()

sum1_utility = 0
sum2_utility = 0
sum3_utility = 0
sum1_payment = 0
sum2_payment = 0
sum3_payment = 0


for i in range(num_users):
    sum1_utility += Mana1.users[i].utility
    sum2_utility += Mana2.users[i].utility
    sum3_utility += Mana3.users[i].utility
    sum1_payment += Mana1.users[i].w
    sum2_payment += Mana2.users[i].w
    sum3_payment += Mana3.users[i].w

Utility_Sum = [sum1_utility, sum2_utility, sum3_utility]
Revenue = [sum1_payment, sum2_payment, sum3_payment]
Model = ['BID-PRAM', 'UNI-PRIM', 'FAID-PRIM']
Zero_Line = [0, 0, 0]

print(Utility_Sum)
print(Revenue)

ax1.bar(Model, Utility_Sum, label = 'Sum of Utilities', width = 0.3, color='blue', edgecolor='black', bottom = 0)
ax1.bar(Model, Revenue, label = 'Revenues', width = 0.3, color='red', edgecolor='black', bottom = 0)
ax1.plot(Model, Zero_Line, 'k', linewidth = 1)
ax1.set_ylabel('Sums of Utilities & Revenues', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax1.legend(prop = {'family' : 'Arial', 'size':20}, loc = 3)

for tick in ax1.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax1.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)

fig1.savefig('fig10.pdf')