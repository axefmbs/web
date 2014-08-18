# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone

from customers.models import Customer
from suppliers.models import Supplier

class Compound(models.Model):
        #CAS号
        casNo=models.CharField(max_length=20,verbose_name='CAS号',blank=True,null=True)
        #中文名
        name_cn=models.CharField(max_length=200,verbose_name='中文名')
        #英文名
        name_en=models.CharField(max_length=200,verbose_name='英文名',blank=True,null=True)
        #分子结构
        molecular_formula=models.CharField(max_length=100,verbose_name='分子式',blank=True,null=True)
        #分子量
        molecular_weight=models.DecimalField(max_digits=6, decimal_places=2,verbose_name='分子量',blank=True,null=True)
        #结构
        molecular_Structure = models.ImageField(upload_to = 'image/staructure',verbose_name='化学结构',blank=True,null=True)
        #纯度
        assay=models.CharField(max_length=10,verbose_name='纯度',blank=True,null=True)
        #丰度
        abundance=models.CharField(max_length=50,verbose_name='丰度',blank=True,null=True)
        #HPLC分析报告
        hplc_file=models.FileField(upload_to='upload/compounds/assay/hplc_file',verbose_name='HPLC分析报告',blank=True,null=True)
        #GC分析报告
        gc_file=models.FileField(upload_to='upload/compounds/assay/gc_file',verbose_name='GC分析报告',blank=True,null=True)
        #1H NMR分析报告
        hnmr_file=models.FileField(upload_to='upload/compounds/assay/hnmr_file',verbose_name='1H NMR分析报告',blank=True,null=True)
        #13C NMR分析报告
        cnmr_file=models.FileField(upload_to='upload/compounds/assay/cnmr_file',verbose_name='13C NMR分析报告',blank=True,null=True)
        #LC MS分析报告
        lcms_file=models.FileField(upload_to='upload/compounds/assay/lcms_file',verbose_name='LC MS分析报告',blank=True,null=True)
        #doc
        doc_file=models.FileField(upload_to='upload/compounds/doc_file',verbose_name='技术报告',blank=True,null=True)
        #供应商
        suppliers=models.ManyToManyField(Supplier)
        #客户
        customers=models.ManyToManyField(Customer)
        #描述
        discription = models.TextField(verbose_name='描述',blank=True,null=True)
        #发布时间
        pub_date = models.DateTimeField('date published')

        def __unicode__(self):
        	return self.casNo

        
        def was_published_recently(self):
                return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

