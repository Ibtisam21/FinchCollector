from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse
from .models import Finch
# class Finch:
#     def __init__(self, name, breed, description, Image, Age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.Image = Image
#         self.Age = Age

# finch_list = [
#         Finch('Lolo', 'tabby', 'foul little demon', 'https://imgur.com/40qC4jX.jpg', 3),
#         Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 'https://imgur.com/40qC4jX.jpg', 0),
#         Finch('Raven', 'black tripod', '3 legged cat', 'https://imgur.com/40qC4jX.jpg', 4)
#     ]

# Define the home view
# def home(request):
#   return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# def finch_index(request):
#     finch_list=Finch.object.all()

#     return render(request, 'finch/index.html',
#     {
#         'finch': finch_list
#     })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finch/detail.html',
    { 'finch': finch })

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finch_list = Finch.objects.all()
    return render(request, 'finch/index.html',{
        'finch': finch_list
    })
