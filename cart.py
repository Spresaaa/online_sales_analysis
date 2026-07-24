class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def show_cart(self):
        for product, quantity in self.items:
            print(f"{product.name} - {quantity} pcs")