from django.shortcuts import render
from .models import othermatters
# Create your views here.
#현진

def page2(request):
    return render(request, 'page2.html')

def create(request):
    matter1 = othermatters()
    matterlist = dict(request.POST.lists())

    del matterlist['csrfmiddlewaretoken']
    matter1.manufacturer = ','.join(matterlist['제조사'])
    matter1.laptopweight1 = ','.join(matterlist['무게'])
    matter1.screensize = ','.join(matterlist['화면크기'])
    matter1.operating = ','.join(matterlist['운영체제'])

    matter1.save()
    return render(request, 'practice.html', {'matter1': matter1})





