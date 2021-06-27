from django.shortcuts import render
from .models import SoftwareSpec, ChoosenSpec, othermatters
# Create your views here.
#소현

#1. 페이지 생성 전

def page2(request):
    softnamelist = request.POST['???']
    softSpec = SoftwareSpec.objects.all()
    softlist = []

    for soft in softSpec:
        if soft.name in softnamelist:
            softlist.append(soft)

    return render(request, 'page2.html' , {'softs':softlist})
#2. 페이지 생성 후
