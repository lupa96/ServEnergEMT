from django.contrib import admin

from apps.models import Parking, FreeSpaces
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.formats import base_formats


class CSV(base_formats.CSV):
    def get_title(self):
        return "scsv"

    def create_dataset(self, in_stream, **kwargs):
        kwargs['delimiter'] = ';'
        return super().create_dataset(in_stream, **kwargs)


class FreeSpacesResource(resources.ModelResource):
    class Meta:
        model = FreeSpaces


class FreeSpacesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("parking", "free_spaces_number", "updated_at")
    resource_class = FreeSpacesResource


admin.site.register(Parking)
admin.site.register(FreeSpaces, FreeSpacesAdmin)
