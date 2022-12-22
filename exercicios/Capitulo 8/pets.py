pets = {'dog': 'willie', 'hamester': 'harry'}

def describe_pet(pet, name):
        print("\nI have a {}!".format(pet))
        print("My {}'s name is {}.".format(pet, name))


for pet, name in pets.items():
    describe_pet(pet, name)
