from powerset import PowersetList

class Manager3:
    def __init__(self, Fmax, users, f):
        self.Fmax = Fmax
        self.users = users
        self.unit_price = [0, 0]
        self.num_users = len(users)
        self.fairness = f
        self.coefficients = []
        for user in users:
            self.coefficients.append((user.R*user.C/user.mu)**0.5)
        self.index_sol = []
        self.alpha, self.beta = 0, 0

    def solve(self):
        gamma = sum(self.coefficients)/2
        index = range(self.num_users)
        index_Powerset = PowersetList(index)
        index_sol = []
        diff = gamma
        for elem in index_Powerset:
            sum1 = 0
            for k in elem:
                sum1 += self.coefficients[k]
            if diff > abs(gamma-sum1):
                index_sol = elem
                diff = abs(gamma-sum1)
        self.index_sol = index_sol
        for i in index_sol:
            self.alpha += self.coefficients[i]
        self.beta = 2*gamma - self.alpha

        self.unit_price[0] = ((self.alpha + self.beta*self.fairness**0.5)/self.Fmax) ** 2
        self.unit_price[1] = ((self.alpha + self.beta*self.fairness**0.5)/self.fairness**0.5/self.Fmax) ** 2

        for i in range(self.num_users):
            if i in index_sol:
                self.users[i].w = (self.users[i].R*self.users[i].C*self.unit_price[0]/self.users[i].mu) ** 0.5
                self.users[i].F = self.users[i].w / self.unit_price[0]
                self.users[i].set_utility(self.users[i].w)
            else:
                self.users[i].w = (self.users[i].R * self.users[i].C * self.unit_price[1] / self.users[i].mu) ** 0.5
                self.users[i].F = self.users[i].w / self.unit_price[1]
                self.users[i].set_utility(self.users[i].w)

    def print_info(self):
        print('unit price', self.unit_price)
        utility_total, revenue = 0, 0
        for user in self.users:
            utility_total += user.utility
            revenue += user.w
            print('F = ', user.F, 'w = ', user.w, 'utility = ', user.utility)

        print('utility_total ', utility_total)
        print('revenue ', revenue)
        print('revenue theoretical', (self.alpha **2 + self.beta ** 2 + (self.fairness**0.5+self.fairness ** (-0.5))*self.alpha*self.beta)/self.Fmax)
        print('theoretical revenue difference between 2 & 3', (self.fairness ** 0.5 + self.fairness ** (-0.5)-2)*self.alpha*self.beta/self.Fmax)
        print('index sol', self.index_sol)





