from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime

def hello(request):
    context = {}
    context['hello'] = 'Hello Python!放弃吧，骚年！！！'
    context['title'] = '欢迎页面'
    context['time'] = datetime.datetime.now()
    return render(request, 'hello.html', context)

@login_required(login_url="/login/")
def home(request):

    return HttpResponse('Welcome, <a target="_blank" href="/logout/">logout</a>')