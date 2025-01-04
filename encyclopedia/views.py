from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, wiki):
    if wiki not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
            "error": "The requested page was not found."
        })
    return render(request, "encyclopedia/wiki.html", {
        "name": util.get_entry(wiki)
    })