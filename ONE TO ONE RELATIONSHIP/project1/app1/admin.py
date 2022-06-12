from django.contrib import admin
from .models import Person, Adhar

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['pid', 'first_name', 'last_name']

admin.site.register(Person, PersonAdmin)

class AdharAdmin(admin.ModelAdmin):
    list_display = ['person', 'aid']

admin.site.register(Adhar, AdharAdmin)
