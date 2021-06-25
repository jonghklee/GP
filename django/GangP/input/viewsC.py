from django.shortcuts import render
from django.utils.translation import check_for_language
from .models import SoftwareSpec, ChoosenSpec
# Create your views here.
#종혁

def page1(request):
    soft = SoftwareSpec.objects.all()
    choosen = ChoosenSpec.objects.all()
    return render(request, 'page1.html', {'soft':soft, 'shoosen':choosen})


# name과 옵션선택이 분리되어있어서 문제발생 - request.POST[''] 방식으로 받아오면됨.

#
