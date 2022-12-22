age = int(input('Qual sua idade? '))

if age < 4:
    print('A sua entrada é gratuita!')
elif 4 <= age < 18:
    print('A sua entrada custa 5 dólares!')
else:
    print('A sua entrada custa 10 dólares!')