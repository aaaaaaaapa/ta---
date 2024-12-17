from django.contrib import admin

from .models import Rang, Depart, Employee, EmployeeAccounting, Vacation, Tabel

admin.site.register(Rang)
admin.site.register(Depart)
admin.site.register(Employee)
admin.site.register(EmployeeAccounting)
admin.site.register(Vacation)
admin.site.register(Tabel)
