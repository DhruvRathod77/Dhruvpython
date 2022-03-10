from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myApp import views

urlpatterns = [
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("signup", views.handleSignup, name='handleSignup'),
    path("login", views.handleLogin, name='handleLogin'),
    path("logout", views.handleLogout, name='handleLogout')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
