from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.

def main(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,'index.html',{'rs':obj,'re':obj1})


