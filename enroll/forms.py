from django import forms
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from enroll.models import Post

class Sign_up_form(UserCreationForm):
  password1 = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control'}),label='Password' )
  password2 = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
  class Meta:
    model = User
    fields = ['username','email', 'first_name', 'last_name']
    
    widgets = {
            'username': forms.TextInput(attrs={'class':'form-control',},),
            'email': forms.EmailInput(attrs={'class':'form-control'},),
            'first_name': forms.TextInput(attrs={'class':'form-control'},),
            'last_name': forms.TextInput(attrs={'class':'form-control'},),
    }
class log_in_form(AuthenticationForm):
  username = forms.CharField(widget=widgets.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(widget=widgets.PasswordInput(attrs={'class':'form-control'}))

class Add_post_form(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'desc']
    widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'desc' : forms.Textarea(attrs={'class':'form-control','cols':'100','rows':'5'}),
      }
    labels = {'desc':'Description'}