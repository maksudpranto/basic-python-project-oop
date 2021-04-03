from tech_product import Tech


class Mobile(Tech):
    def __init__(self, name, price, weight, color, screen, camera):
        super().__init__(name, price, weight, color)
        self.screen = screen
        self.camera = camera

    def apply_discount(self):
        self.price = self.price - self.price * (super().discount / 2)

    def __str__(self):
        return f'Name is {self.name}\n Price is {self.price}\n Weight is {self.weight}\n' \
               f'Color is {self.color}\n Screen {self.screen}\n Camera {self.camera}'
