from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(
        regex=r'^(?P<year>\d{4})/(?P<month>\d\d)/(?P<day>\d\d)/(?P<post>[-\w]+)/$',
        view=views.post_detail, name='post_detail'
    ),
]

