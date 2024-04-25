from django.urls import path
#from .views import Home, Feature ,Contact , Tracking
from .views import *

urlpatterns = [
    path('', Home , name='home'),
    path('feature', Feature , name='feature'),
    path('contact', Contact, name='contact'),
    path('track', TrackingPage , name='tracking'),
    path('ask', Ask , name='ask'),
    path('questions',Questions,name = 'questions'),
    path('answer/<int:askid>',Answer, name = 'answer'),
    path('blogs',Posts,name='posts'),
    path('blogs2',Posts2,name='posts'),

]
