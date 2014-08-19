# -*- coding: utf-8 -*-
from django.db import models

class Compoundclass(models.Model):
	name=models.CharField(max_length=20,verbose_name='类别')

	def __unicode__(self):
		return self.name
# Create your models here.
