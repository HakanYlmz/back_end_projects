from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
import MySQLdb
import json
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import uuid

#Admin panelinde oluturulan default değerler ve yapıların oluşturulması
blog = {}
startboostrap = 'Start Bootstrap'
posttime =  datetime.today().strftime('%Y-%m-%d %H:%M:%S')
textAreaNum = 1
titleNum = 1

#admin paneli blog oluşturma sayfasıyla karşılanır
def admin(request):
    return render(request,'createBlog.html')

blogParts = []

denemePart = {}

def sendBlog(request):
    if(request.POST):
        denemePart.update({"key" : uuid.uuid4()})
        for key,value in request.POST.items():
            denemePart.update({key: value})
        for key,value in request.FILES.items():
            denemePart.update({key : value.name})
            handle_uploaded_file(value,value.name)

        print(denemePart)
        for key,value in denemePart.items():
            print(key+ " " + value)
        
        saveBlogData(denemePart)

        '''
        blog.update({'startboostrap' : startboostrap})
        blog.update({'posttime' : posttime})
        #Blog yapısındaki default değerler atandıktan sonra sözlük yapısın oluşturulur
        
        for key , value in request.FILES.items():
            handle_uploaded_file(value,key)

        for key, value in request.POST.items():
           #Blog title ve blogSubtitle her Blog yapısında bir tane oluşur
            if("blogTitle" in key):
                addTitle = { "title": value }
                blog.update(addTitle)
            if("blogSubtitle" in key):     
                addSubitle = { "subtitle": value }
                blog.update(addSubitle)
                #header ve textArea sayıları değişken olmakla beraber header parçalarına text Alanları atanır
            if("header" in key): 
                addHeader = { "header": value }
                blogParts.append(addHeader)
                blog.update(addHeader)
            if("textArea" in key):
                addTextArea = { "textArea": value }
                blogParts[-1].update(addTextArea)
                blog.update(addTextArea)
                  
            
           
        blog.update({"blogParts" : blogParts})      
        saveBlogData(blog)
      '''
        
       
    return render(request,'loginpage.html')

#Blog veri yapısı verisetine eklenir
def saveBlogData(blogData):
    with open("project/blogsDataset.json", "r+") as file:
        json_data = json.load(file)
        json_data["blogData"].append(blogData)
        file.seek(0)
        json.dump(json_data, file, indent = 4)
        
# Create your views here.

def handle_uploaded_file(f,key):
    fss = FileSystemStorage()
    file = fss.save(f.name,f)

