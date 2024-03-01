my_dict = {'name': 'John', 'age': 25}

# Add item
my_dict['city'] = 'New York'

# Search for an item
age = my_dict.get('age', 'Age not found')

print("Updated Dictionary:", my_dict)
print("Age:", age)
