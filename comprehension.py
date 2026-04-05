# List comprehension
# set comprehension
# dict comprehension
# generator comprehension

quadrado=[x**2 for x in range(9)]
print(quadrado)

# criando uma lista de numeros pares entre 0 e 20

pares=[x for x in range(21) if x%2 ==0]
print(pares)


# cria um dicionario com numeros e seus quadrados

dicionarioquad={x: x**2 for x in range(5)}
print(dicionarioquad)

# set (conjunto) não permite duplicatas
quadrado_set={x**2 for x in [1,2,2,3,3,4]}
print(quadrado_set)

