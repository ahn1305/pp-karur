from django.contrib import admin
from .models import StudentProfile
from django.contrib.auth.models import User,Group


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', )


    def has_view_or_change_permission(self, request ,obj=None):
        if request.user.username == "main-admin":
            return True

    def has_add_permission(self, request ,obj=None):
        if request.user.username == "main-admin":
            return True
    def has_delete_permission(self, request ,obj=None):
        if request.user.username == "main-admin":
            return True
    

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('Name_Of_The_Student','Father_Name','Mother_Name','Date_Of_Birth','Mobile_Number')
    fieldsets = (
        (None, {
            'fields': ('image_preview', 'Student_Image', 'Student_Enrollment_Number', 
            'Roll_Number', 'University_Register_Number', 'Name_Of_The_Student', 
            'Father_Name', 'Mother_Name', 'Father_Occupation', 
            'Gender', 'Date_Of_Birth', 'Differently_Abled_Person',
            'Visually_Challenged', 'Marital_Status', 'Mother_Tongue',
            'Nationality','Religion', 'Aadhar_Number',
            'Address_For_Commumication','Mobile_Number','Email_Address','created_by')
        }),
    )
    readonly_fields=('image_preview','created_by', )
    # list_filter = ('created_by',)


    def get_queryset(self, request):
        qs = StudentProfile.objects.filter(created_by=request.user)
        if request.user.is_superuser and request.user.username == "main-admin":
            return StudentProfile.objects.all()
            
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
    

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(StudentProfile,StudentProfileAdmin)
admin.site.unregister(Group)
