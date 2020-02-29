from django.contrib import admin
from ebook.models import ebook
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(ebook)
class PersonAdmin(ImportExportModelAdmin):
    pass