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
    #Urls for Basic Functionalities
    url(r'^services/$', views.ListCreateService.as_view()),
    url(r'^subservices/$', views.ListCreateSubService.as_view()),
    url(r'^events/$', views.ListCreateEvent.as_view()),
    url(r'^additionalservices/$', views.ListCreateAdditionalService.as_view()),
    url(r'^rooms/$', views.ListCreateRoom.as_view()),
    url(r'^hrs/$', views.ListCreateHR.as_view()),
    url(r'^doctors/$', views.ListCreateDoctor.as_view()),
    url(r'^reports/$', views.ListCreateReport.as_view()),
    url(r'^feedbacks/$', views.ListCreateFeedback.as_view()),
    url(r'^services/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyService.as_view()),
    url(r'^subservices/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroySubService.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyEvent.as_view()),
    url(r'^additionalservice/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyAdditionalService.as_view()),
    url(r'^hrs/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyHR.as_view()),
    url(r'^doctors/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyDoctor.as_view()),
    url(r'^reports/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyReport.as_view()),
    url(r'^feedbacks/(?P<pk>[0-9]+)/$', views.RetrieveUpdateDestroyFeedback.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)