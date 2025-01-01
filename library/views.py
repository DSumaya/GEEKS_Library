from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Hello my name is Sumaya, i am 16 years old 🙃')


def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse('I dont have animal) '"<img src = 'https://upload-os-bbs.hoyolab.com/upload/2022/05/14/23130084/b9bdec07c9250c4e390b69ce32059719_5031582172423641290.gif' >")

def date_time(request):
    if request.method == 'GET':
        time = datetime.datetime.now()
        return HttpResponse(f"{time.strftime('%Y-%m-%d %H:%M:%S')}")