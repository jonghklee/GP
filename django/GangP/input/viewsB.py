from django.shortcuts import redirect, render
from .models import SoftwareSpec, ChoosenSpec, othermatters
# Create your views here.
#소현

#1. 페이지 생성 전

def page1_5(request):
    softpost = request.POST
    softnamelist = []

    for i in softpost:
        softnamelist.append(i[5:])
    
    softnamelist = softnamelist[1:]

    softSpec = SoftwareSpec.objects.all()
    softlist = []

    for soft in softSpec:
        if soft.name in softnamelist:
            isthere = False
            same = None
            for inlistsoft in softlist:
                if soft.name == inlistsoft.name:
                    isthere = True
                    same = inlistsoft
            if isthere:
                if soft.version > same.version:
                    softlist.remove(same)
                    softlist.append(soft)
            else:
                softlist.append(soft)

    return render(request, 'page1.5.html', {'softs':softlist})
#2. 페이지 생성 후

def page2(request):
    listpost = request.POST
    listpost = dict(listpost)
    listpostkey = []
    listofrightsoftspec = []
    for i in listpost:
        listpostkey.append(i)
    softSpec = SoftwareSpec.objects.all()
    for soft in softSpec:
        for postspec in listpostkey:
            if soft.name == postspec and soft.version == listpost[postspec]:
                listofrightsoftspec.append(soft)

    cpu = ''
    vga = ''
    ram = 0
    hdd = 0

    for soft in listofrightsoftspec:
        cpu += str(soft.cpu)
        vga += str(soft.vga)
        hdd += float(soft.hdd)
        if soft.ram >= ram:
            ram = soft.ram
    
    newspec = ChoosenSpec()
    
    newspec.cpu = cpu
    newspec.vga = vga
    newspec.ram = ram
    newspec.hdd = hdd
    newspec.save()

    return render(request, 'page2.html')


