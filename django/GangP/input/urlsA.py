from django.urls import path
from input import viewsA


urlpatterns = [
    path('create/', viewsA.create, name="create"),
    path('page3/', viewsA.page3, name="page3"),
]