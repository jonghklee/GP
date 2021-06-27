from django.urls import path
from input import viewsA as viewsA

urlpatterns = [
    path('page2', viewsA.page2 ,name='page2'),
]