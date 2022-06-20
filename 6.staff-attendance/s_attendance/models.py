from tabnanny import verbose
from django.db import models

poa = (
    ("Present","Present"),
    ("Absent","Absent")
)

class Staff(models.Model):
    staff_id = models.CharField(max_length=200)
    staff_name = models.CharField(max_length=200)

    class meta:
        verbose_name_plural = "Staff"

    def __str__(self):
        return self.staff_name

class Attendance(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=8,choices=poa,default=None)
    reason = models.CharField(max_length=200, blank=True)
    date = models.DateField(null=True)

    class meta:
        verbose_name_plural = "Attendance"

    def __str__(self):
        return str(self.staff)

