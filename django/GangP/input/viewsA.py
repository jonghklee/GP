from django.shortcuts import render, redirect
from .models import othermatters
# Create your views here.
#현진

def page2(request):
    blogs = othermatters.objects.all()
    return render(request, 'page2.html', {'blogs':blogs})

def create(request):
    o_m__ = othermatters()
    manufacturer = request.POST['제조사']
    laptopweight1, laptopweight2 = request.POST['무게']
    screensize = request.POST['화면크기']
    operating = request.POST['운영체제']
    o_m__.save()
    return redirect('detail', o_m__.id)


