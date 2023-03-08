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

    def customer_is_old_enough(self, customer):
        return customer.age >= 18

    def customer_is_not_wasted(self, customer):
        return customer.drunkenness < 12

    def sell_a_drink(self, customer, drink):
        if (
            customer.can_pay_for_drink(drink.price)
            and self.customer_is_old_enough(customer)
            and self.customer_is_not_wasted(customer)
        ):
            customer.reduce_wallet(drink.price)
            self.add_to_till(drink.price)
