from django.db import models

# 참고 : 우선 모델을 구성할때 부장님이 언급하신 방법대로 하지 않아서 여러차례 수정을 거쳐야할 가능성이 높음
# 그러므로 수정에 용이하게 하기위해 데이터베이스(DB)에 저장해 놓은 정보를 삭제해서 새롭게 DB를 만드는 방법을 익혀놓아야함. 이 과정이 귀찮기에 되도록 DB에 정보를 저장하지 않는것을 권장.

# 또한 위처럼 사소한 일이라도 이 코드를 읽거나 수정하는 사람이 알아야하는 정보는 꼭 주석으로 남겨놓기!


# 소프트웨어별 사양
class SoftwareSpec(models.Model):
    name = models.CharField(max_length=100) # 중복 가능 (version으로 나누면 됨.)
    img = models.ImageField(upload_to = "input/", blank = True, null = True)
    version = models.IntegerField(default=0) # 하옵 중옵 상옵 등을 나타내는 인덱스로 사용
    # 0: 옵션 구별 없음 / 자연수: 자연수 개수만큼 옵션 존재
    cpu = models.CharField(max_length=100)
    vga = models.CharField(max_length=100)
    ram = models.IntegerField()
    hdd = models.IntegerField()

    def __str__(self):
        return self.name

    def goodfunction(self):
        print('I am good function')
    #사진 추가 필요 - media 다시 듣고 구현하기
    #사진 추가하기 전까지는 일단 templates/resource 폴더 사용하기


# 선택한 사양
class ChoosenSpec(models.Model):
    cpu = models.CharField(max_length=100, default=None)
    vga = models.CharField(max_length=100, default=None)
    ram = models.IntegerField(default=None)
    hdd = models.IntegerField(default=None)
    # 기타 선택이 필요한 사항 추가할 필요있음.

#전달폼 제작()

class othermatters(models.Model): 
    manufacturer = models.CharField(max_length = 100, default=None)
    laptopweight1 = models.FloatField(default=None)
    laptopweight2 = models.FloatField(default=None)
    screensize = models.CharField(max_length = 100, default=None)
    operating = models.CharField(max_length= 100, default=None)






    
