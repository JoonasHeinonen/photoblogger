from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Post
from .forms import PostForm

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/photos/')
    else:
        form = PostForm()
        
    return render(request, 'photos/index.html', {'form': form})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'photos/detail.html', {'post': post})

def results(request, post_id):
    response = "You are looking at the results of post %s."
    return HttpResponse(response % post_id)

def like(request, post_id):
    return HttpResponse("You're liking/disliking %s." % post_id)