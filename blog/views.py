from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post


def post_list_published(request):
    post_list = Post.published.all()
    
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
        
    return render(
        request,
        'blog/post/post_list.html',
        {'posts': posts}
    )

def post_list_draft(request):
    posts = Post.draft.all()
    return render(
        request,
        'blog/post/post_list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/post_detail.html',
        {'post': post}
    )


class PostListView(ListView):
    """
    Альтернативное представление для post_list
    Args:
        ListView (_type_): _description_
    """
    
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/post_list.html'