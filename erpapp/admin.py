from django.contrib import admin
from .models import Employee,EmployeeBioData,EmployeeBank_Salary_Details,EmployeeAcademic_Details,EmployeeResearch_Details,EmployeeProfession_Details
# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeBioData)
admin.site.register(EmployeeBank_Salary_Details)
admin.site.register(EmployeeAcademic_Details)
admin.site.register(EmployeeResearch_Details)
admin.site.register(EmployeeProfession_Details)
