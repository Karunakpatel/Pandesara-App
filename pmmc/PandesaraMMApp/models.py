import datetime
from django.db import models


"""
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    id_no = models.CharField(max_length = 4,primary_key =True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=15)
    dob = models.DateField()
    age = models.CharField(max_length=3)
    firm = models.CharField(max_length=500)
    blood_group = models.CharField(max_length=5)
    contact_no = models.CharField(max_length = 10)
    education = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    fees = models.CharField(max_length = 5)

    



    
    def __str__(self):
        return(f"{self.created_at} {self.id_no} {self.name} {self.gender} {self.dob} {self.age}{self.firm}{self.blood_group}{self.contact_no}{self.education}{self.address}{self.fees}")
    
    """
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    id_no = models.CharField(max_length = 10,primary_key =True)
    parivar_no = models.CharField(max_length=10)
    family_id = models.CharField(max_length = 10,null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=15)
    dob = models.DateField()
    age = models.IntegerField()
    firm = models.CharField(max_length=500)
    blood_group = models.CharField(max_length=5)
    contact_no = models.CharField(max_length = 10)
    education = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    fees = models.CharField(max_length = 5)
    designation = models.CharField(max_length=100)
    sabhasad_no = models.CharField(max_length=10,null=True)
    reciept_no = models.CharField(max_length=10,null=True)
    reciept_date = models.CharField(max_length=20,null=True)
    kutch_watan = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.created_at} {self.id_no} {self.name} {self.gender} {self.dob} {self.age}{self.firm}{self.blood_group}{self.contact_no}{self.education}{self.address}{self.fees}{self.designation}{self.sabhasad_no}{self.reciept_no}{self.reciept_date}{self.parivar_no}{self.family_id}{self.kutch_watan}")
