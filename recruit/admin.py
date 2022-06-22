# admin.py
from django.contrib import admin
from .models import Company, JobPosting

admin.site.register(Company)
admin.site.register(JobPosting)




