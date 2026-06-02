# listas
nomes = []

nomes.append("Vitor")
nomes.append("Neto")
nomes.append("Gustavo")

print(nomes) # é listado de maneira geral em formato de lista

print(nomes[0]) # é listado apenas para Vitor
print(nomes[1]) # é listado apenas para Neto
print(nomes[2]) # é listado apenas para Carecudo gustavinhu

print("-----------------")

for sena in nomes:
    print("O nome da pessoa é :", sena)

nomes.remove("Gustavo") # excluir item pelo valor

for sena in nomes:
    print("O nome da pessoa é :", sena)

del nomes[1] # excluir item pelo indice

for sena in nomes:
    print("O nome da pessoa é : ", sena)
