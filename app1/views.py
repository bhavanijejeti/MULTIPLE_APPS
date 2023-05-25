from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_string(request):
    return HttpResponse('hloo haii')
def app1(request):
    return render(request,'app1.html')
