from django import forms
from app.models import *

tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
wl=[[wo.name,wo.name] for wo in Webpage.objects.all()]

class Topicforms(forms.Form):
    topic_name=forms.CharField()


class Webpageforms(forms.Form):
    topic_name=forms.ChoiceField(choices=tl)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()



class AccessRecordsforms(forms.Form):
    name=forms.ChoiceField(choices=wl)
    date=forms.DateTimeField()
    author=forms.CharField()