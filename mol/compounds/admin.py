from django.contrib import admin
from compounds.models import Compound

#class CasInline(admin.TabularInline):
#    model=Cas
#    extra=3
class CompoundAdmin(admin.ModelAdmin):
    #fieldsets=[
    #    ('CAS No.',{'fields':['casNo'], 'classes': ['collapse']}),
    #    ('Name CN.',{'fields':['name_cn'], 'classes': ['collapse']}),
    #    ('Name EN.',{'fields':['name_en'], 'classes': ['collapse']}),        
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #    ]
    #inlines=[CasInline]
    list_display=('casNo',
        'name_cn',
        'name_en',
        'molecular_formula',
        'molecular_weight',
        'molecular_Structure',
        'hplc_file',
        'gc_file',
        'hnmr_file',
        'cnmr_file',
        'lcms_file',
        'doc_file',
        #'suppliers',
        #'customers',
        'discription',
        'was_published_recently',
        )

    list_filter=['pub_date']    
    search_fields=['casNo','name_en','name_cn']
    
admin.site.register(Compound,CompoundAdmin)

# Register your models here.
