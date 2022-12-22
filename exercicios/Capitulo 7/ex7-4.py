prompt = "\nDigite os sabores que você quer na pizza: "
prompt += "\n(Digite 'quit' quando voce quiser parar de adicionar sabores.)"
prompt += "\n"

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print('O sabor {} foi adicionado a pizza!'.format(topping))
        