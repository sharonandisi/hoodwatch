from django.shortcuts import render, redirect
from .models import Profile, Post, Business, Comment, Neighbourhood
from .forms import ProfileForm, NeighbourhoodForm, PostForm, CommentForm, BusinessForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
   

    return render(request, 'index.html')


def search(request):
    if 'business' in request.GET and request.GET['business']:
        search_term = request.GET.get('business')
        results = Business.objects.filter(name__icontains =search_term)
        message = f'{search_term}'
        context = {
            'message': message,
            'results':results
        }

    return render(request, 'search.html', context)

def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    context = {
        'profile': profile
    }
    return redirect(request,'profile.html', context)

def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        profile = Profile.objects.get(user=current_user)
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect ('profile', username = request.user)

    else:
        if Profile.objects.filter(user=current_user):
            profile = Profile.objects.get(user=current_user)
            form = ProfileForm(instance=profile)
        
        else:
            form = ProfileForm()
    return render(request, 'edit_profile.html', {"form":form})


def new_business(request):
    profile = Profile.object.get(user = request.user)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = profile
            business.neighbourhood = profile.neighbourhood
            business.save()
        return redirect('index')

    else:
        form = BusinessForm()
    context = {
        'form': form
    }

    return render(request, 'new_business.html', context)


def new_post(request):
    profile = Profile.object.get(user = request.user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.neighbourhood = profile.neighbourhood
            post.save()
        return redirect('index')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {"posts":posts, "profile":profile,"form":form})

