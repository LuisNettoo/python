responses = {}

responses_active = True

while responses_active:
    name = input("Qual o seu nome? ")
    response = input("\nQual montanha russa você gostaria de andar? ")
    repeat = input("Você gostaria de dar outra resposta? (sim/nao) ")
    if repeat == 'nao' or 'não':
        responses_active = False
    
