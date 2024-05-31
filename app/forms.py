from django import forms
from .models import files

class filesForm(forms.ModelForm):
	class Meta:
		model = files
		fields = ['file']
		widgets = {
            'file': forms.FileInput(attrs={"accept": ".csv, .xlsx, .xls"}),
        }