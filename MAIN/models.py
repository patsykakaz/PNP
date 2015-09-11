#-*- coding: utf-8 -*-
from django.db import models

class Client(models.Model):
   email = models.EmailField(unique=True, max_length=100)
   password = models.CharField(max_length=128)
   is_active = True
   is_staff= True