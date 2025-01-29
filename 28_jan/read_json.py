import json
import sys
import requests
import tarfile 

with open("1.json", "r") as fh:
    json_data=json.load(fh)
   # print(json_data)

"""
for ele in json_data:
    for key, value in ele.items():
        print(ele["Source URL"])
        #print(key)
        #print(value)
        print("----------")
    #print(ele)
    sys.exit()
"""
file_path="/home/ubuntu/Python/28_jan/behave.tar.gz"

for ele in json_data:
   # for key, value in ele.items():
   Source_url=ele["Source URL"]
   response = requests.get(Source_url)
   #response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
   with open(file_path, 'wb') as file:
      file.write(response.content)
   print("Tar file downloaded successfully.")
   print(Source_url)
        #print(key)
        #print(value)
    #print("----------")
    #print(ele)
   #sys.exit()
   break

file = tarfile.open('/home/ubuntu/Python/28_jan/behave.tar.gz') 
  
# extracting file 
file.extractall('/home/ubuntu/Python/28_jan/') 
  
#file.close()    
