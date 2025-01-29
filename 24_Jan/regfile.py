import re

email_data="Kedhar <adurikedharnadh@gmail.com>,$kedhar <$kedharnadh.aduri@gmail.com> ,kedharnadh <kedharnadh.aduri@gmail.com>, phaNinandigam <phaniNandigam@gmail.com>, Harish <Harish@gmail.com>"

result=re.search(r"phani", email_data)
print(result)

result=re.search(r"kedhar", email_data)
print(result)

result=re.search(r"Kedhar", email_data)
print(result)

result=re.findall(r"pha", email_data)
print(result)

result=re.search(r"suresh", email_data)
print(result)

result=re.search(r"pha[o,i,n]", email_data)
print(result)

result=re.search(r"pha[a-z]{2}", email_data)
print(result)

result=re.search(r"pha[a-z]+", email_data)
print(result)

result=re.search(r"pha[a-z,A-Z]+", email_data)
print(result)

result=re.search(r"[a-zA-Z0-9_]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)


#email_data = "PhaniNandigam <PhaniNandigam@gmail.com> "

result=re.search(r"[a-zA-Z0-9_@.]+", email_data)
print(result)


print("-------------------")
result=re.findall(r"[a-zA-Z0-9_@.]+", email_data)
print(result)

print("---------------------------.operator")
result=re.findall(r"[a-zA-Z0-9_.]+@[A-Za-z0-9]+\.[a-z]+", email_data)
print(result)

print("---------------------------\w")
result=re.findall(r"[\w]+@[\w]+\.[\w]+", email_data)
print(result)




result= re.findall(r"\w+[@]+\w+[.]+\w+", email_data)
print(result)


print("------with \w and . -------")
result=re.findall(r"[\w.]+@[\w]+\.[\w]+", email_data)
print(result)


print("------with capital \W and . -------")
result=re.findall(r"[\W.]+@[\w]+\.[\w]+", email_data)
print(result)
