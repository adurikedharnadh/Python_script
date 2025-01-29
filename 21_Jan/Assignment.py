mydict={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": ["iam:ChangePassword"],
      "Resource": "*"
    },
    {
      "Sid": "SecondStatement",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "ThirdStatement",
      "Effect": "Allow",
      "Action": [
        "s3:List*",
        "s3:Get*"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data",
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data/*"
      ],
      "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
    }
  ]
}


print(mydict["Version"])
print(mydict["Statement"][0]["Sid"])
print(mydict["Statement"][0]["Action"][0])
print(mydict["Statement"][0]["Resource"])

print(mydict["Statement"][1]["Sid"])
print(mydict["Statement"][1]["Action"][0])
print(mydict["Statement"][1]["Resource"])

print(mydict["Statement"][2]["Sid"])
print(mydict["Statement"][2]["Action"][0])
print(mydict["Statement"][2]["Action"][1])
print(mydict["Statement"][2]["Resource"])
print(mydict["Statement"][2]["Resource"][0])
print(mydict["Statement"][2]["Resource"][1])
print(mydict["Statement"][2]["Condition"])
print(mydict["Statement"][2]["Condition"]["Bool"])
print(mydict["Statement"][2]["Condition"]["Bool"]["aws:MultiFactorAuthPresent"])
