from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import crossroadmember
from .models import newvisitor
from .models import NewChurches  
from .models import Intern 
# Register your models here.

class crossroadmemberAdmin(ImportExportModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'status','date_joined', )
    list_filter = ('date_joined',

    )
    search_fields= ('id', 'first_name', 'last_name', 'salutation','status', 
    	'date_joined','country_of_Citizenship','state','district', 'pin_code', )
    list_per_page = 10
    date_hierarchy ='date_joined'
admin.site.register(crossroadmember, crossroadmemberAdmin)


class newvisitorAdmin(ImportExportModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'status','date_visited', )
    list_filter = ('date_visited',

    )
    search_fields= ('id', 'first_name', 'last_name', 'salutation','status', 
    	'date_visited','country_of_Citizenship','state','district', 'pin_code', )
    list_per_page = 10
    date_hierarchy ='date_visited'
admin.site.register(newvisitor, newvisitorAdmin)


class NewChurchesAdmin(ImportExportModelAdmin):
    list_display=('id', 'Planter', 'country', 'city','Year_Established', )
    list_filter = ('Year_Established',

    )
    search_fields= ('id', 'Planter', 'country', 'city','Year_Established', 'pin_code', )
    list_per_page = 10
    date_hierarchy ='Year_Established'
admin.site.register(NewChurches, NewChurchesAdmin)


class InternAdmin(ImportExportModelAdmin):
    list_display=('id', 'first_name', 'last_name','country_of_Citizenship', 'district','start_date', )
    list_filter = ('start_date',

    )
    search_fields= ('id', 'first_name', 'last_name', 'district','start_date','country_of_Citizenship', 'pin_code', )
    list_per_page = 10
    date_hierarchy ='start_date'
admin.site.register(Intern, InternAdmin)
