#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from test_ks.models import Chubanshe
from test_ks.models import Jiaocai
from test_ks.models import Dinggou
from test_ks.models import Xuexiao
def signup(request):
    list = Chubanshe.objects.all()
    context = {'cbslist': list}
    if request.method =='POST':
        return render(request, 'test_ks/index.html',context)
    else:
        return render(request,'test_ks/signup.html')

def index(request):
    list=Chubanshe.objects.all()
    context={'cbslist':list}
    return render(request,'test_ks/index.html',context)

def detail(request,id):
    list=Chubanshe.objects.get(cbs_id=id).jiaocai_set.all()
    list2 = Chubanshe.objects.get(cbs_id=id).dinggou_set.all()
    list1 = Chubanshe.objects.get(cbs_id=id).xuexiao_set.all()
    context={
        'Jclist':list,
        'Dglist':list2,
        'Xxlist':list1,
    }
    return render(request,'test_ks/detail.html',context)



