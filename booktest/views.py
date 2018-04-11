#coding=UTF-8
from django.shortcuts import render
from django.db.models import *
from models import *

# Create your views here.
def index(request):
    #list=BoookInfo.books1.filter(heroinfo__hcontent__contains="")
    #list=BoookInfo.books1.filter(pk__lte=3)
    #Max1=BoookInfo.books1.aggregate(Max('bpub_date'))
    #list=BoookInfo.books1.filter(bread__gt=F('bcomment'))
    #list=BoookInfo.books1.filter(pk__lt=4,btitle__contains='1')
    list=BoookInfo.books1.filter(Q(pk__lt=4)|Q(btitle__contains='1'))
    context={'list1':list,
             #'Max1':max1
             }
    return render(request,'booktest/index.html',context)