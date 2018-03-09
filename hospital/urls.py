from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import reverse

app_name= 'hospital'

urlpatterns = [
    #url(r'^login/', views.login, name='login'),
    url(r'^hospitals/$', views.ListCreateHospital.as_view()),
    url(r'^hospitals/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyHospital.as_view()),
    url(r'^login/', views.login),
]

urlpatterns = format_suffix_patterns(urlpatterns)