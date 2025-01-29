my_list = [12,21,32,"Harish", "Kedhar", "Devops", 59]

my_dict = {
        "name": "Kedhar",
        "age" : 29,
        "city": "Hyderabad"
        }

if "Kedhar" in my_list:
    print("Element is found")
else:
    print("Element not found")

if my_list:
    print("List contains values")
else:
    print("Empty")

my_list1 = []

if my_list1:
    print("List contains values")
else:
    print("Empty")

if "name" in my_dict:
    print("Key found")
else:
    print("Key not found")

if "name" in my_dict.values():
    print("Value found")
else:
    print("Value not found")


if my_dict["name"] == "Kedhar":
    print("The Key contain the specific value")
else:
    print("The key doesnt contaithe specific value")


found = True
if not found:
    print("The value is True")
else:
    print("False")


if my_dict:
    print("Dictionary is not empty")
else:
    print("The Ditionary is empty")
