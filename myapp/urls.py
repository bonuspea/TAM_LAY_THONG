from django.urls import path
#from .views import Home, Feature ,Contact , Tracking
from .views import *

urlpatterns = [
    path('', Home , name='home'),
    path('feature', Feature , name='feature'),
    path('contact', Contact, name='contact'),
    path('track', Tracking , name='tracking'),
]
