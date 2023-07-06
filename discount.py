#Discount

class Discount:
    def __init__(self, discount_id, product_id, discount_percentage, start_date, end_date):
        self.discount_id = discount_id
        self.product_id = product_id
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    def apply_discount(self, price):
        if self.discount_percentage > 0:
            return price * (100 - self.discount_percentage) / 100
        else:
            return price

    def remove_discount(self, price):
        return price * (100 / 100)

    def check_validity(self, current_date):
        if current_date >= self.start_date and current_date <= self.end_date:
            return "The discount is valid"
        else:
            return "The discount is not valid"

discount = Discount(1, 123, 10, '2023-06-05', '2023-06-15')
price = 100
discounted_price = discount.apply_discount(price)
print(discounted_price)

removed_price=discount.remove_discount(price)
print(removed_price)
validity=discount.check_validity('2023-06-01')
print(validity)