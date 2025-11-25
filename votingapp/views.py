from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request,"index.html")

def register(request):
    return render(request, "register.html")


