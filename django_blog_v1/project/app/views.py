from django.shortcuts import render
import json
# Create your views here.


posts = {
    'data' : [ 
    ],
    "status" : "Quest",
    "failedLogin" : False
}
def getBlogData():
    posts['data'] = []
    with open("project/blogsDataset.json", "r+") as file:
        json_data = json.load(file)
        for  i in json_data['blogData']:
            posts['data'].append(i)






def index(request):
    getBlogData()
    return render(request,'posts.html',posts)



def login(request):
    with open("project/accounts.json", "r+") as file:
        json_data = json.load(file)
    
    if(request.POST):
        email= request.POST["email"]
        password = request.POST['password']
        for i in json_data['members']:
            if(i['email'] == email and i['password']== password):
                posts['status'] = "Member"
                return render(request,'posts.html',posts)
            else:
                posts['failedLogin'] = True  
                return render(request,'loginpage.html',posts) 
    else:
        posts['failedLogin'] = False
        return render(request,'loginpage.html',posts)         
    

def about(request):
    return render(request,'about.html',posts)

def contact(request):
    return render(request,'contact.html',posts)

def post(request,title):
    getBlogData()
    jsonData = posts['data']

    post = {}
    for i in jsonData:
        if(title in i['title']):
            post = i
            print(i['blogParts'])
            break
    postData = {'post' : post}
    
    return render(request,'post.html',postData)