import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from buyer import Buyer
from manager1 import Manager1
from manager2 import Manager2
from manager3 import Manager3
from matplotlib.ticker import FixedFormatter, LinearLocator
import pdb

'''
num_users, Fmax, C = 5, 100, 10
users1 = []
users2 = []
users3 = []
Rmax, mumax = 10, 10
Rs, mus = [], []

for i in range(num_users):
    Rs.append(Rmax*np.random.random())
    mus.append(mumax*np.random.random())

sorted_idx = sorted(range(num_users), key = lambda i: Rs[i] * mus[i])
Rs = [Rs[sorted_idx[i]] for i in range(num_users)]
mus = [mus[sorted_idx[i]] for i in range(num_users)]
'''

Rs = [1, 2, 8, 10, 15] #MegaBytes

for i in range(len(Rs)):
    Rs[i] = Rs[i] * 8

mus = [1, 1.5, 2, 3, 5]
num_users = 5
Fmax = 8 #GHz

Fmax *= 10 ** 3 #Megabits to GHz

Cs = [20000, 20000, 31680, 31680, 2640] #needed cycles per one bit
users1, users2, users3 = [], [], []

for i in range(num_users):
    users1.append(Buyer(Rs[i], mus[i], Cs[i], Fmax))
    users2.append(Buyer(Rs[i], mus[i], Cs[i], Fmax))
    users3.append(Buyer(Rs[i], mus[i], Cs[i], Fmax))

Mana1 = Manager1(Fmax, users1)
Mana2 = Manager2(Fmax, users2)
Mana3 = Manager3(Fmax, users3, 3.5)

print('<<First Model>>')
Mana1.solve()
Mana1.print_info()
print('<<Second Model>>')
Mana2.solve()
Mana2.print_info()
print('<<Third Model>>')
Mana3.solve()
Mana3.print_info()


fig1 = plt.figure(figsize=(15, 10), dpi = 1000)
ax1 = fig1.add_subplot(111, projection='3d')

fig2 = plt.figure(figsize = (15, 10), dpi =1000)
ax2 = fig2.add_subplot(111, projection='3d' )

'''
fig3 = plt.figure(figsize=(15, 10), dpi = 1000)
ax3 = fig3.add_subplot(111)
fig4 = plt.figure(figsize=(15, 10), dpi = 1000)
ax4 = fig4.add_subplot(111)
'''

x1 = np.arange(1, 4)
y1 = np.arange(1, num_users+1)
z1 = np.zeros(num_users)


xx1, yy1 = np.meshgrid(x1, y1)
xxx1, yyy1 = xx1.ravel(), yy1.ravel()

top1 = np.array([])
top2 = np.array([])
avg_antiutility = np.array([0, 0, 0])
avg_payment = np.array([0, 0, 0])
for i in range(num_users):
    top1 = np.append(top1, [-Mana1.users[i].utility, -Mana2.users[i].utility, -Mana3.users[i].utility])
    top2 = np.append(top2, [Mana1.users[i].w, Mana2.users[i].w, Mana3.users[i].w])
    avg_antiutility = avg_antiutility + np.array([-Mana1.users[i].utility, -Mana2.users[i].utility, -Mana3.users[i].utility])
    avg_payment = avg_payment + np.array([Mana1.users[i].w, Mana2.users[i].w, Mana3.users[i].w])
avg_antiutility = avg_antiutility / num_users
avg_payment = avg_payment / num_users
bottom1 = np.zeros_like(top1)
bottom2 = np.zeros_like(top2)
width = 0.3
depth = 0.7
colors1 = ['darkgreen', 'seagreen', 'mediumspringgreen']*num_users
colors2 = ['blue', 'royalblue', 'cyan']*num_users


ax1.bar3d(xxx1, yyy1, bottom1, width, depth, top1, shade = False, color=colors1, edgecolor = 'black')
ax1.bar3d(np.array([1, 2, 3]), np.array([0, 0, 0]), np.array([0, 0, 0]), width, depth, avg_antiutility, shade = False, color = ['dimgray', 'darkgray', 'lightgray'], edgecolor = 'black')
ax1.view_init(30, -120)
ax1.set_xticks([1.2, 2.2, 3.2])
ax1.xaxis.set_major_formatter(FixedFormatter('123'))
ax1.set_xlabel('Model', fontname = 'Arial', fontweight = 'bold', fontsize = 25)
ax1.set_ylabel('Users', fontname = 'Arial', fontweight = 'bold', fontsize = 25)
ax1.set_zlabel('-Utility', fontname = 'Arial', fontweight = 'bold', fontsize = 25)
ax1.set_title('', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
for tick in ax1.get_xticklabels():
    tick.set_fontname('Arial')
for tick in ax1.get_yticklabels():
    tick.set_fontname('Arial')
fig1.subplots_adjust(top=1, bottom=0, left=0, right=1)


ax2.bar3d(xxx1, yyy1, bottom2, width, depth, top2, shade = False, color = colors2, edgecolor = 'black')
ax2.bar3d(np.array([1, 2, 3]), np.array([0, 0, 0]), np.array([0, 0, 0]), width, depth, avg_payment, shade = False, color = ['dimgray', 'darkgray', 'lightgray'], edgecolor = 'black')
ax2.view_init(30, -120)
ax2.set_xticks([1.2, 2.2, 3.2])
ax2.xaxis.set_major_formatter(FixedFormatter('123'))
ax2.set_xlabel('Model', fontname = 'Arial', fontweight = 'bold', fontsize = 25)
ax2.set_ylabel('Users', fontname = 'Arial', fontweight = 'bold', fontsize = 25)
ax2.set_zlabel('Payment', fontname = 'Arial', fontweight = 'bold', fontsize = 25)
ax2.set_title('', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
fig2.subplots_adjust(top=1, bottom=0, left=0, right=1)

'''
fig2.savefig('fig2-New.pdf')

fig1.savefig('fig1-New.pdf')
'''
'''
Mana1.users[0], Mana1.users[2] = Mana1.users[2], Mana1.users[0]
x3 = np.arange(0.5*Mana1.users[0].w, 1.5*Mana1.users[0].w, 10)
utility = [[] for i in range(num_users)]
sum = 0
for i in range(1, num_users):
    sum += Mana1.users[i].w
for a in x3:
    Mana1.users[0].F = Mana1.users[0].Fmax*a/(sum+a)
    Mana1.users[0].w = a
    b = Mana1.users[0].compute_utility(a)
    utility[0].append(b)
    for i in range(1, num_users):
        Mana1.users[i].F = Mana1.users[i].Fmax*Mana1.users[i].w/(sum+a)
        utility[i].append(Mana1.users[i].compute_utility(Mana1.users[i].w))

np.asarray(utility)

ax3.plot(x3, utility[2], 'rd-' , label = '1st User\'s Utility', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 15)
ax3.plot(x3, utility[1], 'b^-' , label = '2nd User\'s Utility', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 15)
ax3.plot(x3, utility[0], 'k*-' , label = '3rd User\'s Utility', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 20)
ax3.plot(x3, utility[3], 'cs-' , label = '4th User\'s Utility', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 15)
ax3.plot(x3, utility[4], 'go-' , label = '5th User\'s Utility', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 15)
ax3.set_xlabel('3rd User\'s Payment', fontname='Arial', fontweight = 'bold', fontsize = 30)
ax3.set_ylabel('Utility of Each User', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax3.set_title('', fontname='Arial'
                           '', fontweight = 'bold', fontsize = 20)
for tick in ax3.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax3.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
ax3.legend(prop = {'family' : 'Arial', 'size':20}, loc = 4)

ax3.annotate('Nash Equilibrium Point \n -1354 at 275.0', fontname = 'Arial', fontsize =25, xy = (275.0, -1353.9), xytext = (175, -1000), arrowprops = dict(width = 0.5, headwidth = 5, shrinkA = 0, facecolor = 'black'),  verticalalignment='top', ha = 'center')
'''
'''
x4 = np.arange(0.11, Mana2.unit_price*1.1, 0.002)
distributed_F = [[] for i in range(num_users)]
sum_F = []
dashed_line = [Fmax / 1000] * len(x4)
for i in range(num_users):
    for j in x4:
        Mana2.unit_price = j
        Mana2.users[i].w = (Mana2.users[i].R*Mana2.users[i].C*Mana2.unit_price/Mana2.users[i].mu) ** 0.5
        Mana2.users[i].F = Mana2.users[i].w / Mana2.unit_price
        distributed_F[i].append(Mana2.users[i].F / 1000)

for i in range(len(x4)):
    sum = 0
    for j in range(num_users):
        sum += distributed_F[j][i]
    sum_F.append(sum)

np.asarray(distributed_F)

ax4.plot(x4, distributed_F[0], 'rd-' , label = '1st User\'s F', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax4.plot(x4, distributed_F[1], 'b^-' , label = '2nd User\'s F', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax4.plot(x4, distributed_F[2], 'gv-' , label = '3rd User\'s F', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax4.plot(x4, distributed_F[3], 'cs-' , label = '4th User\'s F', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax4.plot(x4, distributed_F[4], 'mo-' , label = '5th User\'s F', linewidth = 1.5,  markeredgewidth = 1.5, markerfacecolor = 'None', markersize = 13)
ax4.plot(x4, sum_F, 'k*-', label = 'Total F', linewidth = 1.0, markerfacecolor = 'None', markersize = 18)
ax4.plot(x4, dashed_line, 'k-.', label = '$F_{max}$', linewidth = 1.8)
ax4.set_xlabel('Unit Price', fontname='Arial', fontweight = 'bold', fontsize = 30)
ax4.set_ylabel('CPU Cycles (GHz)', fontname = 'Arial', fontweight = 'bold', fontsize = 30)
ax4.set_title('', fontname='Arial'
                           '', fontweight = 'bold', fontsize = 20)
for tick in ax4.get_xticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)
for tick in ax4.get_yticklabels():
    tick.set_fontname('Arial')
    tick.set_fontsize(25)

ax4.annotate('Total distributed CPU cycles become 8GHz \n when the unit price is 0.1444', fontname = 'Arial', fontsize =25, xy = (0.1444, 8), xytext = (0.125, 7), arrowprops = dict(width = 1, headwidth = 10, shrinkA = 0, facecolor = 'black'),  verticalalignment='top', ha = 'center')

fig4.legend(prop = {'family' : 'Arial', 'size':20}, loc = 'center right', bbox_to_anchor = (0.9, 0.5))


fig4.savefig('fig4-New.pdf')
'''
'''
fig3.savefig('fig3-New.pdf')
'''