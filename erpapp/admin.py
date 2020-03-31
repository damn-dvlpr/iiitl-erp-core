from django.contrib import admin
from .models import User,Employee_bio_data,Employee_bank_details,Employee_academic_details,Employee_research_details,Employee_profession_details
# Register your models here.

admin.site.register(User)
admin.site.register(Employee_bio_data)
admin.site.register(Employee_bank_details)
admin.site.register(Employee_academic_details)
admin.site.register(Employee_research_details)
admin.site.register(Employee_profession_details)
