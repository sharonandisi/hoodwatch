from django.shortcuts import render, redirect
from .models import Profile, Post, Business, Comment, Neighbourhood
from .forms import ProfileForm, NeighbourhoodForm, PostForm, CommentForm, BusinessForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    profile = Profile.objects.get(user = request.user)
    current_user = request.user
    posts = Post.objects.filter(neighbourhood = profile.neighbourhood)
    businesses = Business.objects.filter(neighbourhood = profile.neighbourhood)
   

    return render(request, 'index.html', {"posts":posts,"profile":profile, "businesses": businesses})

@login_required(login_url='/accounts/login/')
def post(request):
    profile = Profile.objects.get(user = request.user)
    current_user = request.user
    posts = Post.objects.filter(neighbourhood = profile.neighbourhood)
    comments = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('post', id)
    else:
        form = CommentForm()

    return render(request, 'post.html', {"posts":posts, "profile":profile, "comments":comments, "form":form})

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
    return render(request,'profile.html', context)

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

login_required(login_url='/accounts/login/')
def new_business(request):
    profile = Profile.objects.get(user = request.user)
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

    return render(request, 'new_business.html', {"profile":profile, "form":form})


def new_post(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.neighbourhood = profile.neighbourhood
            post.save()
        return redirect('post')
    else:
        form = PostForm()
    return render(request, 'new_post.html', { "profile":profile,"form":form})

