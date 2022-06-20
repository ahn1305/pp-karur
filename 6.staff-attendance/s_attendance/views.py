from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Staff,Attendance
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from datetime import date, datetime
import calendar

def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)

num_days = calendar.monthrange(date.today().year, date.today().month)[1]
currentMonth = datetime.now().month


def home(request):
    return render(request, 's_attendance/home.html')

@login_required
def monthlyreport(request):
    sd = Staff.objects.all()
    if request.method == "POST":
        query_dict = request.POST
        s_name = query_dict.get('name')

        try:
            sc = Staff.objects.get(staff_name=s_name)
        except ObjectDoesNotExist:
            messages.warning(request,"Staff doesn't exist")
            return redirect('mr')

        s_id = Staff.objects.get(staff_name=s_name).id

        start_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+"01"

        res = calendar.monthrange(datetime.now().year, currentMonth)[1]

        end_date = str(datetime.now().year)+"-"+str(currentMonth)+"-"+str(res)
        print(end_date)

        marp = Attendance.objects.filter(staff=s_id,attendance_status="Present").filter(date__month__gte=currentMonth,date__range=[start_date, end_date])
        mara = Attendance.objects.filter(staff=s_id,attendance_status="Absent").filter(date__month__gte=currentMonth)

        if marp or mara:
            staff = Staff.objects.get(staff_name=s_name)
            
            context = {"staff":staff,"mar":str(marp.count()),'asd':sd,'total_days':num_days,'mara':mara.count(),}
            if mara.count() >= 3:
                context['lop'] = "True"
                context['cl'] = "-"
            elif mara.count() <= 3:
                context['cl'] = "True"
                context['lop'] = "-"
            else:
                pass
            return render(request, 's_attendance/monthly.html',context)
        else:
            messages.success(request,"Query not found")
            return redirect('mr')

    else:
        context = {'asd':sd,}

        return render(request, 's_attendance/monthly.html',context)