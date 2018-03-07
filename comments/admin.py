from django.contrib import admin
from .models import Comment, Rate

admin.site.register(Comment)
admin.site.register(Rate)