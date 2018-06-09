from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def not_found (request, *args, **kwargs):
#    raise Http404
    return('Not OK')
