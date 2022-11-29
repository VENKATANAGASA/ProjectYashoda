from django import forms
from app1.models import Bookappoinment,Bookappoinmenttime

class Bookappoinmentform(forms.ModelForm):
	class Meta:
		model = Bookappoinment
		fields = '__all__'


class Bookappoinmentdateform(forms.ModelForm):
	class Meta:
		model = Bookappoinmenttime
		fields = '__all__'
