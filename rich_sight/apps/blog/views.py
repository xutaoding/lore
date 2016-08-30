from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from . import forms
from .models import Post


# Create your views here.
def post_list(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 3)
    page = request.GET.get('page')
    print('Len:', len(posts_list))
    template_name = 'blog/post/post_list.html'

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, template_name, {'posts': posts, 'page': page})


def post_detail(request, year, month, day, post):
    template_name = 'blog/post/post_detail.html'
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__startswith=datetime.date(int(year), int(month), int(day))
    )

    print('post:', post)
    print('post:', post.publish.year, post.publish.month, post.publish.day, type(post.publish.year))

    return render(request, template_name, {'post': post})


class PostListView(ListView):
    queryset = Post.published.all()
    template_name = 'blog/post/post_list.html'
    paginate_by = 3
    context_object_name = 'posts'


class EmailPostView(View):
    form_class = forms.EmailPostForm

    def post(self, request):
        # post = get_object_or_404()
        pass
