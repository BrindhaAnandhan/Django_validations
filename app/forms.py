from django import forms
from app.models import *

def valid(data):
    if len(data) < 5:
        raise forms.ValidationError("invalid data")


class EmployeeForms(forms.Form):  
    Name = forms.CharField(validators=[valid, ])
    Experience = forms.IntegerField()
    Mobile = forms.IntegerField()
    Email = forms.EmailField()
    Remail = forms.EmailField()
    Portfolio = forms.URLField()
    Botcach = forms.CharField(required=False, widget=forms.HiddenInput)
    def clean_Botcach(self):
        b = self.cleaned_data['Botcach']
        if len(b)> 0:
            raise forms.ValidationError("Invalid")
        
    def clean(self):
        e = self.cleaned_data['Email']
        re = self.cleaned_data['Remail']
        if e != re:
            raise forms.ValidationError("Incorrect Email")
