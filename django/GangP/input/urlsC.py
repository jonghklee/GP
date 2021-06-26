from django.urls import path
from input import viewsC as viewsC

urlpatterns = [
    path('', viewsC.page0 ,name='page0'),
    path('page1', viewsC.page1 ,name='page1'),
]