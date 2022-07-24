from __future__ import unicode_literals
from django.db import models

class ThiefLocation(models.Model):
    name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Person(models.Model):
    name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=255,default=None)
    address = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)