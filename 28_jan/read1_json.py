import json
import sys
import requests
import tarfile
import zipfile 

with open("2.json", "r") as fh1:
    json_data1=json.load(fh1)
   # print(json_data)

file_path="/home/ubuntu/Python/28_jan/apache-tomcat-9.0.98.zip"

for ele in json_data1:
   Source_url=ele["Source URL"]
   response = requests.get(Source_url)
   with open(file_path, 'wb') as file:
      file.write(response.content)
   print("ZIP file downloaded successfully")
   print(Source_url)
   
   with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(path="/home/ubuntu/Python/28_jan/")

   print("ZIP file extracted successfully.")
   break

