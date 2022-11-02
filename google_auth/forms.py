from django import forms
from .models import *
  
class UserImage(forms.ModelForm):  
    class Meta:  
        model = photo_share  
        # It includes all the fields of model  
        fields = ["name","photo","user"]  