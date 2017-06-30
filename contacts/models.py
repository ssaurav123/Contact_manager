# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length = 255,)
    last_name = models.CharField(max_length = 255,)
    email = models.EmailField()
    mob_no =PhoneNumberField()

    def __str__(self):
        return (self.mob_no)