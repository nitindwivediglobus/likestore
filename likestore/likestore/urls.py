"""
Definition of urls for Like_gifts.
"""

from datetime import datetime
from django.conf.urls import patterns, include, url
from app.forms import BootstrapAuthenticationForm

from app.views import *
from app.package1.HomeController import usersignup , userlogin ,userlogout
from app.package1.ProductController import *
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^sendgift', sendgift, name='sendgift'),
    url(r'^userlogin', userlogin, name='userlogin'),
    url(r'^userlogout', userlogout, name='userlogout'),
    url(r'^usersignup', usersignup, name='usersignup'),
    url(r'^howitworks', howitworks, name='howitworks'),
    url(r'^gifts', gifts, name='gifts'),
    url(r'^gifts/(?P<cat>\w{0,2})/$', gifts_1, name='gifts_1'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
