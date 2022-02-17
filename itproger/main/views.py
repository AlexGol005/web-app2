from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def picture(request):
    return HttpResponse("<img src='https://itproger.com/img/courses/1479108898.jpg'>")