from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def shops(request):
    return render(request, 'shops.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def feedback(request):
    return render(request, 'feedback.html')