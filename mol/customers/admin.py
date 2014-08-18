from django.contrib import admin
from customers.models import Customer,Contact

class ContactInline(admin.TabularInline):
	model=Contact
	extra=3

class CustomerAdmin(admin.ModelAdmin):

	inlines=[ContactInline]
	list_display=(
		'customer_name',
		'customer_tel',
		'customer_fox',
		'customer_email',
		'customer_bank',
		'customer_account',
		'customer_taxid',
		'customer_documents1',
		'customer_documents2',
		'customer_documents3',
		)
	list_filter=['pub_date']
	search_fields=['name']

admin.site.register(customer,CustomerAdmin)
# Register your models here.
