from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    password1 = models.CharField(max_length=128, default='')
    password2 = models.CharField(max_length=128, default='')
    user_type = models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee')], max_length=20)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
        blank=True,
    )

    class Meta:
        unique_together = ('name', 'email')

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    skills = models.TextField()
    def __str__(self):
        return f"Employee ID: {self.id}"
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    project_manager = models.CharField(max_length=100)
    project_skills = models.TextField()
    employees = models.ManyToManyField(Employee, through='EmployeeProject', blank=True)
    def __str__(self):
        return f"Project ID: {self.id}"

class EmployeeProject(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.id} - {self.project.id if self.project else 'No Project'}"

    class Meta:
        db_table = 'prj_emp_employeeproject'
        unique_together = ('employee',) 

class Request(models.Model):
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Request from Manager ID: {self.manager_id}, Project ID: {self.project_id}"
    
class RequestEmployees(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee ID: {self.employee.id}, Request ID: {self.request.id}"