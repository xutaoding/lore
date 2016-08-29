from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        print('This Custom Manager:', self.model, self.model.__name__, self._db)
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    # author = models.ForeignKey(User)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meat:
        ordering = ('-publish',)

    objects = models.Manager()  # Default Manager
    published = PublishedManager()  # custom manager

    def get_absolute_url(self):
        print('*' * 100)
        print(dir(self.publish))
        print('#' * 100)
        return reverse(
            viewname='blog:post_detail',
            args=[self.publish.year, self.publish.strftime('%m'), self.publish.day, self.slug])




