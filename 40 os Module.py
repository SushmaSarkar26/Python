#46 #harry
# It is Importent for create many folder and file within few second


# see harry's video
# google search os module in python


# Dont run this code

import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")


# rename
for i in range(0, 100):
     os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")



# which which folder in any folder
folders = os.listdir("data")

# print(folders)

for folder in folders:
    print(folder)   # folder in folder
    print(os.listdir(f"data/{folder}"))   # file in folder



# directory
print(os.getcwd())
os.chdir("/user")
print(os.getcwd())
