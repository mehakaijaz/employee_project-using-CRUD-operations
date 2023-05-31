from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': "Full Name",
            'emp_code': 'EMP. Code'
        }
        
    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__( *args, **kwargs )    
        self.fields['position'].empty_label = 'select'