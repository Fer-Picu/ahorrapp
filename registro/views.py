from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoadForm


def index(request):
    return HttpResponse("You're looking at question ")


def load(request):
    form = LoadForm()
    return render(request, 'registro/load.html', {'form': form})
