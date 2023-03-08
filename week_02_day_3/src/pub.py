class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def has_drink(self, drink):
        if drink in self.drinks:
            return True

    def add_to_till(self, amount):
        self.till += amount


# if cust has money and pub has drink
