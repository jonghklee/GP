from django.urls import path
from input import viewsA
from .viewsA import *


urlpatterns = [
    path('page2', viewsA.page2 , name='page2'),
    path('create/',create, name="create")

]