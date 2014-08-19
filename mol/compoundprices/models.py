# -*- coding: utf-8 -*-
from django.db import models

from compounds.models import Compound
from suppliers.models import Supplier
from customers.models import Customer
from compoundclasss.models import Compoundclass

class Compoundprice(models.Model):
	compound=models.ForeignKey(Compound,verbose_name='化合物名称')
	supplier=models.ForeignKey(Supplier,verbose_name='供应商')
	class_name=models.ForeignKey(Compoundclass,verbose_name='类别')
	price=models.DecimalField(max_digits=6, decimal_places=2,verbose_name='价格',blank=True,null=True)

	def __unicode__(self):
		return self.price
		

# Create your models here.
