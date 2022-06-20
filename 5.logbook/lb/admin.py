from django.contrib import admin
from . models import Department,Class, LessonPlanExtended, RemedialForModel,Subject_A_SubjectCode,LogBook,CourseObj,LessonPlan,LessonPlanExtended,Cia_1_Result_Analysis,university_Result_Analysis,StudentParticulars,RemedialForUniversity,RemedialForCIA_2,RemedialForCIA_1,Model_Result_Analysis,CorrectiveAndPreventiveUniversity,CorrectiveAndPreventiveCIA_2,CorrectiveAndPreventiveModel,CorrectiveAndPreventiveCIA_1,Cia_2_Result_Analysis
from django.contrib.auth.models import Group

admin.site.register(Department)
admin.site.register(Class)
admin.site.register(Subject_A_SubjectCode)
admin.site.register(CourseObj)


class CourseObjInline(admin.TabularInline):
    model = CourseObj
    extra = 0

class LessonPlanInline(admin.TabularInline):
    model = LessonPlan
    extra = 0

class LessonPlanExtendedInline(admin.TabularInline):
    model = LessonPlanExtended
    extra = 0

class StudentParticularsInline(admin.TabularInline):
    model =StudentParticulars
    extra = 0

class Cia_1_Result_AnalysisInline(admin.TabularInline):
    model =Cia_1_Result_Analysis
    extra = 0

class CorrectiveAndPreventiveCIA_1Inline(admin.TabularInline):
    model =CorrectiveAndPreventiveCIA_1
    extra = 0

class RemedialForCIA_1Inline(admin.TabularInline):
    model =RemedialForCIA_1
    extra = 0


class Cia_2_Result_AnalysisInline(admin.TabularInline):
    model =Cia_2_Result_Analysis
    extra = 0

class CorrectiveAndPreventiveCIA_2Inline(admin.TabularInline):
    model =CorrectiveAndPreventiveCIA_1
    extra = 0

class RemedialForCIA_2Inline(admin.TabularInline):
    model =RemedialForCIA_2
    extra = 0

class Model_Result_AnalysisInline(admin.TabularInline):
    model =Model_Result_Analysis
    extra = 0

class CorrectiveAndPreventiveModelInline(admin.TabularInline):
    model =CorrectiveAndPreventiveModel
    extra = 0

class RemedialForModelInline(admin.TabularInline):
    model =RemedialForModel
    extra = 0


class university_Result_AnalysisInline(admin.TabularInline):
    model =university_Result_Analysis
    extra = 0

class CorrectiveAndPreventiveUniversityInline(admin.TabularInline):
    model =CorrectiveAndPreventiveUniversity
    extra = 0

class RemedialForUniversityInline(admin.TabularInline):
    model =RemedialForUniversity
    extra = 0



class LogBookAdmin(admin.ModelAdmin):
    inlines = [CourseObjInline,LessonPlanInline,LessonPlanExtendedInline,StudentParticularsInline,Cia_1_Result_AnalysisInline,CorrectiveAndPreventiveCIA_1Inline,RemedialForCIA_1Inline,Cia_2_Result_AnalysisInline,CorrectiveAndPreventiveCIA_2Inline,RemedialForCIA_2Inline,Model_Result_AnalysisInline,CorrectiveAndPreventiveModelInline,RemedialForModelInline,university_Result_AnalysisInline,CorrectiveAndPreventiveUniversityInline,RemedialForUniversityInline]

    readonly_fields = ('faculty_name',)

    def get_queryset(self, request):
        qs = LogBook.objects.filter(faculty_name=request.user)
        if request.user.is_superuser and request.user.username == "main-admin":
            return LogBook.objects.all()
            
        return qs.filter(faculty_name=request.user)

        

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'faculty_name', None) is None:
            obj.faculty_name = request.user
        obj.save()
    
    def has_change_permission(self, request, obj=None):
        if request.user.username == "main-admin":
            return True

        if obj is not None and obj.faculty_name != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.username == "main-admin":
            return True
        if obj is not None and obj.faculty_name != request.user:
            return False
        return True
    
    def has_view_permission(self, request, obj=None):
        if request.user.username == "main-admin":
            return True
        if obj is not None and obj.faculty_name != request.user:
            return False
        return True

admin.site.unregister(Group)
admin.site.register(LogBook,LogBookAdmin)
