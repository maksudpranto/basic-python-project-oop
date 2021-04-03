class Tech:
    total_products = 0
    discount = 0.5

    def __init__(self, name, price, weight, color):
        self.name = name
        self.price = price
        self.weight = weight
        self.color = color
        Tech.total_products += 1

    def apply_discount(self):
        self.price = int(self.price - self.price * Tech.discount)

    def shipping_cost(self, rate):
        return f'Shipping Cost will be {self.weight * rate}'

    @classmethod
    def get_total_product(cls):
        return 'Total Products : ' + str(cls.total_products)
