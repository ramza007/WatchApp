"""
Main Routes
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('appwatch.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
]
