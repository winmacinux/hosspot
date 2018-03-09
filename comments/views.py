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
from hospital.models import Hospital, Service, SubService, Event, AdditionalService, Room, HR, Doctor, Feedback, Report
from hospital.serializers import HospitalSerializer, ServiceSerializer, SubServiceSerializer, EventSerializer, AdditionalServiceSerializer, RoomSerializer, HRSerializer, DoctorSerializer, FeedbackSerializer, ReportSerializer
from .models import Rate, Comment
from .serializers import RateSerializer, CommentSerializer
from django.contrib.contenttypes.models import ContentType

class ListCreateComment(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class RetrieveUpdateDestroyComment(generics.RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class ListCreateRating(generics.ListCreateAPIView):
  queryset = Rate.objects.all()
  serializer_class = RateSerializer

class RetrieveUpdateDestroyRating(generics.RetrieveUpdateDestroyAPIView):
  queryset = Rate.objects.all()
  serializer_class = RateSerializer