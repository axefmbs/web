# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone


class Supplier(models.Model):
	supplier_name=models.CharField(max_length=100,verbose_name=u'供应商名称')
	supplier_tel=models.CharField(max_length=20,verbose_name=u'电话')
	supplier_fox=models.CharField(max_length=20,verbose_name=u'传真')
	supplier_email=models.EmailField(verbose_name=u'电子邮件')
	supplier_bank=models.CharField(max_length=100,verbose_name=u'开户行')
	supplier_account=models.CharField(max_length=50,verbose_name=u'账户')
	supplier_taxid=models.CharField(max_length=50,verbose_name=u'税号')
	supplier_documents1=models.FileField(upload_to='upload/supplier/supplier_documents',verbose_name='证件1',blank=True)
	supplier_documents2=models.FileField(upload_to='upload/supplier/supplier_documents',verbose_name='证件2',blank=True)
	supplier_documents3=models.FileField(upload_to='upload/supplier/supplier_documents',verbose_name='证件3',blank=True)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.supplier_name


class Contact(models.Model):
	supplier=models.ForeignKey(Supplier)
	contact_name=models.CharField(max_length=100,verbose_name=u'联系人名称')
	contact_jobtitle=models.CharField(max_length=50,verbose_name=u'职务')
	contact_tel=models.CharField(max_length=20,verbose_name=u'电话')
	contact_fox=models.CharField(max_length=20,verbose_name=u'传真')
	contact_email=models.EmailField(verbose_name=u'电子邮件')
	contact_qq=models.CharField(max_length=20,verbose_name=u'QQ')

	def __unicode__(self):
		return self.contact_name 
