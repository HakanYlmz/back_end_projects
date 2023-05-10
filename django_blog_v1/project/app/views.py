from django.shortcuts import render
import json
import os
from dotenv import load_dotenv
from django.conf import settings
from django.core.mail import send_mail


load_dotenv()
# Create your views here.

#Uygulama içerisinde kullandığım veri yarpısı
posts = {
    'data' : [ 
    ],
    "status" : "Quest",
    "failedLogin" : False
}

#Veri seti olarak kullandığım Json dosyasındaki verileri almak için kullanılır
def getBlogData():
    posts['data'] = []
    with open("project/blogsDataset.json", "r+") as file:
        json_data = json.load(file)
        for  sectionData in json_data['blogData']:
            posts['data'].append(sectionData)





#index saydasındaki fonksiyonunu
def index(request):
    getBlogData()
    return render(request,'posts.html',posts)


#login sayfası işlemleri
def login(request):
    with open("project/accounts.json", "r+") as file:
        json_data = json.load(file)
    #kullanıcı denetimi gerçekleştirilmesi
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
    
#About sayfası işlemleri
def about(request):
    return render(request,'about.html',posts)
#Contact sayfası işlemleri
def contact(request):
    if request.POST:
        target_email = os.environ['targetEmail']
        subject = "Contact Mail"
        message = request.POST['name'] +"\n" + request.POST['email'] + "\n" +request.POST['message']
        from_email = os.environ['email']
        send_mail(subject,message,from_email,[target_email] )
        return render(request,'contact.html',posts)
    else :
        return render(request,'contact.html',posts)

#Post sayisindaki işlemler için kullandığımız
def post(request,key):
    #Uygulama içerisinde veriseti güncelleştirir
    getBlogData()
    jsonData = posts['data']
    post = {}
    order = []
    for i in jsonData:
        if(i['key'] == key):
            post = i
            break
    postData = {'post' : post}
    
    for key, value in post.items():
        order.append(value)
    print(order)
    
    return render(request,'post.html',postData)