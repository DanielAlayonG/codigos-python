import json

person = {'name':'Daniel', 'age': '19', 'city':'bogota', 'titles':['Tecnologo en desarrollo informatico', 'Ingeniero de software']}

personJSON = json.dumps(person, indent = 4)

print(personJSON)


#Crear un archivo json a partir de un diccionario
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


#leer archivo json y guardarlo en un diccionario
with open('person.json', 'r') as file:
    person2 = json.load(file)

print(person2)