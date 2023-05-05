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
 
def get_people(request):
    db = MySQLdb.connect(user='root', db='blog', passwd='aslan076', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM persons;')
    names = [row for row in cursor.fetchall()]
    print(names[0])
    print("hjk")
    db.close()
    return HttpResponse("get peaople")

def sendBlog(request):
    print("get Blog")
    if(request.POST):
        print("post")
        blog.update({'startboostrap' : startboostrap})
        blog.update({'posttime' : posttime})
        for key, value in request.POST.items():
            if("header" in key):
                print(value)
                print(key)
                addHeader = { "title": value }
                blog.update(addHeader)
               

            if("textArea" in key):
                print(value)
                print(key)
                addTextArea = { "textArea": value }
                blog.update(addTextArea)
                

            if("title" in key):
                addTitle = { "header": value }
                blog.update(addTitle)
            if("blogSubtitle" in key):
                addSubitle = { "subtitle": value }
                blog.update(addSubitle)
        
                
        saveBlogData(blog)
    print(blog)            
    return HttpResponse("alindi")


def saveBlogData(blogData):
    with open("project/blogsDataset.json", "r+") as file:
        json_data = json.load(file)
        json_data["blogData"].append(blogData)
        file.seek(0)
        json.dump(json_data, file, indent = 4)
        
# Create your views here.
