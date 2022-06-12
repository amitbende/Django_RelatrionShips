from django.contrib import admin
from .models import Student, Course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'first_name', 'last_name', 'mail']
admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['student', 'course_name', 'course_fees']
admin.site.register(Course, CourseAdmin)

