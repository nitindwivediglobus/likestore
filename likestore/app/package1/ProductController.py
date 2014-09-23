"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest, HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from django import *
from app.forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from app.models import *


def gifts(request):
    products = Products.objects.raw('SELECT * FROM Products')
    template=loader.get_template("app/browse.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def gifts_1(request, cat):
    print ('hiiii')
    print (cat)
    products = Products.objects.raw('SELECT * FROM Products WHERE productcategoryid =', cat)
    template=loader.get_template("app/browse.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def gifts_2(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/browse.html',
        
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def gifts_3(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/browse.html',
        
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def gifts_4(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/browse.html',
        
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

