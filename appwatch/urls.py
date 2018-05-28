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
    url(r'^new/hood/$',views.create_hood, name='newHood'),
    url(r'^all/hoods/',views.view_neighborhoods, name='allHoods'),
    url(r'^neighborhood/(\d+)',views.hood_details, name='pickHood'),
    url(r'^follow/(\d+)', views.follow, name='follow'),
    url(r'^unfollow/(\d+)', views.unfollow, name='unfollow'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^new/business/',views.create_business, name='newBusiness'),
    url(r'^business/(\d+)',views.business_details, name='business'),
    url(r'^search/', views.search_results, name='search_results'),


    # url(r'^manage/(\d+)',views.manage_image, name='manageImage'),
    url(r'^comment/(\d+)', views.new_comment, name='Comment'),




    # url(r'^home',views.home,name='hoodNews'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)