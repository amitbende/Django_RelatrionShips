from django.contrib import admin
from .models import Owner, Car

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['oid', 'first_name', 'last_name']
admin.site.register(Owner, OwnerAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ['cid', 'year', 'brand', 'model']
admin.site.register(Car, CarAdmin)
