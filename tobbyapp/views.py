from django.shortcuts import render
# from .models import electrical,salon,welding

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def login(request):
    return render(request,'login.html')

def Order(request):
    return render(request,'Order.html')

