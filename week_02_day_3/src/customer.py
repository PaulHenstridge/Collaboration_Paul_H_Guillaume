class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def can_pay(self, amount):
        return self.wallet > amount

    def rejuvinate(self, food):
        self.drunkenness -= food.rejuvination
