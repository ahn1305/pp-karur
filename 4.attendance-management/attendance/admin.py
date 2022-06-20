from django.contrib import admin
from .models import StudentDept,Student,Attendance

admin.site.register(StudentDept)
admin.site.register(Student)

class AttendanceAdmin(admin.ModelAdmin):
    date_hierarchy = 'Date'

admin.site.register(Attendance,AttendanceAdmin)
