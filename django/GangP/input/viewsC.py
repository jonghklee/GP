from django.shortcuts import render
from .models import SoftwareSpec, ChoosenSpec
# Create your views here.
#종혁


def page0(request):
    return render(request, 'page0.html')

def page1(request):
    softs = SoftwareSpec.objects.all()
    choosen = ChoosenSpec.objects.all()
    softnamelist = []
    softlist = []
    for soft in softs:
        if soft.name in softnamelist:
            pass
        else:
            softnamelist.append(soft.name)
            softlist.append(soft)
    return render(request, 'page1.html', {'softs':softlist, 'shoosen':choosen})


def getpage1(request):
    a = request.POST('???')




# name과 옵션선택이 분리되어있어서 문제발생 - request.POST[''] 방식으로 받아오면됨.

#
