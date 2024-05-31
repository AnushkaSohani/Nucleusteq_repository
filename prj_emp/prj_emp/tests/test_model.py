from django.test import TestCase
from prj_emp.models import CustomUser, Employee, Project, EmployeeProject, Request, RequestEmployees # type: ignore
from django.utils import timezone

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='password', user_type='admin')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.user_type, 'admin')

    def test_user_str(self):
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='password', user_type='admin')
        self.assertEqual(str(user), 'testuser')

class EmployeeModelTest(TestCase):
    def test_create_employee(self):
        employee = Employee.objects.create(name='John Doe', email='john@example.com', phone='1234567890', role='Developer', skills='Python, Django')
        self.assertEqual(employee.name, 'John Doe')
        self.assertEqual(employee.email, 'john@example.com')

    def test_employee_str(self):
        employee = Employee.objects.create(name='John Doe', email='john@example.com', phone='1234567890', role='Developer', skills='Python, Django')
        self.assertEqual(str(employee), 'Employee ID: {}'.format(employee.id))

class ProjectModelTest(TestCase):
    def test_create_project(self):
        project = Project.objects.create(name='Project X', description='A project description', start_date=timezone.now(), end_date=timezone.now(), project_manager='Manager X', project_skills='Python, Django')
        self.assertEqual(project.name, 'Project X')
        self.assertEqual(project.project_manager, 'Manager X')

    def test_project_str(self):
        project = Project.objects.create(name='Project X', description='A project description', start_date=timezone.now(), end_date=timezone.now(), project_manager='Manager X', project_skills='Python, Django')
        self.assertEqual(str(project), 'Project ID: {}'.format(project.id))

class EmployeeProjectModelTest(TestCase):
    def test_create_employee_project(self):
        employee = Employee.objects.create(name='John Doe', email='john@example.com', phone='1234567890', role='Developer', skills='Python, Django')
        project = Project.objects.create(name='Project X', description='A project description', start_date=timezone.now(), end_date=timezone.now(), project_manager='Manager X', project_skills='Python, Django')
        emp_proj = EmployeeProject.objects.create(employee=employee, project=project)
        self.assertEqual(emp_proj.employee, employee)
        self.assertEqual(emp_proj.project, project)

class RequestModelTest(TestCase):
    def test_create_request(self):
        manager = Employee.objects.create(name='Manager X', email='manager@example.com', phone='1234567890', role='Manager', skills='Management')
        project = Project.objects.create(name='Project X', description='A project description', start_date=timezone.now(), end_date=timezone.now(), project_manager='Manager X', project_skills='Python, Django')
        request = Request.objects.create(manager=manager, project=project, skills='Python, Django')
        self.assertEqual(request.manager, manager)
        self.assertEqual(request.project, project)

class RequestEmployeesModelTest(TestCase):
    def test_create_request_employee(self):
        employee = Employee.objects.create(name='John Doe', email='john@example.com', phone='1234567890', role='Developer', skills='Python, Django')
        project = Project.objects.create(name='Project X', description='A project description', start_date=timezone.now(), end_date=timezone.now(), project_manager='Manager X', project_skills='Python, Django')
        request = Request.objects.create(manager=employee, project=project, skills='Python, Django')
        req_emp = RequestEmployees.objects.create(employee=employee, request=request)
        self.assertEqual(req_emp.employee, employee)
        self.assertEqual(req_emp.request, request)
