motorcycles = ['honda', 'yamaha', 'suzuki']

# Para acresentar itens na lista use o metodo "append()"

new = str(input('Digite o novo item na lista: '))
motorcycles.append(new)

print(motorcycles)

# Para remover itens da lista, use a instrução del

del motorcycles[0]

print(motorcycles)

# O metodo remove() serve para remover um item da lista usando seu valor como string

motorcycles.remove('yamaha')

print(motorcycles)


