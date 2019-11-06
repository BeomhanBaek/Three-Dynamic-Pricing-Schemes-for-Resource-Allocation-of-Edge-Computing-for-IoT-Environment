class Manager2:
    def __init__(self, Fmax, users):
        self.users = users
        self.Fmax = Fmax
        self.unit_price = 0
        self.num_users = len(users)

    def solve(self):
        sum = 0
        for user in self.users:
            sum += (user.R*user.C/user.mu)**0.5
        self.unit_price = sum**2/self.Fmax**2

        for user in self.users:
            user.w = (user.R*user.C*self.unit_price/user.mu)**0.5
            user.F = (user.R*user.C/user.mu/self.unit_price)**0.5
            user.set_utility(user.w)

    def print_info(self):
        print('unit price', self.unit_price)
        utility_total, revenue = 0, 0
        for user in self.users:
            utility_total += user.utility
            revenue += user.w
            print('F = ', user.F, 'w = ', user.w, 'utility = ', user.utility)

        print('utility_total ', utility_total)
        print('revenue ', revenue)
