from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def base(response):

    return render(response, "base.html", {})

def index(response):

    return render(response, "index.html", {})

