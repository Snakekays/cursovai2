"""pavel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pavelapp.views import *
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('login/', LoginPage.as_view()),
    path('contact/', ContactPage.as_view()),
    path('manager/', ManagerPage.as_view()),
    path('employee/', EmployeePage.as_view()),
    path('customers/', CustomersPage.as_view()),
    
    path('application/', ApplicationPage.as_view()),
    path('сhangeApplication/<int:id>', ApplicationChangePage.as_view()),
    path('deleteApplication/<int:id>', ApplicationDeletePage.as_view()),

    path('create/', CreatePage.as_view()),
    path('changeCustomer/<int:id>', CustomersrChangePagePage.as_view()),
    path('deleteCustomer/<int:id>', CustomersrDeletePage.as_view()),
    
    path('<int:id>', CustomersApplicationPage.as_view()),
    path('back', SessionCheck.as_view()),
]