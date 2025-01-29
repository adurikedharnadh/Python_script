import random

import sys

import os

print(random.randint(2, 5))

for i in range(2,5):
  print(i)

print(sys.argv[0])
#print(sys.exit())

print(sys.argv[1])
print(sys.path)  

os.chdir("/home/ubuntu")

os.makedirs("dirnew1234", exist_ok=True)
print(os.getcwd())

print(os.listdir("/home/ubuntu"))

for path, dir, files in os.walk("/home/ubuntu/dir1"):
  #  print(path, dir, files)
    print(files)


