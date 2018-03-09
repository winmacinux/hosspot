from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import reverse

app_name= 'comments'

urlpatterns = [
    url(r'^comments/$', views.ListCreateComment.as_view()),
    url(r'^ratings/$', views.ListCreateRating.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyComment.as_view()),
    url(r'^ratings/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyRating.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)