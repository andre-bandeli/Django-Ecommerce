from django.shortcuts import render


def api(request):
    return render(request, 'index.html')