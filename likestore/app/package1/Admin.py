
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

def admin(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'admin/page_login.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
        }
    )

def loginadmin(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'admin/index.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
        }
    )

def logoutadmin(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'admin/index.html',
        
        {
            'title':'About',
            'message':'Your application description page.',
        }
    )

def myusers(request):
    print ('hiiii')
    users = Users.objects.raw('SELECT * FROM users')
    template=loader.get_template("admin/userlist.html")
    rc=RequestContext(request,{'users':users})
    return HttpResponse(template.render(rc))


def myproducts(request, cat):
    print ('hiiii')
    print (cat)
    products = Products.objects.raw('SELECT * FROM products WHERE ProductCategoryId ='+ cat)
    template=loader.get_template("admin/tables_datatables.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

