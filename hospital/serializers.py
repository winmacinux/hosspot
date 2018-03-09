from rest_framework import serializers
from .models import Hospital, Service, SubService, Event, AdditionalService, Room, HR, Doctor, Feedback, Report
from django.contrib.auth.models import Permission, User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hospital
    fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = '__all__'

class SubServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = SubService
    fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'

class AdditionalServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = AdditionalService
    fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = '__all__'

class HRSerializer(serializers.ModelSerializer):
  class Meta:
    model = HR
    fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feedback
    fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = Report
    fields = '__all__'