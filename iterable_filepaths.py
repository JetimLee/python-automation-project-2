from datetime import datetime
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
        stats = item.stat()
        # get the size and last time it was modified
        print("Size: ", stats.st_size)
        # Goes from January 3rd, 1970
        print("Last time modified: ", stats.st_mtime)
        print(
            "Last time modified human readable", datetime.fromtimestamp(stats.st_mtime)
        )
        print(item.suffix)

    elif item.is_dir():
        print(item.name, "is a directory")
    if "read" in item.name.lower():
        print(item.name, "contains the word read")
