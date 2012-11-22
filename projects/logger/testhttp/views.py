# Create your views here.

from django.shortcuts import render


def home(request):

    context = {
            'title': 'Home',
            'request': request,
            }

    return render(
            request,
            'home.html',
            context
            )
