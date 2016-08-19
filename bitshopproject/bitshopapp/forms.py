import re
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bitshopapp.models import *

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This User does not exist.")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password.")
			if not user.is_active:
				raise forms.ValidationError("This User is no longer active.")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
	email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))

	class Meta:
		model = User
		fields = ['username','email','password']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email already exists. Please try another one.")
		return email

class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea, label=_(""))

	class Meta:
		model = Comment
		fields = ['content']

	def clean(self):
		return self.cleaned_data

# class SubCommentForm(forms.ModelForm):
# 	content = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=1000, render_value=False)), label=_(""))

# 	class Meta:
# 		model = SubComment
# 		fields = ['content']

# 	def clean(self):
# 		return self.cleaned_data



