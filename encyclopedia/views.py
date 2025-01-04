from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, wiki):
    return render(request, "encyclopedia/wiki.html", {
        "name": util.get_entry(wiki)
    })

def search(request):
    q = request.GET['q']

    if q in util.list_entries():
        return HttpResponseRedirect(q)
    else: 
        return render(request, "encyclopedia/error.html")

# https://django-book-new.readthedocs.io/en/latest/chapter07.html