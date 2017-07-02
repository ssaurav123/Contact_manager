# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Contact(models.Model):
    phone = [
        ('mobile', 'mobile'),
        ('Home', 'home'),
        ('Office', 'office'),
        ('Phone', 'phone'),

    ]
    image = models.ImageField(null=True, blank=True)
    first_name = models.CharField(max_length = 255,)
    last_name = models.CharField(max_length = 255,)
    email = models.EmailField()
    mob_no =PhoneNumberField()
    Type=models.CharField(choices=phone,default='mobile',max_length = 255)

    def __str__(self):
        return str(self.mob_no)