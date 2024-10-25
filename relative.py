import os

# Create the path dynamically
path = os.path.join("absolute_v_relative", "dad_jokes.txt")


with open(path, "r") as file:
    print(file.read())
