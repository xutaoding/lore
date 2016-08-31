from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.mail import send_mail
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


def share_post(request, post_id):
    template_name = ''
    sent = False
    post = get_object_or_404(Post, id=post_id, status='published')

    if request.POST == 'POST':
        form_email = forms.EmailPostForm(request.POST)

        if form_email.is_valid():
            data = form_email.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = "{] ({}) recommends you reading '{}".format(data['name'], data['email'], post.title)
            message = "Read '{}' at {}\n\n{} 's comments: {}".format(data['title'], post_url, data['name'],
                                                                     data['comments'])
            send_mail(subject, message, 'xxxx@aliyun.com', [data['to']])
            sent = True
    else:
        form_email = forms.EmailPostForm()

    return render(request, template_name, {'form': form_email, 'post': post, 'sent': sent})

