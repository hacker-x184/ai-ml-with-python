import os
with open("demo.txt", "r") as f:
    data =f.read()
    print(data)
# For removing command
os.remove("heloo.txt")
