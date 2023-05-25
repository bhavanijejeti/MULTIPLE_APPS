from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_string(request):
    return HttpResponse('Taswin')
def app2(request):
    return render(request,'app2.html')

