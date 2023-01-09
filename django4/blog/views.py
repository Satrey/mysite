from django.shortcuts import render
from django.http import Http404
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request, 'blog/list.html', {'post': post})


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)

    except Post.DoesNotExist:
        raise Http404('Not Found')

    return render(request, 'blog/detail.html', {'post': post})
