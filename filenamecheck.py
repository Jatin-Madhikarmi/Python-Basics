import os
from pathlib import Path

file=input("Enter the filename : ")
extension=os.path.splitext(file)[1]
file_path=Path(file)

if file.lower().endswith('.txt'):
    print("Yes, the correct format is provided")
else:
    print("No, the incoreect format is provided")

if extension.lower()=='.txt':
    print("Yes, the correct format is provided")
else:
    print("No, the incoreect format is provided")

if file_path.suffix.lower() == '.txt':
    print("Yes, the correct format is provided")
else:
    print("No, the incoreect format is provided")

path=Path('/documents/files/report.txt')

print(path)
print(path.stem)
print(path.suffix)
print(path.name)
print(path.parent)
print(path.is_dir())