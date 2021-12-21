from django.db import models
from django.utils import timezone

class Customer(models.Model):
    Series_and_number = models.CharField(max_length=10)
    Telephone = models.CharField(max_length=11)
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Otchestvo = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)


class Post(models.Model):
    Name = models.CharField(max_length=50)
    Salary = models.IntegerField(default=0)
    Employment_contract = models.BooleanField(default=0)


class Employee(models.Model):
    Telephone = models.CharField(max_length=11)
    Email = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Otchestvo = models.CharField(max_length=50)
    Access_rights = models.BooleanField(default=0)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=300, default='')
    ID_Post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Application(models.Model):
    Type = models.CharField(max_length=50)
    Design = models.CharField(max_length=50)
    Comments = models.CharField(max_length=50)
    Cost = models.IntegerField(default=0)
    Time = models.DateField(default=timezone.now)
    Status = models.CharField(max_length=20, null = True)
    ID_Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


