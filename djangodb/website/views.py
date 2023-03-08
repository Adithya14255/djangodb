from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def truehome(request):
    return render(request, 'truehome.html', {})


