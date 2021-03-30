# Nicolas Campero
# 1856853

class ItemToPurchase:

    def __init__(self, name_item = 'none', price_item = 0, quantity = 0):
        self.name_item = name_item
        self.price_item = price_item
        self.quantity = quantity
    def print_item_cost(self):
        self.name_item = str(input())
        self.price_item = float(input())
        self.quantity = int(float())
        price = self.quantity * self.price_item
        print('{} {} @ ${} = {}'.format(self.name_item, self.quantity, self.price_item, price))

items = ItemToPurchase()

