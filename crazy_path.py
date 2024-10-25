from pathlib import Path

crazy_path = Path.home() / "I" / "dont" / "exist.csv"

print(crazy_path)

if crazy_path.exists():
    with open(crazy_path, "r") as file:
        print(file.read())  # This will error because no such directory/file exists
else:
    print("Path does not exist")
