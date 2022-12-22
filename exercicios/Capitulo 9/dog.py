class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + ' rolou!')
    def rolling(self):
        print(self.name.title() + ' sentou!')
    
my_dog = Dog('Willian', 6)

print('o nome do meu cachorro é ' + my_dog.name.title())
my_dog.sit()