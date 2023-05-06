from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
import MySQLdb
import json
from datetime import datetime

blog = {}
startboostrap = 'Start Bootstrap'
posttime =  datetime.today().strftime('%Y-%m-%d %H:%M:%S')
textAreaNum = 1
titleNum = 1

def admin(request):
    return render(request,'createBlog.html')
 
blogParts = []

def sendBlog(request):
    if(request.POST):
        blog.update({'startboostrap' : startboostrap})
        blog.update({'posttime' : posttime})
        for key, value in request.POST.items():
           
            if("blogTitle" in key):
                print(key)
                addTitle = { "title": value }
                blog.update(addTitle)
            if("blogSubtitle" in key):
                print(key)
                addSubitle = { "subtitle": value }
                blog.update(addSubitle)
            if("header" in key):
                print(key)
                addHeader = { "header": value }
                blogParts.append(addHeader)
                blog.update(addHeader)
            if("textArea" in key):
                print(key)
                addTextArea = { "textArea": value }
                blogParts[-1].update(addTextArea)
                blog.update(addTextArea)        
            
           
        
        blog.update({"blogParts" : blogParts})      
        saveBlogData(blog)
       
    return render(request,'loginpage.html')


def saveBlogData(blogData):
    with open("project/blogsDataset.json", "r+") as file:
        json_data = json.load(file)
        json_data["blogData"].append(blogData)
        file.seek(0)
        json.dump(json_data, file, indent = 4)
        
# Create your views here.
