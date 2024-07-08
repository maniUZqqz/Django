from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


# mysterious





def nav(request):
    context = {}
    return render(request, "mysterious/new.html", context)


def e404(request):
    raise Http404()





