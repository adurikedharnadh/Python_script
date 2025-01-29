my_list = [22, 23, 56, 75, 82, 91, 109, 44, 28, 98]

print(f"The values inside the list are:{my_list}")


print("The even numbers mentioned in the list are:")
for val in my_list:
  
    if val % 2 == 0:
        print(val, end = " ")
print("\n")
