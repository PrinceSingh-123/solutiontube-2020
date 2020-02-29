from django.contrib import admin
from mysolution.models import examsolution
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(examsolution)
class PersonAdmin(ImportExportModelAdmin):
    pass
