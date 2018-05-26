"""
App routes
"""


from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

#-----------------------------App Routes------------------------#

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^update/profile/', views.create_profile, name='createProfile'),
    url(r'^new/hood/',views.create_hood, name='newHood'),
    # url(r'^home',views.home,name='hoodNews'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)