from django.contrib import admin

from omop.models import OMOP_TABLES

# Register your models here.
for table in OMOP_TABLES:
    admin.site.register(table)
