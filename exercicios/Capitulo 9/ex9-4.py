class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print('O nome do restaurante é ' + self.restaurant_name.title(), end=' ')
        print('e seu tipo é ' + self.cuisine_type.title())
    
    def open_restaurant(self):
        print(f'O restaurante {self.restaurant_name.title()} está aberto!')

    def set_number_served(self):
        self.number_served = 15

new_restaurant = Restaurant('mais sabor', 'hamburguer')
new_restaurant.set_number_served()
print(new_restaurant.number_served)