from mobile_tech import Mobile
from laptop_tech import Laptop
from tech_product import Tech
from sales_person import SalesPerson
from datetime import date

phone1 = Mobile('Iphone 11', 60000, 500, 'Black', '1920-1080', 10)
phone2 = Mobile('Iphone 12', 70000, 600, 'Red', '1920-1080', 15)
phone3 = Mobile('Iphone 12 Pro Max', 90000, 700, 'Green', '1920-1080', 20)

laptop_1 = Laptop('Assus', 125000, 2.5, 'Black', 12, 'i5', 1024)
laptop_2 = Laptop('Dell', 100000, 1.5, 'Blue', 8, 'i7', 896)

# Test Methods

# print(phone1)
# print(laptop_1)

# Applying Discount upon the Product

# phone1.apply_discount()
# print(phone1)


# Total Number of Products

# print(Tech.get_total_product())

# Shipping Cost

# print(laptop_1.shipping_cost(10))


# Setting the Double price for the 1st Laptop

# print(laptop_1.price)
# laptop_1.set_double_price()
# print(laptop_1.price)


# Changes Specs for a Laptop

# print(laptop_2)
# laptop_1.change_specs(55, 1500)
# print(laptop_2)


# Adding the Products

sales_person1 = SalesPerson(

    'Maksud Hossain',
    'Pranto',
    20000,
    date(2021, 1, 5)
)

sales_person1.sell_product(phone1)
sales_person1.sell_product(phone2)
sales_person1.sell_product(phone3)

print(sales_person1.calculate_commission(0.2))
sales_person1.sort_by_price()

