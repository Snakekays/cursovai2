from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Post)
admin.site.register(Employee)
admin.site.register(Application)