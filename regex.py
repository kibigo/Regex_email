import re


#UserId@domainname.ext

pattern = "^[a-z A-Z 0-9 .]+@[a-z A-Z]+\.[a-z A-Z]{2,3}$"

sample = input("Enter your email: ")

if re.search(pattern, sample):
    print(f"{sample} is valid")

else:
    print(f"{sample} is not valid")