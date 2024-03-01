import pickle

data = {'name': 'Alice', 'age': 30}

# Writing to a file using pickle
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Reading from a file using pickle
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("Loaded Data:", loaded_data)
