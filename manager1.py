from scipy.optimize import minimize
import numpy as np

class Manager1:
    def __init__(self, Fmax, users):
        self.users = users
        self.Fmax = Fmax
        self.unit_price = 0
        self.num_users = len(users)

    def initialize(self):
        self.unit_price = 0

    def solve(self):

        F=[]
        for k in range(self.num_users):
            F.append(100)

        def objective(F):
            sum = 0
            for k in range(self.num_users):
                sum += (-self.users[k].R*self.users[k].C/F[k]+self.users[k].R*self.users[k].C/self.Fmax-self.users[k].R*self.users[k].C/self.Fmax*np.log(F[k]))/self.users[k].mu
            return -sum

        def constraint(F):
            return self.Fmax - sum(F)
        const = {'type':'ineq', 'fun':constraint}


        def const_function(i):
            return lambda F: F[i]
        constraints = [const_function(i) for i in range(self.num_users)]
        consts = []
        for i in range(self.num_users):
            consts.append({'type':'ineq', 'fun':constraints[i]})

        cons = ([const]+consts)

        b = (0.0, self.Fmax)
        bnds = [b]*self.num_users

        solution = minimize(objective, F, bounds = tuple(bnds), constraints = cons)
        F = solution.x

        sum2 = 0
        for i in range(self.num_users):
            sum2 += self.users[i].R*self.users[i].C*(self.Fmax-F[i])/self.users[i].mu/self.Fmax/F[i]/F[i]
        self.unit_price = sum2 / self.num_users

        for i in range(self.num_users):
            self.users[i].F = F[i]
            self.users[i].w = F[i]*self.unit_price
            self.users[i].set_utility(self.users[i].w)

    def print_info(self):
        utility_total, revenue = 0, 0
        for user in self.users:
            utility_total += user.utility
            revenue += user.w
            print('F = ', user.F, 'w=', user.w, 'utility=', user.utility)

        w_theoretical = [0 for i in range(self.num_users)]
        for i in range(self.num_users):
            w_theoretical[i] = (-self.users[i].R * self.users[i].C + (
                    self.users[i].R ** 2 * self.users[i].C ** 2 + 4 * self.users[i].mu * self.users[i].Fmax ** 2 *
                    self.users[i].R * self.users[i].C * self.unit_price) ** 0.5) / (
                                       2 * self.users[i].mu * self.users[i].Fmax)
        print('w_theoretical', w_theoretical)
        print('utility_total', utility_total)
        print('revenue ', revenue)
        print('unit price ', self.unit_price)







