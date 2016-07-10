import pickle

pickle_in = open("banner.p", "rb")
file_pickle = pickle.load(pickle_in)    # Move it from folder Resources to the current folder.

for line in file_pickle:
    for item in line:
        print(item[0] * item[1], end="")
    print()
