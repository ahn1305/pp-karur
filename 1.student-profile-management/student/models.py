from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.utils.html import mark_safe


Gender = (
    ("Male","Male"),
    ("Female","Female")
)

Differently_Abled = (
    ('YES','YES'),
    ('NO','NO')
)

Visually_Challenged = (
    ('YES','YES'),
    ('NO','NO')
)


# Create your models here.
class StudentProfile(models.Model):
    Student_Image = models.ImageField(upload_to='student-imgs/')
    Student_Enrollment_Number = models.CharField(max_length=15)
    Roll_Number = models.CharField(max_length=15)
    University_Register_Number = models.CharField(max_length=200)
    Name_Of_The_Student = models.CharField(max_length=200)
    Father_Name = models.CharField(max_length=200)
    Mother_Name = models.CharField(max_length=200)
    Father_Occupation = models.CharField(max_length=200)
    Gender = models.CharField(max_length=6,choices=Gender)
    Date_Of_Birth = models.DateField()
    Differently_Abled_Person = models.CharField(max_length=4,choices=Differently_Abled,default='NO')
    Visually_Challenged = models.CharField(max_length=4,choices=Visually_Challenged,default='NO')
    Marital_Status = models.CharField(max_length=200,default="Single")
    Mother_Tongue = models.CharField(max_length=200)
    Nationality = models.CharField(max_length=200,default="INDIAN")
    Religion = models.CharField(max_length=200)
    Aadhar_Number = models.CharField(max_length=12)
    Address_For_Commumication = models.TextField(max_length=400,help_text="Enter a proper address",verbose_name="CommunicationAddress")
    Mobile_Number = models.CharField(max_length=10)
    Email_Address = models.EmailField()

    created_by = models.ForeignKey(User, null=True, blank=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Name_Of_The_Student

    def save(self ,*args, **kwargs):
        super().save()

        img = Image.open(self.Student_Image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Student_Image.path)
    
    @property
    def image_preview(self):
        if self.Student_Image:
            return mark_safe('<img src="{}" width= 300px height= 300px; style="border-radius: 50%" />'.format(self.Student_Image.url))
        return ""
    