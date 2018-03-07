from django.contrib import admin
from .models import Hospital, Service, SubService, Event, AdditionalService, Room, HR, Doctor, Feedback, Report

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Event)
admin.site.register(AdditionalService)
admin.site.register(Room)
admin.site.register(HR)
admin.site.register(Doctor)
admin.site.register(Feedback)
admin.site.register(Report)
