from django.shortcuts import render, get_object_or_404
from django.views import View

from . import forms
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    template_name = 'blog/post/post_list.html'

    return render(request, template_name, {'post': posts})


def post_detail(request, year, month, day, post):
    template_name = ''
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    return render(request, template_name, {'post': post})


class EmailPostView(View):
    form_class = forms.EmailPostForm

    def post(self, request):
        # post = get_object_or_404()
        pass
