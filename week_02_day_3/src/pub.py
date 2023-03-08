
class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    # def has_drink(self, drink):
    #     if drink.name in self.drinks:
    #         return True

    def add_to_till(self, amount):
        self.till += amount

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink


# if cust has money and pub has drink
