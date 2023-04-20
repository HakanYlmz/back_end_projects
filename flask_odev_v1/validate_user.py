import json



json_file_path = "acounts_info.json"
print("validate")
def initilize():
    with open(json_file_path, 'r') as j:
        data = json.loads(j.read())
        return data
def validate_member(email,password):
    data = initilize()
    members = data['members']
    for i in members:
        print(i)
        if i['email'] == email and i['password'] == password:
            return i['username']
    return "Login"



def add_member(username,email,password):
    member = {
        'username' :username,
        'email' : email,
        'password' : password
    }
    data = initilize()
    data['members'].append(member)
    with open("acounts_info.json",'w+') as f:
        json.dump(data,f)
       

add_member("dsa","dsa","fsa")