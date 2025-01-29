import os

for root, dir, files in os.walk("/home/ubuntu"):
    for file in files:
        if file.endswith(".txt"):
            print(f"The test files available are:{root}/{file}")
