import pandas as pd
import json

"""
def check_str(x):
    if isinstance(x, str):
        x.strip()
    else:
        x
"""        

def read_excel_content(excel_file_path, json_file_path):
   data= pd.read_excel(excel_file_path, sheet_name="Sheet1")
   #print(data)
   data1=data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
   data1.to_json(json_file_path, orient='records', indent=4)
   print("Excel file converted into the Json format")
#print(dir(pd))

excel_file_path="/home/ubuntu/Python/28_jan/sample.xlsx"

json_file_path="1.json"
read_excel_content(excel_file_path, json_file_path)
