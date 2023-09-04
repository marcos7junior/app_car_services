from django.shortcuts import render
from .models import User

def home(request):
    usuarios = User.objects.all()
    return render(request, 'index.html', {"usuario": usuarios})
