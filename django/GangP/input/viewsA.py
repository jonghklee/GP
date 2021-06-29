from django.shortcuts import render
from .models import othermatters
# Create your views here.
#현진

def page2(request):
    return render(request, 'page2.html')

def create(request):
    matter1 = othermatters()

    matter1.manufacturer = request.POST['제조사']
    matter1.laptopweight1 = request.POST['무게']
    matter1.screensize = request.POST['화면크기']
    matter1.operating = request.POST['운영체제']
    matter1.save()
    return render(request, 'practice.html', {'matter1': matter1})





