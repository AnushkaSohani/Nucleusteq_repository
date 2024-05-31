from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Employee  
from .models import Project,Request

class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee')])
    name = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'
        self.fields['user_type'].label = 'User Type'
        self.fields['name'].label = 'Name'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'role', 'skills', ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'project_manager', 'project_skills']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['manager', 'project', 'skills']

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'role', 'skills', ]

    def __init__(self, *args, **kwargs):
        super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False

class EmployeeSkillsUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['skills', ]

