"""
URL configuration for statisticalsnacks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.conf.urls import handler404
from django.views.defaults import page_not_found

handler404 = page_not_found # built-in view that either produces a not found message or loads and renders the 404 template if there is one created

#endpoints
# all other url routes are appended to the base url
# url route - 'about/'
# full url of this endpoint will be http://localhost:8000/about/

# view function - handles web requests (e.g. visiting a website) and returns a response (e.g. renders a page)
#               - mapped to specific urls
#               - for example, http://localhost:8000/about/ will call a view function named about
#               - the mapping is done here in the urls.py

# the request parameter is for an instance of the HttpRequest class
# django gets the http request, encapsulates it, puts it in an http request object, passes it to the function

def index(request):
    return HttpResponse('<p>Hello, World! How are you today?</p>')

def banana(request):
    return HttpResponse('<h2>Banana</h2>')

urlpatterns = [
    path("admin/", admin.site.urls), # http://localhost:8000/admin/
    path('', index), # http://localhost:8000/
    path('webkiosk/', include('webkiosk.urls')), # http://localhost:8000/webkiosk
]
