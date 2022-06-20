from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    dept = models.CharField(max_length=200)

    def __str__(self):
        return self.dept

class Class(models.Model):
    name_of_the_class = models.CharField(max_length=200)
    def __str__(self):
        return self.name_of_the_class



class Subject_A_SubjectCode(models.Model):
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.subject

class LogBook(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    faculty_name = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
    clas = models.ForeignKey(Class,on_delete=models.CASCADE)
    title_of_the_paper = models.CharField(max_length=200)
    sub = models.ForeignKey(Subject_A_SubjectCode,on_delete=models.CASCADE)  
    semester = models.CharField(max_length=200)

    def __str__(self):
        return self.title_of_the_paper

class CourseObj(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    objectives = models.TextField(max_length=400,blank=True)
    outcomes = models.TextField(max_length=400,blank=True)
    inference = models.TextField(max_length=400,blank=True)

    def __str__(self):
        return str(self.related_with)

class LessonPlan(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE,blank=True)
    LessonPlanName = models.CharField(max_length=200,blank=True)
    clas = models.ForeignKey(Class,on_delete=models.CASCADE,blank=True)
    faculty_name = models.ForeignKey(User,null=True, blank=True,on_delete=models.CASCADE)
    sub = models.ForeignKey(Subject_A_SubjectCode,on_delete=models.CASCADE,blank=True)
    semester = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.LessonPlanName
    

class LessonPlanExtended(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE,null=True)
    name = models.ForeignKey(LessonPlan,on_delete=models.CASCADE)
    lecturenumber_and_hour = models.IntegerField(default=1)
    Date_planned = models.DateField()
    topics_to_be_covered = models.TextField(max_length=200)
    Actual_date = models.DateField()
    Remarks = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.related_with)

class StudentParticulars(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    s_no = models.IntegerField(default=1)
    Reg_No = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    CIA_1 = models.IntegerField(default=None)
    retest_for_cia1 = models.IntegerField(default=None,blank=True,null=True)
    CIA_2 = models.IntegerField(default=None)
    retest_for_cia2 = models.IntegerField(default=None,blank=True,null=True)
    modelexam = models.IntegerField(default=None)
    CIA_1_AVG = models.IntegerField(default=None)
    CIA_2_AVG = models.IntegerField(default=None)
    Assignments = models.IntegerField(default=None)
    Seminar = models.IntegerField(default=None)
    Attendance = models.IntegerField(default=None)
    InternalMarks = models.IntegerField(default=None)

class Cia_1_Result_Analysis(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    date_of_examination = models.CharField(max_length=200,blank=True,default="dd/mm/yyyy",null=True)
    name_of_the_examination = models.CharField(max_length=200,blank=True,null=True)
    total_number_of_students = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_appeared = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_passed = models.IntegerField(default=None,blank=True,null=True)
    no_pf_students_failed = models.IntegerField(default=None,blank=True,null=True)
    percentage_of_pass = models.CharField(max_length=200,blank=True,null=True)

    no_of_students_below_40 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_40_60 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_60_75 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_75_100 = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return self.name_of_the_examination


class CorrectiveAndPreventiveCIA_1(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    exam_name = models.ForeignKey(Cia_1_Result_Analysis,on_delete=models.CASCADE,blank=True,null=True)
    reason_for_failure = models.TextField(max_length=300,blank=True,null=True)
    corrective_action = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials_for_advance_learners = models.TextField(max_length=300,blank=True,null=True)


class RemedialForCIA_1(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE,blank=True)
    s_no = models.IntegerField(default=None,blank=True,null=True)
    reg_no = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    date = models.CharField(max_length=200,default="dd/mm/yyyy",null=True)


class Cia_2_Result_Analysis(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    date_of_examination = models.CharField(max_length=200,blank=True,default="dd/mm/yyyy",null=True)

    name_of_the_examination = models.CharField(max_length=200,blank=True,null=True)
    total_number_of_students = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_appeared = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_passed = models.IntegerField(default=None,blank=True,null=True)
    no_pf_students_failed = models.IntegerField(default=None,blank=True,null=True)
    percentage_of_pass = models.CharField(max_length=200,blank=True,null=True)

    no_of_students_below_40 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_40_60 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_60_75 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_75_100 = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return self.name_of_the_examination


class CorrectiveAndPreventiveCIA_2(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    exam_name = models.ForeignKey(Cia_2_Result_Analysis,on_delete=models.CASCADE,blank=True,null=True)
    reason_for_failure = models.TextField(max_length=300,blank=True,null=True)
    corrective_action = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials_for_advance_learners = models.TextField(max_length=300,blank=True,null=True)


class RemedialForCIA_2(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE,blank=True,null=True)
    s_no = models.IntegerField(default=None,blank=True,null=True)
    reg_no = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    date = models.CharField(max_length=200,default="dd/mm/yyyy",null=True)




class Model_Result_Analysis(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    name_of_the_examination = models.CharField(max_length=200,blank=True,null=True)
    date_of_examination = models.CharField(max_length=200,blank=True,default="dd/mm/yyyy",null=True)
    total_number_of_students = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_appeared = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_passed = models.IntegerField(default=None,blank=True,null=True)
    no_pf_students_failed = models.IntegerField(default=None,blank=True,null=True)
    percentage_of_pass = models.CharField(max_length=200,blank=True,null=True)

    no_of_students_below_40 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_40_60 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_60_75 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_75_100 = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return self.name_of_the_examination


class CorrectiveAndPreventiveModel(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    exam_name = models.ForeignKey(Model_Result_Analysis,on_delete=models.CASCADE,blank=True,null=True)
    reason_for_failure = models.TextField(max_length=300,blank=True,null=True)
    corrective_action = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials_for_advance_learners = models.TextField(max_length=300,blank=True,null=True)

    def __str__(self):
        return str(self.related_with)


class RemedialForModel(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE,blank=True,null=True)
    s_no = models.IntegerField(default=None,blank=True,null=True)
    reg_no = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    date = models.CharField(max_length=200,default="dd/mm/yyyy")

    def __str__(self):
        return str(self.related_with)


class university_Result_Analysis(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE,null=True)
    date_of_examination = models.CharField(max_length=200,blank=True,default="dd/mm/yyyy",null=True)
    name_of_the_examination = models.CharField(max_length=200,blank=True,null=True)
    year = models.CharField(max_length=200,blank=True,null=True)
    no_of_students_appeared = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_passed = models.IntegerField(default=None,blank=True,null=True)
    no_pf_students_failed = models.IntegerField(default=None,blank=True,null=True)
    percentage_of_pass = models.CharField(max_length=200,blank=True,null=True)
    percentage_of_fail = models.CharField(max_length=200,blank=True,null=True)
    higher_mark = models.CharField(max_length=200,blank=True,null=True)
    faculty_handled = models.CharField(max_length=200,blank=True,null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True,null=True)
    no_of_students_below_40 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_40_60 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_60_75 = models.IntegerField(default=None,blank=True,null=True)
    no_of_students_below_75_100 = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return self.name_of_the_examination



class CorrectiveAndPreventiveUniversity(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE)
    exam_name = models.ForeignKey(university_Result_Analysis,on_delete=models.CASCADE,blank=True,null=True)
    reason_for_failure = models.TextField(max_length=300,blank=True,null=True)
    corrective_action = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials = models.TextField(max_length=300,blank=True,null=True)
    coaching_detials_for_advance_learners = models.TextField(max_length=300,blank=True,null=True)

    def __str__(self):
        return str(self.related_with)


class RemedialForUniversity(models.Model):
    related_with = models.ForeignKey(LogBook,on_delete=models.CASCADE,blank=True)
    s_no = models.IntegerField(default=None,blank=True,null=True)
    reg_no = models.CharField(max_length=200,blank=True,null=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    date = models.CharField(max_length=200,default="dd/mm/yyyy",null=True)