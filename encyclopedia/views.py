from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import markdown2

from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, wiki):
    content = util.get_entry(wiki)
    
    if wiki not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "title": "404 - Page Not Found",
            "message": "Sorry, The page you are looking for does not exist."
        })

    content_converted = markdown2.markdown(content)
    return render(request, "encyclopedia/wiki.html", {
        "content": content_converted,
        "title": wiki
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
        return render(request, "encyclopedia/error.html", {
            "title": "404 - Page Not Found",
            "message": "Sorry, The page you are looking for does not exist."
        })

def create(request):
    return render(request, "encyclopedia/create.html")

def new(request):
    q = request.POST['q']
    as_q = request.POST['as_q']
    entries = util.list_entries()

    if q in entries:
        return render(request, "encyclopedia/error.html", {
            "title": "Whoops...",
            "message": "This page already exists"
        })
    else:
        util.save_entry(q, as_q)
        return HttpResponseRedirect(f"wiki/{q}")

def edit(request, wiki):
    return render(request, "encyclopedia/edit.html", {
        "content": util.get_entry(wiki),
        "title": wiki,
    })

def update(request):
    q = request.POST['q']
    as_q = request.POST['as_q']

    util.save_entry(q, as_q)
    return HttpResponseRedirect(f"wiki/{q}")

def lucky(request):
    list = util.list_entries()
    randomInt = random.randint(0, len(list) - 1)
    luck = list[randomInt]

    return HttpResponseRedirect(f"wiki/{luck}")

# https://django-book-new.readthedocs.io/en/latest/chapter07.html