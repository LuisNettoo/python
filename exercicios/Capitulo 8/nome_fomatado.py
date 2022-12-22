import re


def nome_formatado(primeiro_nome, ultimo_nome):
    nome_completo = primeiro_nome + ' ' + ultimo_nome
    return nome_completo.title()

musician = nome_formatado('jimi', 'hendrix')

print(musician)
