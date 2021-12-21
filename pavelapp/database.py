from django.shortcuts import redirect
from .models import *
from django.utils import timezone

def order_today():
    date_today = timezone.now()
    o_today = Application.objects.filter(Time=date_today)
    return o_today

def get_managers():
    managers = Employee.objects.filter(Access_rights=True)
    return managers

def get_Employee():
    employees = Employee.objects.filter(Access_rights=False)
    return employees

def autoriz(login, passw):
    users = Employee.objects.filter(login=login, password=passw)
    return users

def get_customer():
    customers = Customer.objects.all()
    return customers

def get_application(ID_Customer):
    applications = Application.objects.filter(ID_Customer=ID_Customer)
    return applications

def get_customers_id(id):
    i_customers = Customer.objects.get(id=id)
    return i_customers    

def add_customer(Series_and_number,Telephone,Name,Surname,Otchestvo,Email):
    a_customer = Customer(Series_and_number=Series_and_number,Telephone=Telephone,Name=Name,Surname=Surname,Otchestvo=Otchestvo,Email=Email)
    a_customer.save()

def update_customers(id,Series_and_number,Telephone,Name,Surname,Otchestvo,Email):
    u_customers = Customer.objects.get(id=id)
    u_customers.Series_and_number = Series_and_number
    u_customers.Telephone = Telephone
    u_customers.Name = Name
    u_customers.Surname = Surname
    u_customers.Otchestvo = Otchestvo
    u_customers.Email = Email
    u_customers.save()

def delete_customers(id):
    u_customers = Customer.objects.get(id=id)
    u_customers.delete()

def get_application_id(id):
    i_application = Application.objects.get(id=id)
    return i_application   

def add_application(Type, Design, Comments, Cost, date, Status, OCustomer):
    a_application = Application(ID_Customer=Customer.objects.get(id=OCustomer), Comments=Comments, Time=date, Type=Type, Design=Design, Cost=Cost, Status=Status)
    a_application.save()

def update_application(id,Type,Design,Comments,Cost, Time, Status, Ocustomer):
    u_application = Application.objects.get(id=id)
    u_application.Type = Type
    u_application.Design = Design
    u_application.Comments = Comments
    u_application.Cost = Cost
    u_application.Ocustomer = Ocustomer
    u_application.Time = Time
    u_application.Status = Status
    u_application.save()

def delete_application(id):
    u_application = Application.objects.get(id=id)
    u_application.delete()