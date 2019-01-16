from django import forms
from .models import UserProfile, Business, Neighbourhood, Post, Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class BusinessForm(forms.ModelForm):
