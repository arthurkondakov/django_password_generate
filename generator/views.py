from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from random import choice

# Create your views here.
def index_page(request):
    return render(request, 'generator/index.html')

def info_page(request):
    user_header = "Данные пользователя"
    user_info = {"firstname": "Ivan",
                 "age": 23}
    user_address = ("ул. Абрикосовая", 23, 45)
    user_language = ["python", "C++"]
    info = {"header": user_header,
            "message": "Welcome to info page",
            "user_info": user_info,
            "user_address": user_address,
            "user_language": user_language,
            "site": "<h1>Тест для отображения</h1>"
            }
    return render(request, 'generator/info.html', context=info)


def password(request):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    user_lenght_pass = int(request.GET.get("lenght", 10))
    generators_str = ''
    if request.GET.get("uppercase"):
        characters += characters.upper()
    if request.GET.get("simvol"):
        characters += '!#%&$@?'
    if request.GET.get("number"):
        characters += "0123456789"
    for i in range(user_lenght_pass):
        generators_str += choice(characters)
    return render(request, 'generator/password.html', context={"pass": generators_str,
                                                               "user_pass": user_lenght_pass})

def aboutpage(request):
    return render(request, "generator/about.html")