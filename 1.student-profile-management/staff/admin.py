from django.contrib import admin
from .models import StaffProfile

class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('Name_Of_The_Staff', 'Date_Of_Birth', 'Gender', 'Email_Id',)

    fieldsets = (
        (None, {
            'fields': ('image_preview', 'Staff_Image', 'Name_Of_The_Staff', 
            'Designation', 'Qualification', 'Date_Of_Appointment', 
            'Experience', 'SET_or_NET_Qualified', 'Additional_Responsibility', 
            'Date_Of_Birth', 'Gender', 'Nationality',
            'Caste', 'Address_Of_Communication', 'Email_Id',
            'Pan_Card_No','Area_Of_Specialization', 'Candidates_Produced_Mphil_or_Phd',
            'Awards_or_Honours_Received','Papers_Published','Papers_Presented','Workshops_Attended',
            'Con_or_semi', 'Invited_Speaker', 'Programs_Organized', 'University_Rank_Produced',)
        }),
    )

    readonly_fields=('image_preview', )


# admin.site.register(StaffProfile,StaffProfileAdmin)