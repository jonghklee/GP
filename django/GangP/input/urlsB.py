from django.urls import path
from input import viewsB

urlpatterns = [
    path('page2', viewsB.page2 , name='page2'),
    path('page1_5', viewsB.page1_5, name='page1_5'),
]