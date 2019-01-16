from django.shortcuts import render
from .models import Profile, Post, Business, Comment, Neighbourhood
from .forms import ProfileForm, NeighbourhoodForm, PostForm, CommentForm, BusinessForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except:
        return redirect('edit_profile',username = current_user.username)
    

    businesses = Business.objects.filter(neighbourhood = profile.neighbourhood)
    posts = Post.objects.filter(neighbourhood =profile.neighbourhood)

    return render(request, 'index.html', {"posts":posts, "profile":profile, "business": businesses})


def search(request):
    if 'busi'
