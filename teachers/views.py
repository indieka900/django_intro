from django.shortcuts import render


def home(request):
    return render(request, 'teachers/home.html')

# Create your views here.
