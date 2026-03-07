import os
from pathlib import Path

path="C:/Users/jatin/Downloads"
newdir=["config"]
newpath=os.path.join(path,*newdir)

if not(os.path.exists(newpath)):
    os.makedirs(newpath)
    print("New test file sucessfully created.\n")

else:
    print("The test file already exists.\n")

if os.path.isdir(newpath):
    print("YES")
else:
    print("NO")

if os.path.exists(path):
    print("Yes it exitst")

else:
    print("No it doesn't exists")

brandnewpath=os.path.join(path,"hello")

if os.path.exists(brandnewpath):
    print(f"Yes the brandnewpath exists")
else:
    print("No the brandnewpath doesn't exists")


print(os.path.realpath("Downloads"))
print(os.path.abspath("Downloads"))

path="C:/Users/jatin/Downloads"
if os.listdir(path):
    print(f"The path already exists {path}")

else:
    print(f"The path doesn't exists {path}")

# for files in os.listdir(path):
#     print(files)

child=path
parent=os.path.realpath(os.path.join(child,'..'))
print(f"The child path is {child}")
print(f"The parent to the above child path is {parent}")

prefix=''
suffix="hello"
print(os.path.join(prefix,suffix))
print(os.path.join(suffix,prefix))
print(os.path.join(prefix,prefix))

file_path='C:/Users/jatin/Downloads/config/hello.docx'
file_path=os.path.realpath(file_path)

print(f"The python is currently looking at the directory {os.getcwd()}")
if os.path.exists(file_path): # To check whether the path exists or not 
    if not os.path.isdir(file_path): # To check whether it is a directory path or a file path
        print(f"Not a directory {file_path}")
    elif os.listdir(file_path): # To check if the directory already exists or not 
        print(f"The directory {file_path} is not empty")
else:
    print(f"No, the path {file_path} doesn't exists")

directory_path='C:/Users/jatin/Downloads'
print(directory_path)
directory_path=os.path.realpath(directory_path)
directory_file=Path(directory_path).name
print(directory_file)
