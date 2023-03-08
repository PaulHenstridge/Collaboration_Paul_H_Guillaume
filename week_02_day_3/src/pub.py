class Pub:
    def __init__(self, name, till, drinks, inventory):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.inventory = inventory

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

    def update_inventory(self, food):
        self.inventory[food.name] -= 1

    def sell_a_drink(self, customer, drink):
        if (
            customer.can_pay(drink.price)
            and self.customer_is_old_enough(customer)
            and self.customer_is_not_wasted(customer)
        ):
            customer.reduce_wallet(drink.price)
            self.add_to_till(drink.price)

    def sell_food(self, customer, food):
        if customer.can_pay(food.price):
            customer.reduce_wallet(food.price)
            self.add_to_till(food.price)
            customer.rejuvinate(food)
            self.update_inventory(food)
