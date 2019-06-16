from django.http import HttpResponse
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)


def testdb(request):
    db1 = User(name="hello world")
    db1.save()
    return HttpResponse("添加数据成功")