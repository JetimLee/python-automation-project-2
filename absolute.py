import os

# Define the base directory (absolute path to the project folder)
base_dir = "/Users/gavincoulson/PythonAutomationProject1/pythonProject"

# Construct the absolute path to the dad_jokes.txt file
file_path = os.path.join(base_dir, "absolute_v_relative", "dad_jokes.txt")

# Open and read the file
with open(file_path, "r") as file:
    dad_jokes = file.read()

# Print the content of the file
print(dad_jokes)
