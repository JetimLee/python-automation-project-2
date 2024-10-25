from pathlib import Path

p = Path(".")

print(p, "is the current working directory")

home = Path.home()


print("The home directory is", home)
