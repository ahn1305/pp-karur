from django.db import models
from PIL import Image
from django.utils.html import mark_safe
from django.contrib.auth.models import User


s_o_n_quali = (
   
    ('YES','YES'),
    ('NO','NO')
)

Gender = (
    ("Male","Male"),
    ("Female","Female")
)


class StaffProfile(models.Model):
    Staff_Image = models.ImageField(upload_to='staff-imgs/')
    Name_Of_The_Staff = models.CharField(max_length=200)
    Designation = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=200)
    Date_Of_Appointment = models.DateField()
    Experience = models.TextField(max_length=500)
    SET_or_NET_Qualified = models.CharField(max_length=4,choices=s_o_n_quali,default='NO')
    Additional_Responsibility = models.TextField(max_length=300)
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(max_length=6,choices=Gender)
    Nationality = models.CharField(max_length=200)
    Caste = models.CharField(max_length=200)
    Address_Of_Communication = models.TextField(max_length=500,help_text="Enter a proper address",verbose_name="Communication Address")
    Email_Id = models.EmailField()
    Pan_Card_No = models.CharField(max_length=11)
    Area_Of_Specialization = models.CharField(max_length=200)
    Candidates_Produced_Mphil_or_Phd = models.CharField(max_length=200, verbose_name="M.Phil/Ph.D, Candidates Produced", blank=True)
    Awards_or_Honours_Received = models.TextField(max_length=400, blank=True,verbose_name="Awards & Honours Received")
    Papers_Published = models.TextField(max_length=500, blank=True,verbose_name="Papers Published in Journals (N/I)")
    Papers_Presented = models.TextField(max_length=400,blank=True,verbose_name="Papers Presented in Conferences")
    Workshops_Attended = models.TextField(max_length=500,blank=True)
    Con_or_semi = models.TextField(max_length=500, blank=True, verbose_name="Conference/Seminar Attended")
    Invited_Speaker = models.TextField(max_length=500, blank=True)
    Programs_Organized = models.TextField(max_length=600, verbose_name="Programs organized (Conf/Workshop/FDP/GL/Webinar)...")
    University_Rank_Produced = models.CharField(max_length=200, blank=True)

    created_by = models.ForeignKey(User, null=True, blank=True,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Name_Of_The_Staff
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.Staff_Image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Staff_Image.path)
    
    @property
    def image_preview(self):
        if self.Staff_Image:
            return mark_safe('<img src="{}" width= 300px height= 300px; style="border-radius: 50%" />'.format(self.Staff_Image.url))
        return ""


