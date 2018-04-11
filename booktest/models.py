# coding=UTF-8
from django.db import models

# Create your models here.
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    def create(cls,btitle,bpub_daate):
        b=BoookInfo
        b.btitle=btitle
        b.bread=0
        b.bcomment=0
        b.isDelete=False
        return b

class BoookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcomment=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='bookinfo'
    books1=models.Manager()
    books2=BookInfoManager()

    @classmethod
    def create(cls,btitle,bpub_daate):
        b=BoookInfo
        b.btitle=btitle
        b.bread=0
        b.bcomment=0
        b.isDelete=False
        return b


class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BoookInfo)