from pathlib import Path

import magic

path = Path.home() / "PythonAutomationProject1" / "pythonProject"

magic_instance = magic.Magic(mime=True)
# A pretty cool way of iterating over a directory
for item in path.iterdir():
    if item.is_file():
        print(item.name, "is a file")
        print(magic_instance.from_file(item))
        # accessing the file type by what it ends with, doesn't actually look at what type the file is
        print(item.suffix)
    elif item.is_dir():
        print(item.name, "is a directory")
    else:
        print(item, "is not a file nor a directory")
