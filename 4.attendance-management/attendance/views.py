import calendar
import datetime as dt
from datetime import date, datetime
import itertools
from turtle import end_fill
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from attendance.models import Attendance, Student

def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)

num_days = calendar.monthrange(date.today().year, date.today().month)[1]
currentMonth = datetime.now().month




@login_required
def dailyreport(request):
    sd = Student.objects.all()
    if request.method == "POST":
        query_dict = request.POST
        s_name = query_dict.get('name')

        try:
            sc = Student.objects.get(Name=s_name)
        except ObjectDoesNotExist:
            messages.warning(request,"Student doesn't exist")
            return redirect('dr')

        s_id = Student.objects.get(Name=s_name).id
        dar = Attendance.objects.filter(Student=s_id,Date=date.today())
        if dar.exists():
            student = Student.objects.get(Name=s_name)
            context = {"student":student,"dar":dar,'asd':sd,}
            return render(request, 'attendance/dailyreport.html',context)
        else:
            messages.success(request,"Query not found")
            return redirect('dr')
    else:
        return render(request, 'attendance/dailyreport.html',{"asd":sd})
    
@login_required
def monthlyreport(request):

    def getalldata(st_name):
        try:
            sid = Student.objects.get(Name=st_name).id
        except:
            print("error")
        
        sid = Student.objects.get(Name=st_name).id
        start_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+"01"

        res = calendar.monthrange(datetime.now().year, currentMonth)[1]

        end_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+str(res)

        marp = Attendance.objects.filter(Student=sid,Present_or_Absent="Present").filter(Date__month__gte=currentMonth,Date__range=[start_date, end_date])
        mara = Attendance.objects.filter(Student=sid,Present_or_Absent="Absent").filter(Date__month__gte=currentMonth)

        return (marp.count(),mara.count(),Student.objects.get(Name=st_name))

    

    sd = Student.objects.all()


    if request.method == "POST":
        query_dict = request.POST
        s_name = query_dict.get('name')

        

        try:
            sc = Student.objects.get(Name=s_name)
        except ObjectDoesNotExist:
            messages.warning(request,"Student doesn't exist")
            return redirect('mr')

        s_id = Student.objects.get(Name=s_name).id

        start_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+"01"

        res = calendar.monthrange(datetime.now().year, currentMonth)[1]

        end_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+str(res)
        print(end_date)

        marp = Attendance.objects.filter(Student=s_id,Present_or_Absent="Present").filter(Date__month__gte=currentMonth,Date__range=[start_date, end_date])
        mara = Attendance.objects.filter(Student=s_id,Present_or_Absent="Absent").filter(Date__month__gte=currentMonth)

        if marp or mara:
            student = Student.objects.get(Name=s_name)
            context = {"student":student,"mar":str(marp.count()),'asd':sd,'total_days':num_days,'mara':mara.count(),}
            return render(request, 'attendance/monthlyreport.html',context)
        else:
            messages.success(request,"Query not found")
            return redirect('mr')

    else:

        sl = list(Student.objects.all())

        data = []
        for i in sl:
            data.append(getalldata(i))

        context={"asd":sd,"data":data,'num_days':num_days}

        return render(request, 'attendance/monthlyreport.html',context)

@login_required
def semreport(request):
    sd = Student.objects.all()
    if request.method == "POST":
        query_dict = request.POST
        s_name = query_dict.get('name')
        s_date = query_dict.get('sdate')
        e_date = query_dict.get('edate')

        ns_s = list(s_date.split("-"))
        ne_s = list(e_date.split("-"))

        ns_l = [int(i) for i in ns_s]
        ne_l = [int(i) for i in ne_s]

        # ns_f = int("".join(ns_l))
        # ne_f = ",".join(str(v) for v in ne_l)

        # print(type(ns_f))

        f_date = date(ns_l[0],ns_l[1],ns_l[2])
        l_date = date(ne_l[0],ne_l[1],ne_l[2])
        delta = l_date - f_date
    
        try:
            sc = Student.objects.get(Name=s_name)
        except ObjectDoesNotExist:
            messages.warning(request,"Student doesn't exist")
            return redirect('sr')

        s_id = Student.objects.get(Name=s_name).id

        # start_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+"01"

        # res = calendar.monthrange(datetime.now().year, currentMonth)[1]

        # end_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+str(res)
        # print(end_date)


        marp = Attendance.objects.filter(Student=s_id,Present_or_Absent="Present").filter(Date__range=[s_date, e_date])
        mara = Attendance.objects.filter(Student=s_id,Present_or_Absent="Absent").filter(Date__range=[s_date, e_date])

        ap = marp.count()/delta.days * 100
        apdf = f"%.2f" % ap
        print(apdf)

        if marp or mara:
            student = Student.objects.get(Name=s_name)
            context = {"student":student,"mar":str(marp.count()),'asd':sd,'total_days':delta.days,'mara':mara.count(),'percentage':apdf }
            return render(request, 'attendance/semreport.html',context)
        else:
            messages.success(request,"Query not found")
            return redirect('sr')

    else:
        context = {'asd':sd,}

        return render(request, 'attendance/semreport.html',context)