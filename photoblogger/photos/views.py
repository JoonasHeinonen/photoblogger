from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list,}
    return render(request, 'photos/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'photos/detail.html', {'post': post})

def results(request, post_id):
    response = "You are looking at the results of post %s."
    return HttpResponse(response % post_id)

def like(request, post_id):
    return HttpResponse("You're liking/disliking %s." % post_id)