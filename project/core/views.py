from django.shortcuts import render
from .models import User

def home(request):
    #usuarios = User.objects.all()
    return render(request, "index.html")#, {"usuarios": usuarios})

# def salvar(request):
#     vnome = request.POST.get("nome")
#     User.objects.create(nome = vnome)
#     usuarios = User.objects.all()
#     return render(request, "index.html", {"usuario": usuarios})
