from django.shortcuts import render



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def classes(request):
    return render(request, 'classes.html')
    
    
# Create your views here.
