from django import forms
from . import models


class CreateUserDetail(forms.ModelForm):
	class Meta:
		model = models.user
		fields = ['username','usernameid','DOB','sex','country','emailId','profile_pic']