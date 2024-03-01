# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, this is a sample text.')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()

print("File Content:", content)
