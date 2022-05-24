import json
def inscription(user_name,pass_word):
       
    with open('data_user.json','r',) as f:
        data=json.load(f)      
        data_user={user_name:pass_word}
        data_user[user_name]=pass_word
        data.update(data_user)
        print("chargement............")
        print("compte crée avec success")
    with open('data_user.json','w',) as f:
        data1=json.dump(data,f,indent=4)
