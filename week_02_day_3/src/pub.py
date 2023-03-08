class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def has_drink(self, drink):
        if drink in self.drinks:
            return drink