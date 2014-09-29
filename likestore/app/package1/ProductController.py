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
import json
from django.core import serializers



def gifts(request):
    products = Products.objects.raw('SELECT * FROM products')
    template=loader.get_template("app/browse.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

def filter(request):
    if request.method == 'POST':
        fiteroption=request.POST.get("filterdata","")
        #filterarray = fiteroption.split(',')
        query='SELECT * FROM products WHERE ProductCategoryId in '+fiteroption
        print query
        #for cat in filterarray:
        #    query = query,cat
        products = Products.objects.raw(query)
        products = serializers.serialize("json",products)
        data = {'products': products}
        return HttpResponse(json.dumps(data), content_type="application/json")

def catgift(request, cat):
    print ('hiiii')
    print (cat)
    products = Products.objects.raw('SELECT * FROM products WHERE ProductCategoryId ='+ cat)
    template=loader.get_template("app/browse.html")
    rc=RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))

@csrf_protect
def  saveorderdetails(request):

     if request.method == 'POST':
        form = request.POST
        
        order = Orders(ordershipname = form['r_fname'],
             ordershipaddress = form['r_lname'],)
        order.save()
        orderdet = Orderdetails(detailname = form['fname'])
        orderdet.save()
        rc = RequestContext(request,{'products':products})
        return HttpResponse(template.render(rc))#re-direct to next page

def sendgift(request):
    print ('hiiii')
    try:
       user_id = request.session['user']
       user = Users.objects.raw('SELECT * FROM users WHERE UserID ='+user_id)
       template = loader.get_template("app/send_gift.html")
       rc = RequestContext(request,{'user':user})
       return HttpResponse(template.render(rc))
    except :
       template = loader.get_template("app/page_login.html")
       rc = RequestContext(request,{'message':'Login first'})
       return HttpResponse(template.render(rc))


def search(request, keyword):
    print (keyword)
    querey = 'SELECT * FROM products WHERE ProductName LIKE \'%%'+keyword+'%%\''
    products = Products.objects.raw(querey)
    template = loader.get_template("app/browse.html")
    rc = RequestContext(request,{'products':products})
    return HttpResponse(template.render(rc))
