mydict1={"name": "Kedharnadh", "ID": 1, "domain": [10,40,"Kedhar", "Devops", "Cloud Engineer","SRE"],
         "tools": {"os": ["Linux","cloud"], "cloud": "AWS"},"sample": {"value":"Command"}}
print(mydict1)
a=mydict1["name"]
print(a)

print(mydict1["ID"])

print(mydict1["domain"])

print(mydict1["domain"][2])

print(mydict1["tools"])
print(mydict1["tools"]["os"])

print(mydict1["tools"]["os"][0])

print(mydict1["sample"]["value"])

mydict1["place"]=["bangalore", "pune"]
print(mydict1)

mydict2={
        "name1": "KedharnadhAduri"
        }

mydict1.update(mydict2)

print(mydict1)
