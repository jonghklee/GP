from django.urls import path
from input import viewsA


urlpatterns = [
    path('create/', viewsA.create, name="create")
]