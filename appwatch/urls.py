"""
App routes
"""
#-----------------------------App Routes------------------------#


from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
]