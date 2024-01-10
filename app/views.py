from django.shortcuts import render
from app.views import *
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.


def Employee(request):
    EFO = EmployeeForms()
    data = {'EFO': EFO}
    if request.method == 'POST':
        EFDO = EmployeeForms(request.POST)
        if EFDO.is_valid():
            name = EFDO.cleaned_data['Name']
            ex = EFDO.cleaned_data['Experience']
            mob =  EFDO.cleaned_data['Mobile']
            email = EFDO.cleaned_data['Email']
            Remail = EFDO.cleaned_data['Remail']
            pf = EFDO.cleaned_data['Portfolio']
            EOO = EmployeeInfo.objects.get_or_create(Name = name, Experience = ex, Mobile = mob, Email = email,Remail=Remail, Portfolio = pf)[0]
            EOO.save()
            return HttpResponse("School Created")
        else:
            return HttpResponse("Invalid")
    return render(request, 'Employee.html', data)


        


