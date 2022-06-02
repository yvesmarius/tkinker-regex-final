import json

uname=input('nom')
pwd=input('pwd')

# try:
#   try: #try parsing to dict
#     # dataform = str(response_json).strip("'<>() ").replace('\'', '\"')
#     # struct = json.loads(dataform)
#   except:

try:    
    with open('test-main/client_data.json','r') as f:
        data=json.load(f)     
    user_info={'uname':'pwd'}
           
except json.decoder.JSONDecodeError:
    print('erreur')
    user_info={'uname':'pwd','poids':'largeur'}
    with open('test-main/client_data.json','w') as f:
        data1=json.dump(user_info,f, indent=4)

    


# dictionary ={  
#     "name" : "sathiyajith",  
#     "rollno" : 56,  
#     "cgpa" : 8.6,  
#     "phonenumber" : "9976770500"
# }  
     
# with open("test-main/client_data.json", "w") as outfile:  
#     json.dump(dictionary, outfile)