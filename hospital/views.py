from django.shortcuts import render
from annoying.functions import get_object_or_None
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from django.core import serializers
from django.contrib.auth import authenticate
from rest_framework.renderers import JSONRenderer, json
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import Permission, User
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from .models import Hospital, Service, SubService, Event, AdditionalService, Room, HR, Doctor, Feedback, Report
from .serializers import HospitalSerializer, ServiceSerializer, SubServiceSerializer, EventSerializer, AdditionalServiceSerializer, RoomSerializer, HRSerializer, DoctorSerializer, FeedbackSerializer, ReportSerializer
from comments.models import Rate, Comment
from comments.serializers import RateSerializer, CommentSerializer
from django.contrib.contenttypes.models import ContentType

class ListCreateHospital(generics.ListCreateAPIView):
  queryset = Hospital.objects.all()
  serializer_class = HospitalSerializer

  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    page = self.paginate_queryset(queryset)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    
    for item in serializer.data:
      content_type = ContentType.objects.get(model='hospital')
      services = json.loads(serializers.serialize("json", Service.objects.filter(hospital = item['id'])))
      additionalServices = json.loads(serializers.serialize("json", AdditionalService.objects.filter(hospital = item['id'])))
      rooms = json.loads(serializers.serialize("json", Room.objects.filter(hospital = item['id'])))
      hrs = json.loads(serializers.serialize("json", HR.objects.filter(hospital = item['id'])))
      doctors = json.loads(serializers.serialize("json", Doctor.objects.filter(hospital = item['id'])))
      events = json.loads(serializers.serialize("json", Event.objects.filter(hospital = item['id'])))
      ratings = json.loads(serializers.serialize("json", Rate.objects.filter(content_type=content_type, object_id = item['id'])))
      comments = json.loads(serializers.serialize("json", Comment.objects.filter(content_type=content_type, object_id = item['id'])))
      item['services'] = []
      item['additional_services'] = []
      item['rooms'] = []
      item['hrs'] = []
      item['doctors'] = []
      item['events'] = []
      item['ratings'] = []
      item['comments'] = []

      print(FeedbackView.as_view().__str__())
      
      for room in rooms:
        room['fields']['id'] = room['pk']
        item['rooms'].append(room['fields'])
      
      for doctor in doctors:
        doctor['fields']['id'] = doctor['pk']
        item['doctors'].append(doctor['fields'])
      
      for hr in hrs:
        hr['fields']['id'] = hr['pk']
        item['hrs'].append(hr['fields'])
      
      for service in additionalServices:
        service['fields']['id'] = service['pk']
        item['additional_services'].append(service['fields'])
      
      for event in events:
        event['fields']['id'] = event['pk']
        item['events'].append(event['fields'])
      
      for service in services:
        service['fields']['id'] = service['pk']
        service['fields']['sub_services'] = []
        subServices = json.loads(serializers.serialize("json", SubService.objects.filter(service = service['pk'])))
        
        for subService in subServices:
          subService['fields']['id'] = subService['pk']
          service['fields']['sub_services'].append(subService['fields'])
        
        print(len(service['fields']['sub_services']))
        item['services'].append(service['fields'])
      
      for rating in ratings:
        rating['fields']['id'] = rating['pk']
        item['ratings'].append(rating['fields'])
      
      for comment in comments:
        comment['fields']['id'] = comment['pk']
        item['comments'].append(comment['fields'])
      

    return Response(serializer.data)

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data = request.data)
    if serializer.is_valid():
      user = User.objects.create_user(request.data.get('username'),request.data.get('email'), request.data.get('password'))
      user.save()
      token, _ = Token.objects.get_or_create(user = user)
      request.data['user'] = user.id
      request.data['api_key'] = token.api_key
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
        self.object =serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackView(generics.ListCreateAPIView):
  queryset = Feedback.objects.all()
  serializer_class = FeedbackSerializer

  def __str__():
    return self.list(request, *args, **kwargs)


class ReportView(generics.ListCreateAPIView):
  queryset = Report.objects.all()
  serializer_class = ReportSerializer


