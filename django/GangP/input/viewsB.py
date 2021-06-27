from django.shortcuts import render

# Create your views here.
#소현

#1. 페이지 생성 전

def page2(request):
    softnamelist = request.POST['???']
    
    return render()
#2. 페이지 생성 후


def getpage1(request):
    
    software.name=request.POST['name']
    software.version=request.POST['version']

   softs = SoftwareSpec.objects.all()
    choosen = ChoosenSpec.objects.all()
    softnamelist = []
    softlist = []
    for soft in softlist:
        if soft.name in softnamelist:

 return render(request,'page')       