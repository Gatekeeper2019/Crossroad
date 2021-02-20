from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus import MonthPickerInput
from bootstrap_datepicker_plus import YearPickerInput
from django.contrib.admin import widgets
from .models import newvisitor
from .models import NewChurches
from django import forms


class VisitorForm(forms.ModelForm):

	class Meta:
		model = newvisitor
		fields = '__all__'

	date = forms.DateField(input_formats=['%Y-%m-%d'])
	widgets = {
            'Date': DatePickerInput(format='%Y-%m-%d'), }# default date-format %m/%d/%Y will be used
            #'end_date': DatePickerInput(format='%Y-%m-%d'), }




class ChurchForm(forms.ModelForm):
	class Meta:
		model = NewChurches
		fields = '__all__'