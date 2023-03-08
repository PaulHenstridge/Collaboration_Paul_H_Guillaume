class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def can_pay_for_drink(self, amount):
        return self.wallet > amount
