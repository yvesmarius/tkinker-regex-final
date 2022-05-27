import re

regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")



def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

isValid("name.surname@gmail.com")
isValid("anonymous123@yahoo.co.uk")
isValid("anonymous123@...uk")
isValid("K...a...23225@")
isValid("rdfsfqdgdjgidjgisdfigsodjgigdjgieorepoghrogrhgoeirhgieo@r.yves.co")

test_str1=input('entrez text')
if(not test_str1.strip()): 
    print ("Yes") 
else : 
    print ("No")