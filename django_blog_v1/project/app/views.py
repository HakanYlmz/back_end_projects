from django.shortcuts import render
import json
# Create your views here.


posts = {
    'data' : [ 
    ],
    'Statu' : "Quest"
}
def getBlogData():
    with open("project/denemeJsonfile.json", "r+") as file:
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
                posts['Statu'] = "Member"
                return render(request,'posts.html',posts)           
    return render(request,'loginpage.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def post(request,title):
    jsonData = posts['data']
    post = {}
    for i in jsonData:
        if(title in i['title']):
            post = i
            break
    postData = {'post' : post}
    return render(request,'post.html',postData)