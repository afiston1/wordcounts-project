from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html',{'hithere':'this is me'})

def count(request):
    fulltext=request.GET['fulltext']
    ##print (fulltext)
    wordcount=fulltext.split()

    return render(request,'count.html',{'fulltext':fulltext,'count':len(fulltext)})
