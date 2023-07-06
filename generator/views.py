from django.shortcuts import render
import random

# Create your views here.

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')


def password(request):
    
    characters = list("abcdefghijklmnopqrstuvwxyz")
    generate_password = ""

    length_password = int(request.GET.get('length'))
    uppercase_password = request.GET.get('uppercase')
    spe_sym_password = request.GET.get('special_symbols')
    numbers = request.GET.get('numbers')

    if uppercase_password != None: characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if spe_sym_password != None: characters.extend(list("|°!$%&/=¡¿?-_<>"))
    if numbers != None: characters.extend(list("0123456789"))

    for _ in range(length_password):
        generate_password += random.choice(characters)

    return render(request, 'password.html', {"password": generate_password})