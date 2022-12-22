class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('O nome do restaurante é ' + self.restaurant_name.title(), end=' ')
        print('e seu tipo é ' + self.cuisine_type.title())
    
    def open_restaurant(self):
        print(f'O restaurante {self.restaurant_name.title()} está aberto!')

my_restaurant = Restaurant('mais sabor', 'hamburgueria')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
