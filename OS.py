import os

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
