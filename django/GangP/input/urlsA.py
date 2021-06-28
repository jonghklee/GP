from django.urls import path
from input import viewsA


urlpatterns = [
    path('page2', viewsA.page2 , name='page2'),
    path('create/', viewsA.create, name="create")

]