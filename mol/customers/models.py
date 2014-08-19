# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone

class Customer(models.Model):
	customer_name=models.CharField(max_length=100,verbose_name=u'供应商名称')
	customer_tel=models.CharField(max_length=20,verbose_name=u'电话')
	customer_fox=models.CharField(max_length=20,verbose_name=u'传真')
	customer_address=models.CharField(max_length=250,verbose_name=u'地址')
	customer_email=models.EmailField(verbose_name=u'电子邮件')
	customer_bank=models.CharField(max_length=100,verbose_name=u'开户行')
	customer_account=models.CharField(max_length=50,verbose_name=u'账户')
	customer_taxid=models.CharField(max_length=50,verbose_name=u'税号')
	customer_documents1=models.FileField(upload_to='upload/customer/customer_documents',verbose_name='证件1',blank=True)
	customer_documents2=models.FileField(upload_to='upload/customer/customer_documents',verbose_name='证件2',blank=True)
	customer_documents3=models.FileField(upload_to='upload/customer/customer_documents',verbose_name='证件3',blank=True)

	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.customer_name


class Contact(models.Model):
	customer=models.ForeignKey(Customer)
	contact_name=models.CharField(max_length=100,verbose_name=u'联系人名称')
	contact_jobtitle=models.CharField(max_length=100,verbose_name=u'职务')
	contact_tel=models.CharField(max_length=20,verbose_name=u'电话')
	contact_fox=models.CharField(max_length=20,verbose_name=u'传真')
	#contact_address=models.CharField(max_length=250,verbose_name=u'地址')
	contact_email=models.EmailField(verbose_name=u'电子邮件')
	contact_qq=models.CharField(max_length=20,verbose_name=u'QQ')

	def __unicode__(self):
		return self.contact_name
		
