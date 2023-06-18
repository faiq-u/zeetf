from django.shortcuts import render
from .models import thoughts
# Create your views here.

def index(request):
    return render(request,'index.html',{'content':thoughts.objects.all()})

def comment(request):
    text = request.GET['comment']
    return render(request,'comment.html',{'comment':text})
