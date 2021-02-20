import django_filters
from django_filters import DateFilter, CharFilter
from bootstrap_datepicker_plus import DatePickerInput
from .models import newvisitor

class NewvisitorFilter(django_filters.FilterSet):
	first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='contains',label='First Name')
	last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='contains',label='Last Name')
	date_visited = django_filters.DateFilter(field_name='date_visited', lookup_expr='iexact', label='Date Visited(2020-02-23)')
	choices = django_filters.CharFilter(field_name='choices', lookup_expr='icontains', label='choices')

class Meta:
		model = newvisitor
		fields = {
            'date_visited': ['exact'],
        }

		exclude = ['id','status', 'salutation', 'country_of_Citizenship', 'state', 
		'district','location','pin_code ',' email','phone','How_did_you_know_about_us','Note']
		widgets = {
            'date_visited': DatePickerInput(format='%Y-%m-%d'), }# default date-format %m/%d/%Y will be used
            #'end_date': DatePickerInput(format='%Y-%m-%d'), }

            #start_date = DateFilter(field_name="date_visited", lookup_expr='gte',label='Start Date')
	#end_date = DateFilter(field_name="date_visited", lookup_expr='lte',label='End Date')