from django.shortcuts import render


def index(request):
    content = {

    }
    return render(request, 'todo/index.html', content)
