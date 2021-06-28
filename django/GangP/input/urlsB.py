from django.urls import path
from input import viewsB

urlpatterns = [
    path('page1_5', viewsB.page1_5, name='page1_5'),
    path('new', viewsB.new, name='new'),
]