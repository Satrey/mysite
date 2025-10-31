from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Post


def post_list_published(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/post_list.html',
        {'post', posts}
    )

def post_list_draft(request):
    posts = Post.draft.all()
    return render(
        request,
        'blog/post/post_list.html',
        {'post', posts}
    )

def post_detail_published(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/post_detail.html',
        {'post': post}
    )

def post_detail_draft(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.DRAFT
    )
    return render(
        request,
        'blog/poist/post_detail.html',
        {'post': post}
    )