from pathlib import Path

path = Path.home() / "PythonAutomationProject1" / "pythonProject"

# A pretty cool way of iterating over a directory
for item in path.iterdir():
    print(item)
