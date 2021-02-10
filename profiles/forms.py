from django import forms
from .models import profiles, Temperature


class ProfileForm(forms.ModelForm):
   
    class Meta:
        model = profiles
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
     
       
class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Temperature
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TemperatureForm, self).__init__(*args, **kwargs)
     