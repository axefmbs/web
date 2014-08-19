from django.contrib import admin
from suppliers.models import Supplier,Contact

class ContactInline(admin.TabularInline):
#class ContactInline(admin.StackedInline):
	model=Contact
	extra=3

class SupplierAdmin(admin.ModelAdmin):

	inlines=[ContactInline]
	list_display=(
		'supplier_name',
		'supplier_tel',
		'supplier_fox',
		'supplier_address',
		'supplier_email',
		'supplier_bank',
		'supplier_account',
		'supplier_taxid',
		'supplier_documents1',
		'supplier_documents2',
		'supplier_documents3',
		)
	list_filter=['pub_date']
	search_fields=['name']

admin.site.register(Supplier,SupplierAdmin)
# Register your models here.
