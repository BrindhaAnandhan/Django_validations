from django.db import models

# Create your models here.

class EmployeeInfo(models.Model):
    Name = models.CharField(max_length = 100, primary_key = True)
    Experience = models.IntegerField()
    Mobile = models.IntegerField(unique = True)
    Email = models.EmailField()
    Remail = models.EmailField(default ="abc@gmail.com")
    Portfolio = models.URLField()

    def __str__(self):
        return self.Name

