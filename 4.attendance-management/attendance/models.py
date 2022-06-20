from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

poa = (
    ("Present","Present"),
    ("Absent","Absent")
)

ion = (
    ("Yes","Yes"),
    ("No","No")
)

class StudentDept(models.Model):
    Department = models.CharField(max_length=200,blank=True,null=True)


    class Meta:
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.Department

    

class Student(models.Model):
    Application_Number = models.CharField(max_length=200,blank=True)
    Register_Number = models.CharField(max_length=200,blank=True)
    Name = models.CharField(max_length=200,blank=True)
    Class = models.ForeignKey(StudentDept, on_delete=models.CASCADE)
    Parent_Mobile = models.CharField(max_length=10,blank=True)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.Name

class Attendance(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Present_or_Absent = models.CharField(max_length=8,choices=poa, default=None)
    # Informed_or_not = models.CharField(max_length=3,choices=ion, default=None)
    Reason = models.CharField(max_length=200, blank=True)
    Date = models.DateField(null=True)


    class Meta:
        verbose_name_plural = 'Attendance'

    def __str__(self):
        return str(self.Student)






