import os

path="C:/Users/jatin/Downloads"
newdir=["config"]
newpath=os.path.join(path,*newdir)

if not(os.path.exists(newpath)):
    os.makedirs(newpath)
    print("New test file sucessfully created.\n")

else:
    print("The test file already exists.\n")

