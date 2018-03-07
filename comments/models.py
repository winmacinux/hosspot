from __future__ import unicode_literals
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Permission, User


class CommentManager(models.Manager):

	def all(self):
		qs = super(CommentManager, self).filter(parent=None)

		return qs

	def filter_by_instance(self, instance):	
		content_type = ContentType.objects.get_for_model(instance.__class__)
		obj_id = instance.id
		qs = super(CommentManager, self).filter(
		content_type=content_type, object_id=obj_id).filter(parent=None)
		return qs


class Rate(models.Model):
  user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')
  rating = models.IntegerField(default=0, null=False, blank=False)
  timestamp = models.DateTimeField(auto_now_add=True) 
  recommended = models.BooleanField(default=True, null=False, blank=False)

  class Meta:
    ordering = ["-timestamp"]

  def __str__(self):
    return str(self.user.username + "- " + str(self.rating))


class Comment(models.Model):
  user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'object_id')
  parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  objects = CommentManager()

  class Meta:
    ordering = ["-timestamp"]

  def __unicode__(self):
    return str(self.user.username + " " + self.content_type.__str__())

  def __str__(self):
    return str(self.user.username + " " + self.content_type.__str__())

  def get_absolute_url(self):
    return reverse("comments:thread", kwargs= {"pk": self.pk})

  def get_delete_url(self):
    return reverse("comments:delete", kwargs= {"pk": self.pk})		

  def children(self):  #replies
    return Comment.objects.filter(parent = self)

  @property
  def is_parent(self):
    if self.parent is not None:
      return False
    else:
      return True
