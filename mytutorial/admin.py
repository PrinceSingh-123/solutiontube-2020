from django.contrib import admin
from mytutorial.models import Solution_videos
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Solution_videos)
class PersonAdmin(ImportExportModelAdmin):
    pass