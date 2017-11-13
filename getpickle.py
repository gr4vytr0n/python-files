import pickle
with open('entry2.pickle', 'rb') as f:
  entry = pickle.load(f)

print(entry)