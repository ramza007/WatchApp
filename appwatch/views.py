from django.shortcuts import render
from django.http  import HttpResponse
from .models import Profile 
# ,Follow,Neighborhood,Post,Business,
from .forms import ProfileForm 
# ,NeighborhoodForm,PostMessageForm,PostBusinessForm,

# Create your views here.
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