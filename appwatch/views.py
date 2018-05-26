from django.shortcuts import render
from django.http  import HttpResponse, Http404
from .models import Profile 
# ,Follow,Neighborhood,Post,Business,
from .forms import ProfileForm, NeighborhoodForm
# ,PostMessageForm,PostBusinessForm,
from django.contrib.auth.decorators import login_required

# Create your views here.

#-----------------Landing page--------------#

def index(request):
    # images = Image.get_images()
    current_user = request.user
    title = 'WatchApp | Home'
    # hoods = Neighborhood.get_neighborhoods
    # est = Follow.objects.get(user=current_user)
    # business = Business.get_business_by_estate(est.estate)
    # posts = Post.get_posts_by_estate(est.estate)
    return render(request, 'index.html' )
    #  {"est": est,"title": title,"user": current_user,"posts":posts,"business": business,  "hoods":hoods })



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


#-------------------- Hood View Functions--------------------#

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