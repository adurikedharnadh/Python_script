def display_content(filename):
    with open(filename, "r") as fh:
        content = fh.read()
        print(content)
    ab = "From function1"
    num = "From function2"
    return filename, ab, num


file_name = "1.txt"
ab= "testing"
num= "testing2"
var1, var2, var3 =display_content(file_name)

print(var1)
print(var2)
print(var3)
