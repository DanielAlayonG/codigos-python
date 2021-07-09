fruits =  [
    {'name': 'apple', 'price': 20},
    {'name': 'avocado', 'price': 20},
    {'name': 'orange', 'price': 20}
]

fruit_names = [fruit['name'] for fruit in fruits]
print(fruit_names)