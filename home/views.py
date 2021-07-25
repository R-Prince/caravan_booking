from django.shortcuts import render


def index(request):
    # Return Home/Index page
    return render(request, 'home/index.html')
