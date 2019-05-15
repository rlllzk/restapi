from django.contrib import admin
from .models import area, daerah
# Register your models here.
class DaerahAdmin(admin.ModelAdmin):
    list_display=('provinsi',)

class AreaAdmin(admin.ModelAdmin):
    list_display=('provinsi','luas','tahun')

admin.site.register(daerah, DaerahAdmin)
admin.site.register(area, AreaAdmin)
