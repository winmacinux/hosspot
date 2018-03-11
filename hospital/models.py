from django.db import models
from django.contrib.auth.models import Permission, User

class Hospital(models.Model):
  user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
  title = models.CharField(max_length=100, blank=False, null=False)
  about = models.CharField(max_length=20480, null=True, blank=True)
  address = models.CharField(max_length=1024, null=True, blank=True)
  city = models.CharField(max_length=100, null=True, blank=True)
  state = models.CharField(max_length=100, default='Kerala')
  country = models.CharField(max_length=100, default='India')
  phone = models.CharField(max_length=100, blank=True, null=True)
  api_key = models.CharField(max_length=100, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  start_date = models.DateField(null=True, blank=True)
  valid_date = models.DateField(null=True, blank=True)
  location = models.CharField(max_length=100, null=False, blank=False)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.title

  def get_username(self):
    return self.user.__str__()
  
class Service(models.Model):
  hospital = models.ForeignKey(Hospital, default=1, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name+"- "+self.hospital.__str__()

class SubService(models.Model):
  service = models.ForeignKey(Service, default=1, on_delete=models.CASCADE)
  name= models.CharField(max_length=200, null=False, blank=False)
  cost = models.FloatField(default=0)
  cost_implant = models.FloatField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name+"- "+self.service.__str__()

class Event(models.Model):
  hospital = models.ForeignKey(Hospital, default=1, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, null=False, blank=False)
  services = models.ManyToManyField(Service)
  date = models.DateField(null=False, blank=False)
  event_file = models.FileField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name+"- "+self.hospital.__str__()

class AdditionalService(models.Model):
  hospital = models.ForeignKey(Hospital, default=1, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, blank=False, null=False)
  value = models.CharField(max_length=100, blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name+"-"+self.hospital.__str__()

class Room(models.Model):
  hospital = models.ForeignKey(Hospital, default=1, on_delete=models.CASCADE)
  room_type = models.CharField(max_length=100, null=False, blank=False)
  total_bed = models.IntegerField(null=False, default=0, blank=False)
  rent_ac = models.FloatField(null=True, blank=True)
  rent_nonac = models.FloatField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.room_type+"- "+self.hospital.__str__()

class HR(models.Model):
  hospital = models.ForeignKey(Hospital, default=1, on_delete=models.CASCADE)
  title = models.CharField(max_length=100, null=False, blank=False)
  categroy = models.CharField(max_length=100, null= False, blank=True, default='')
  total = models.IntegerField(default=0, blank=True, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return str(self.title+"-"+self.categroy+"-"+self.hospital.__str__())

class Doctor(models.Model):
  hospital = models.ForeignKey(Hospital, default=1, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, null=False, blank=False)
  service = models.ForeignKey(Service, default=1, on_delete=models.CASCADE)
  time_slot = models.CharField(max_length=100, null=True, blank=True)
  experience = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name

class Report(models.Model):
  user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
  to = models.ForeignKey(Service, default=1, on_delete= models.CASCADE)
  message = models.CharField(max_length=20480, null=False, blank=False)
  seen = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.user.__str__()+"- "+self.to.__str__()

class Feedback(models.Model):
  user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
  to = models.ForeignKey(Hospital, default=1, on_delete= models.CASCADE)
  message = models.CharField(max_length=20480, null=False, blank=False)
  seen = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.user.__str__()+"- "+self.to.__str__()
