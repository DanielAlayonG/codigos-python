from collections import Counter

a = 'aaaaaaabbbcccc'


#Los counter tienen comparten funciones con las tuplas
cantidad_de_caracteres = Counter(a)

caracter_mas_comun = Counter(a).most_common(1)[0][0]

print(cantidad_de_caracteres)
print(caracter_mas_comun)