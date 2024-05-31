from django.test import TestCase
from prj_emp.forms import CustomUserCreationForm, EmployeeForm, ProjectForm, RequestForm, EmployeeUpdateForm, EmployeeSkillsUpdateForm # type: ignore
from prj_emp.models import Project, Employee  # type: ignore 


class CustomUserCreationFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'aStrongerPassword123!',
            'password2': 'aStrongerPassword123!',
            'user_type': 'employee',
            'name': 'Test User'
        }
        form = CustomUserCreationForm(data)
        self.assertTrue(form.is_valid(), msg=form.errors)


    def test_invalid_form(self):
        data = {
            'username': '',
            'email': 'invalid-email',
            'password1': 'password123',
            'password2': 'differentpassword',
            'user_type': 'employee',
            'name': ''
        }
        form = CustomUserCreationForm(data)
        self.assertFalse(form.is_valid())

class EmployeeFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'role': 'Developer',
            'skills': 'Python, Django'
        }
        form = EmployeeForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'email': 'invalid-email',
            'phone': '',
            'role': '',
            'skills': ''
        }
        form = EmployeeForm(data)
        self.assertFalse(form.is_valid())

class ProjectFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'name': 'Project X',
            'description': 'A test project',
            'start_date': '2023-01-01',
            'end_date': '2023-12-31',
            'project_manager': 1,  
            'project_skills': 'Python, Django'
        }
        form = ProjectForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',
            'description': '',
            'start_date': '',
            'end_date': '',
            'project_manager': '',
            'project_skills': ''
        }
        form = ProjectForm(data)
        self.assertFalse(form.is_valid())


class RequestFormTest(TestCase):

    def setUp(self):
        self.manager = Employee.objects.create(
            name='Manager Name',
            email='manager@example.com',
            phone='1234567890',
            role='Manager',
            skills='Management'
        )

        self.project = Project.objects.create(
            name='Project1',
            description='A test project',
            start_date='2023-01-01',
            end_date='2023-12-31',
            project_manager='Project Manager Name',  
            project_skills='Python, Django'
        )

    def test_valid_form(self):
        data = {
            'project': self.project.id,
            'skills': 'Python, Django',
            'manager': self.manager.id
        }
        form = RequestForm(data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_invalid_form(self):
        data = {
            'project': '',
            'skills': '',
            'manager': ''
        }
        form = RequestForm(data)
        self.assertFalse(form.is_valid())

class EmployeeUpdateFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '0987654321',
            'role': 'Tester',
            'skills': 'Automation, Selenium'
        }
        form = EmployeeUpdateForm(data)
        self.assertTrue(form.is_valid())

    def test_optional_fields(self):
        data = {
            'name': '',
            'email': '',
            'phone': '',
            'role': '',
            'skills': ''
        }
        form = EmployeeUpdateForm(data)
        self.assertTrue(form.is_valid())

class EmployeeSkillsUpdateFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'skills': 'React, JavaScript'
        }
        form = EmployeeSkillsUpdateForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'skills': ''
        }
        form = EmployeeSkillsUpdateForm(data)
        self.assertFalse(form.is_valid())
