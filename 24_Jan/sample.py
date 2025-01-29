with open("txtpath.py", "r") as fh:
    content = fh.read()
    print(content)
        
#with open("1.txt", "w") as fh:
 #   fh.write("Welcome to devops class")
    
with open("1.txt", "r") as fh1:
    content1 = fh1.read()
    print(content1)

with open("1.txt", "a") as fh2:
    fh2.write("\n Have a great day")

with open("1.txt", "r") as fh3:
    print(fh3.read())
