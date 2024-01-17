# forms.py
from django import forms
from .models import Employee, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Employee_id', 'Employee_name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['Department_id', 'Department_name', 'Department_manager']
