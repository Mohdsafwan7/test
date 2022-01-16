import re
pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$!]).*$"
password = input ("Enter the password: ")
result = re.findall(pattern,password)
if(result):
    print ("Valid")
else:
    print("invalid",result)