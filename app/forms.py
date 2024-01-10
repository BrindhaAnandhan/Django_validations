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
    
    def clean(self):
        e = self.cleaned_data['Email']
        re = self.cleaned_data['Remail']

        if e != re:
            raise forms.ValidationError("Incorrect Email")
