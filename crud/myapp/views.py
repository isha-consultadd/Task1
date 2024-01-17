from django.shortcuts import render,redirect,HttpResponse
from .models import Employee
def allemployees(request):
    emp = Employee.objects.all()
    return render(request, "emp/allemployees.html", {"allemployees":emp})

def singleemployee(request, empid):
    return render(request, "emp/singleemployee.html")

def addemployee(request):
    if request.method == "POST":
        employeeid = request.POST.get("employeeid")
        employeename = request.POST.get("employeename")
        employeemail = request.POST.get("employeemail")
        employeeaddress = request.POST.get("employeeaddress")
        employeephone = request.POST.get("employeephone")

        e = Employee()
        e.employeeid = employeeid
        e.employeename = employeename
        e.email = employeemail
        e.address = employeeaddress
        e.phone = employeephone
        e.save()
        return redirect("/allemployees")
    return render(request, "emp/addemployee.html")

def deleteemployee(request, empid):
    e= Employee.objects.get(pk= empid)
    e.delete()
    return redirect("allemployees")

def updateemployee(request, empid):
    e= Employee.objects.get(pk= empid)
    #return redirect("allemployees")
    return render(request, "emp/updateemployee.html", {'singleemp':e})

def doupdateemployee(request, empid):
   
    try:
        emp = Employee.objects.get(pk=empid)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found", status=404)

    if request.method == "POST":
        updateemployeeid = request.POST.get('employeeid')
        updateemployename = request.POST.get('employeename')
        updateemployeemail = request.POST.get('employeemail')
        updateemployeeaddress = request.POST.get('employeeaddress')
        updateemployeephone = request.POST.get('employeephone')

        emp.employeeid = updateemployeeid
        emp.employeename = updateemployename
        emp.email = updateemployeemail
        emp.address = updateemployeeaddress
        emp.phone = updateemployeephone
        emp.save()

        return redirect("allemployees")

    return render(request, "emp/updateemployee.html", {'singleemp': emp})
    