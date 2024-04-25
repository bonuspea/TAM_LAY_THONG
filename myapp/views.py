from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *

# Create your views here.
def Home(request):
    return render(request,'myapp/home.html')

def Feature(request):
    return render(request,'myapp/feature.html')

def Contact(request):
    return render(request,'myapp/contact.html')

def TrackingPage(request):
    #tracks = ['โบนัส - TA3123TH','พาฤกษ์ - TA3124TH','สุพรรณี - TA3125TH','รอคน - TA3126TH']
    tracks = Tracking.objects.all()
    # print(tracks)
    # print('-----------')
    context = {'tracks':tracks}
    # print(context)
    return render(request,'myapp/tracking.html',context)


def Ask(request):
    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('name')
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')

        new = AskQA()
        new.name = name
        new.email = email
        new.detail = detail
        new.title = title
        new.save()

        print(name,email,title,detail)
    return render(request,'myapp/ask.html')


@login_required
def Questions(request):   
    questions = AskQA.objects.all()   
    context = {'questions':questions}   
    return render(request,'myapp/questions.html',context)


def Answer(request,askid):

    record = AskQA.objects.get(id=askid)

    if request.method == "POST":
        data = request.POST.copy()
        # askid = data.get('askid')
        detail_answer = data.get('detail_answer')
        record.detail_answer = detail_answer
        record.save()

    context = {'record':record}
    
        
    return render(request,'myapp/answer.html',context)



def Posts(request):
    posts = Post.objects.all()

    context = {"posts":posts}

    return render(request,'myapp/blogs.html',context)


def Posts2(request):
    posts = Post.objects.all()

    context = {"posts":posts}

    return render(request,'myapp/blogs2.html',context)



