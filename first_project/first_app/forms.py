from django import forms
from . import models
class formcreate(forms.Form):
	sno = forms.IntegerField()
	name = forms.CharField()
	testtext = forms.URLField(widget=forms.Textarea)
class modelFormcreate(forms.ModelForm):
	class Meta:
		model=models.User
		fields = "__all__" 