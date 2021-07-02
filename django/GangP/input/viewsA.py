from django.shortcuts import redirect, render
from .models import othermatters
# Create your views here.
#현진


def create(request):
    matter1 = othermatters()
    matterlist = dict(request.POST.lists())

    del matterlist['csrfmiddlewaretoken']
    matter1.manufacturer = ','.join(matterlist['제조사'])
    matter1.laptopweight1 = ','.join(matterlist['무게'])
    matter1.screensize = ','.join(matterlist['화면크기'])
    matter1.operating = ','.join(matterlist['운영체제'])

    matter1.save()
    return redirect('page3')

def page3(request):
    return render(request, 'page3.html')






