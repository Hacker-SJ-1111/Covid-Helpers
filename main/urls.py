from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="Home"),
    path("addhelp",views.addhelp,name="Add Help"),
    path("newhelp",views.newhelp,name="New Help"),
    path("report",views.report,name="Report"),
]
