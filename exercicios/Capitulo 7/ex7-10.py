travel_dream = {}

flag = True

while flag:
    
    name = input("Digite seu nome: ")
    travel = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
    # Adiciona o valor na chave
    travel_dream[name] = travel
    
    repeat = input("Alguma outra pessoa vai responder o questionario? (sim/nao) ")
    # Se o usuário responder nao o programa termina
    if repeat == 'nao':
        flag = False

print("Obrigado por responder o formulario!")

# Laço que mostra todos os nomes e lugares que os usuários gostariam de ir
for key, value in travel_dream.items():
    print("{} gostaria de visitar o(a) {}.".format(key.title(), value.title()))
