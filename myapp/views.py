from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'myapp/home.html')

def Feature(request):
    return render(request,'myapp/feature.html')

def Contact(request):
    return render(request,'myapp/contact.html')

def Tracking(request):
    tracks = ['โบนัส - TA3123TH','พาฤกษ์ - TA3124TH','สุพรรณี - TA3125TH','รอคน - TA3126TH']
    context = {'tracks':tracks}
    return render(request,'myapp/tracking.html',context)