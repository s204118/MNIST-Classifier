import pickle

with open('mnist.pkl.gz', 'rb') as f:
    data = pickle.load(f)