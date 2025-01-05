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
    entries = util.list_entries()
    results = []

    for entry in entries:
        if q in entry.casefold():
            results.append(entry)

    if q in entries:
        return HttpResponseRedirect(f"wiki/{q}")
    elif len(results) > 0:
        return render(request, "encyclopedia/search.html", {
            "subentries": results
        })
    else: 
        return render(request, "encyclopedia/error.html")

# https://django-book-new.readthedocs.io/en/latest/chapter07.html