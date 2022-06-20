from django.contrib import admin
from .models import StaffProfile
from django.contrib.auth.models import Group

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
            'Con_or_semi', 'Invited_Speaker', 'Programs_Organized', 'University_Rank_Produced', 'created_by')
        }),
    )

    readonly_fields=('image_preview', 'created_by', )


    def get_queryset(self, request):
        qs = StaffProfile.objects.filter(created_by=request.user)
        if request.user.is_superuser and request.user.username == "main-admin":
            return StaffProfile.objects.all()
            
        return qs.filter(created_by=request.user)

        

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()
    
    def has_change_permission(self, request, obj=None):
        if request.user.username == "main-admin":
            return True

        if obj is not None and obj.created_by != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.username == "main-admin":
            return True
        if obj is not None and obj.created_by != request.user:
            return False
        return True
    
    def has_view_permission(self, request, obj=None):
        if request.user.username == "main-admin":
            return True
        if obj is not None and obj.created_by != request.user:
            return False
        return True
    


admin.site.unregister(Group)
admin.site.register(StaffProfile,StaffProfileAdmin)