from django.shortcuts import render


def index(request):
    x = 50
    return render(request, 'djangoProject/index.html', {"x": x})
