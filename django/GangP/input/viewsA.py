from django.shortcuts import render
from .models import othermatters
# Create your views here.
#현진

def page2(request):
    return render(request, 'page2.html')
