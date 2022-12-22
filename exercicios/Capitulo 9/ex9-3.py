class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f'O seu primeiro nome é {self.first_name.title()}', end=' ')
        
        if len(self.last_name) == 3:
            print(f'e seu ultimo nome é {self.last_name.upper()}')
        else:
            print(f'e seu ultimo nome é {self.last_name.title()}')
    
    def greet_user(self):
        print(f'Bem vindo de volta {self.first_name.title()} {self.last_name.title()}')

    def user_name(self):
        user = self.last_name + '.' + self.first_name
        print(user)

adm_user = User('luis', 'neto')
normal_user = User('leo', 'agf')
any_user = User('samuel', 'ssn')

adm_user.user_name()
adm_user.describe_user()

normal_user.describe_user()
normal_user.user_name()

any_user.describe_user()