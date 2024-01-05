from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.



def insert_topic(request):
    ETFO=Topicforms()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicforms(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('No Topic Created')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=Webpageforms()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageforms(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse('Webpage is created')
        else:
            return HttpResponse('No webpage is created')
    return render(request,'insert_webpage.html',d)

def insert_access_records(request):
    EAFO=AccessRecordsforms()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordsforms(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(name=n)
            dy=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']
            AO=AccessRecords.objects.get_or_create(name=WO,date=dy,author=a)[0]
            AO.save()
            return HttpResponse('AccessRecords is created')
        else:
            return HttpResponse('No AccessRecords')
            
    return render(request,'insert_access_records.html',d)