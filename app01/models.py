from django.db import models
#in setting.py the declaration use the module django.db.mysql

#Below class are doing -(Create a table, named app01_userinfo , in the sql databases
# which the name is varchar32 )
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

class Department(models.Model):
    title = models.CharField(max_length=64)