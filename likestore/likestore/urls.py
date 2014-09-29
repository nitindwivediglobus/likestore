"""
Definition of urls for Like_gifts.
"""

from datetime import datetime
from django.conf.urls import patterns, include, url
from app.forms import BootstrapAuthenticationForm

from app.views import *
from app.package1.HomeController import usersignup , userlogin ,userlogout
from app.package1.ProductController import *
from app.package1.Admin import *

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
    url(r'^filter', filter, name='filter'),
    url(r'^catgift/(?P<cat>\w{0,2})/$', catgift, name='catgift'),
    url(r'^saveorderdetails', saveorderdetails, name='saveorderdetails'),
    url(r'^search/(?P<keyword>[a-z]*)/$', search, name='search'),

    url(r'^admin', admin, name='admin'),
    url(r'^loginadmin', loginadmin, name='loginadmin'),
    url(r'^logoutadmin', logoutadmin, name='logoutadmin'),
    url(r'^myusers', myusers, name='myusers'),
    url(r'^myproducts/(?P<cat>\w{0,2})/$', myproducts, name='myproducts'),



    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
