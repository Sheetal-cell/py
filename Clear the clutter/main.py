import os
def clutter(files,dir,a):
    count=1
    for file in files:
        if file.endswith(a):
            new_name = str(count) + a
            os.rename(os.path.join(dir, file), os.path.join(dir, new_name))
            count+=1
            

dir=input("Enter Directory Of Files:")
files=os.listdir(dir)
a=input("Enter Your File Type:")
clutter(files,dir,a)
