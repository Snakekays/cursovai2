from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from django.urls import *

from .database import *
from .models import *

# Create your views here.

class MainPage(View):
    def get(self, request):
        context = {}
        return render(request, 'index.html', context=context)

class LoginPage(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context=context)

    def post(self, request):
        entered_login = request.POST.get("enter_login")
        entered_passw = request.POST.get("enter_pass")
        users = autoriz(entered_login, entered_passw)
        if not users:
            context = {
                "message": "Введен неверный логин или пароль"
            }
            return render(request, 'login.html', context=context)
        elif users[0].Access_rights == 1:
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].Access_rights
            return HttpResponseRedirect('../manager/')
        else:
            request.session["id_user"] = users[0].id
            request.session["priv_user"] = users[0].Access_rights
            return HttpResponseRedirect('../employee/')

class SessionCheck(View):
    def get(self, request):
        if not request.session["priv_user"]:
            return render(request, 'employee.html')
        else:
            return render(request, 'manager.html')

class ContactPage(View):
    def get(self, request):
        context = {}
        return render(request, 'contact.html', context=context)

class ManagerPage(View):
    def get(self, request):
        employee = Employee.objects.get(id = request.session['id_user'])
        context = {
            'employee': employee
        }
        return render(request, 'manager.html', context=context)

class EmployeePage(View):
    def get(self, request):
        context = {}
        return render(request, 'employee.html', context=context)

class CustomersPage(View):
    def get(self, request):
        customers = get_customer()
        o_today = order_today()
        context = {
            'customers': customers,
            'o_today': o_today
        }
        return render(request, 'customers.html', context=context)

class CustomersApplicationPage(View):
    def get(self, request, id):
        applications = get_application(id)
        customers = get_customer()
        context = {
            'applications': applications,
            'customers': customers
        }
        return render(request, 'customers.html', context=context)

# Создание клиента
class CreatePage(View):
    def get(self, request):
        context = {}
        return render(request, 'create.html', context=context)
    
    def post(self, request):
        context={}
        First_Name = request.POST.get("First_Name")
        Last_Name = request.POST.get("Last_Name")
        Middle_name = request.POST.get("Middle_name")
        Series_and_number = request.POST.get("Series_and_number")
        Telephone = request.POST.get("Telephone")
        Email = request.POST.get("Email")
        if not First_Name:
            context["message_first_name"] = "Enter your name"
        elif not Last_Name:
            context["message_last_name"] = "Enter your last name"
        elif not Middle_name:
            context["message_middle_name"] = "Enter your middle name"
        elif not Series_and_number:
            context["message_series"] = "Enter your series and number"
        elif not Telephone:
            context["message_telephone"] = "Enter your series and number"
        elif not Email:
            context["message_email"] = "Enter your series and number"
        
        if context:
            return render(request, "create.html", context=context)
        else:
            add_customer(Series_and_number, Telephone, First_Name, Last_Name, Middle_name,Email)
            return HttpResponseRedirect('../customers')
# Редактирование клиента
class CustomersrChangePagePage(View):
    def get(self, request, id):
        customers = get_customer()
        changeCustomer = get_customers_id(id)
        context = {
            'customers': customers,
            'changeCustomer':changeCustomer
        }
        return render(request, 'changeCustomer.html', context=context)

    def post(self, request, id):
        context = {}
        First_Name = request.POST.get("First_Name")
        Last_Name = request.POST.get("Last_Name")
        Middle_name = request.POST.get("Middle_name")
        Series_and_number = request.POST.get("Series_and_number")
        Telephone = request.POST.get("Telephone")
        Email = request.POST.get("Email")
        # if not First_Name:
        #     context["message_first_name"] = "Enter your name"
        # elif not Last_Name:
        #     context["message_last_name"] = "Enter your last name"
        # elif not Middle_name:
        #     context["message_middle_name"] = "Enter your middle name"
        # elif not Series_and_number:
        #     context["message_series"] = "Enter your series and number"
        # elif not Telephone:
        #     context["message_telephone"] = "Enter your series and number"
        # elif not Email:
        #     context["message_email"] = "Enter your series and number"

        if context:
            return render(request, "changeCustomer.html", context=context)
        else:
            update_customers(id,Series_and_number,Telephone,First_Name,Last_Name,Middle_name,Email)
            return HttpResponseRedirect('../customers')
# Удаление клиента
class CustomersrDeletePage(View):
    def get(self, request, id):
        customers = get_customer()
        changeCustomer = get_customers_id(id)
        context = {
            'customers': customers,
            'changeCustomer':changeCustomer
        }
        return render(request, 'deleteCustomer.html', context=context)

    def post(self, request, id):
        context={}
        delete_customers(id)
        return HttpResponseRedirect('../customers')

# Создание заявка
class ApplicationPage(View):
    def get(self, request):
        customers = get_customer()
        status = ['Принят', 'В работе', 'Завершен', 'Отдан']
        context = {
            'customers': customers,
            'status': status
        }
        return render(request, 'application.html', context=context)

    def post(self, request):
        customers = get_customer()
        status = ['Принят', 'В работе', 'Завершен', 'Отдан']
        context={
            'customers': customers,
            'status': status
        }
        OCustomer = request.POST.get("OCustomer")
        Comments = request.POST.get("Comments")
        Type = request.POST.get("Type")
        Design = request.POST.get("Design")
        Cost = request.POST.get("Cost")
        Time = request.POST.get("Time")
        Status = request.POST.get("Status")
        if not Comments:
            context["message_comments"] = "Enter your comments"
        elif not Type:
            context["message_type"] = "Enter your type"
        elif not Design:
            context["message_design"] = "Enter your design"
        elif not Cost:
            context["message_cost"] = "Enter your cost"
        elif not Time:
            context["message_time"] = "Enter your time"
        elif not Status:
            context["message_status"] = "Enter your status"

        if context:
            return render(request, "application.html", context=context)
        else:
            add_application(Type, Design, Comments, Cost, Time, Status, OCustomer)
            return HttpResponseRedirect('../customers')
# Редактирование заявки
class ApplicationChangePage(View):
    def get(self, request,id):
        customers = get_customer()
        сhangeApplication = get_application_id(id)
        status = ['Принят', 'В работе', 'Завершен', 'Отдан']
        context = {
            'customers': customers,
            'сhangeApplication': сhangeApplication,
            'status': status
        }
        return render(request, 'сhangeApplication.html', context=context)

    def post(self, request, id):
        context={}
        OCustomer = request.POST.get("OCustomer")
        Comments = request.POST.get("Comments")
        Type = request.POST.get("Type")
        Design = request.POST.get("Design")
        Cost = request.POST.get("Cost")
        Time = request.POST.get("Time")
        Status = request.POST.get("Status")

        if context:
            return render(request, "сhangeApplication.html", context=context)
        else:
            update_application(id, Type, Design, Comments, Cost, Time, Status, OCustomer)
            return HttpResponseRedirect('../customers')
# Удаление заявки
class ApplicationDeletePage(View):
    def get(self, request, id):
        deleteApplication = get_application_id(id)
        context = {
            'deleteApplication':deleteApplication
        }
        return render(request, 'deleteApplication.html', context=context)

    def post(self, request, id):
        context={}
        delete_application(id)
        return HttpResponseRedirect('../customers')