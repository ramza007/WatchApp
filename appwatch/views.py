from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404
from .models import Profile, Neighborhood, Follow, Business, Post
from .forms import ProfileForm, NeighborhoodForm, PostBusinessForm, PostMessageForm
from django.contrib.auth.decorators import login_required


from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os
# Create your views here.

#-----------------Landing page--------------#
@login_required(login_url='/accounts/login')
def index(request):
    # images = Image.get_images()
    current_user = request.user
    title = 'WatchApp | Home'
    hoods = Neighborhood.get_neighborhoods
    est = Follow.objects.get(user=current_user)
    business = Business.get_business_by_estate(est.estate)
    # posts = Post.get_posts_by_estate(est.estate)
    return render(request, 'index.html', {"est": est,"title": title,"user": current_user,"hoods":hoods, "business": business})
    #  {"posts":posts, })



#---------------Profile-----------------#

@login_required(login_url='/accounts/login')
def create_profile(request):
    '''
    View function to view details of a hood
    '''
    current_user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(index)

    else:
        form = ProfileForm()
    return render(request, 'create-profile.html', {"form":form})

@login_required(login_url='/accounts/login')
def follow(request,hood_id):
    '''
    View function to allow user move to a different neighborhood_name
    '''
    current_user = request.user
    estate = Neighborhood.objects.get(id=hood_id)

    following = Follow(user=current_user, estate=estate)

    # check_if_exist = len(Follow.objects.all().filter(user=current_user))
    # if check_if_exist > 0:

    check_if_exists = Follow.objects.filter(user=current_user).exists()

    if check_if_exists == True:

        Follow.objects.all().filter(user=current_user).delete()
        Follow.objects.update_or_create(user=current_user, estate=estate)
        # following.save()
    else:
        following.save()

    return redirect(index)

@login_required(login_url='/accounts/login')
def unfollow(request,id):
    '''
    View function unfollow other users
    '''
    current_user = request.user
    estate = Neighborhood.objects.get(id=id)

    following = Follow(user=current_user, estate=estate).delete()

    return redirect(index)



#-------------------- Hood View Functions--------------------#

def view_neighborhoods(request):
    # images = Image.get_images()
    current_user = request.user
    title = 'Timeline'

    hoods = Neighborhood.get_neighborhoods

    return render(request, 'estates.html', {"title": title, "user": current_user, "hoods":hoods })

@login_required(login_url='/accounts/login')
def create_hood(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid:
            k = form.save(commit=False)
            k.user = current_user
            k.save()
            return redirect(index)

    else:
        form = NeighborhoodForm()
    return render(request, 'new-hood.html', {"form":form})

@login_required(login_url='/accounts/login')
def hood_details(request, hood_id):
    '''
    View function to view details of a hood
    '''

    if len(Follow.objects.all().filter(user=request.user))>0:
        details = Neighborhood.get_specific_hood(hood_id)
        exists = Follow.objects.all().get(user=request.user)
    else:
        details = Neighborhood.get_specific_hood(hood_id)
        exists = 0
    return render(request, 'hood-details.html',{"exists": exists,"details":details})

@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user  # get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user)

        pics = Image.objects.filter(user=request.user.id).all()

    except:

        title = f'{current_user.username}'

        # pics = Image.objects.filter(user=request.user.id).all()

        info = Profile.objects.filter(user=7)

    return render(request, 'my-profile.html', {"title": title, "current_user": current_user, "info": info, })



#-------------------Businesses------------#
@login_required(login_url='/accounts/login')
def create_business(request):
    '''
    View function to post a message
    '''
    current_user = request.user
    est = Follow.objects.get(user=current_user)

    if request.method == 'POST':
        form = PostBusinessForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.estate = est.estate
            post.save()
            return redirect(index)

    else:
        form = PostBusinessForm()
    return render(request, 'new-business.html', {"form":form})

@login_required(login_url='/accounts/login')
def business_details(request, business_id):
    '''
    View function to view details of a hood
    '''
    details = Business.get_specific_business(business_id)

    return render(request, 'business-details.html',{"details":details})

@login_required(login_url='/accounts/login')
def new_comment(request, hood_id):
    form = PostMessageForm(request.POST, request.FILES)
    return render(request, 'new-message.html', {"form":form})

def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photo = Images.search_by_title(search_term)
        photos = Images.objects.filter(name=searched_photo).all()
        message = f"{search_term}"
        return render(request, 'searched.html', {"message": message, "photos": searched_photo})
    else:
        message = 'Try Again'
        return render(request, 'searched.html', {"message": message})