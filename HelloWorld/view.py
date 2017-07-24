from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    context = {}
    context['hello'] = 'Hello Python!放弃吧，骚年！！！'
    context['title'] = '欢迎页面'
    return render(request, 'hello.html', context)