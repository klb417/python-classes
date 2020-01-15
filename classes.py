class Pizza:
    def __init__(self, size=8, crust="regular"):
        self.size = size
        self.crust = crust
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        print(
            f"You ordered a {self.size} inch {self.crust} with "
            + " and ".join(self.toppings)
            + "."
        )


new_pizza = Pizza(12, "thin crust")
new_pizza.add_topping("pepperoni")
new_pizza.add_topping("mushrooms")

new_pizza.print_order()
