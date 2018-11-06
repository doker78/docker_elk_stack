from django import forms
from .models import Vm

class vm_form(forms.ModelForm):
	class Meta:
		model = Vm
		fields = ('vm_name', 'number_of_cpu', 'memory_size', 'OS')