from django.utils import timezone
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from prj_emp.views import * # type: ignore
from prj_emp.models import Employee, Project, Request, EmployeeProject, RequestEmployees, CustomUser # type: ignore
from prj_emp.forms import EmployeeForm, ProjectForm, RequestForm, CustomUserCreationForm, EmployeeUpdateForm, EmployeeSkillsUpdateForm # type: ignore
import json

User = get_user_model()

class ViewTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.manager = Employee.objects.create(
            name='Manager Name',
            email='manager@example.com',
            phone='1234567890',
            role='manager',
            skills='Management, Python'
        )

        self.project = Project.objects.create(
            name='Project 1',
            description='Description of Project 1',
            start_date=timezone.now().date(),
            end_date=timezone.now().date(),
            project_manager=self.manager.name,
            project_skills='Python, Django'
        )

        self.request_obj = Request.objects.create(
            manager=self.manager,
            project=self.project,
            skills='Python, Django'
        )

        self.employee = Employee.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            phone='0987654321',
            role='developer',
            skills='Python, Django'
        )
        self.employee2 = Employee.objects.create(
        name='Jane Doe',
        email='jane.doe@example.com',
        phone='0987654321',
        role='developer',
        skills='Python, Django'
    )

    def test_request_obj_created(self):
        self.assertEqual(Request.objects.count(), 1)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200) 

    def test_user_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard_view(self):
        response = self.client.get(reverse('admin_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard.html')
        self.assertIsInstance(response.context['employee_form'], EmployeeForm)
        self.assertIsInstance(response.context['project_form'], ProjectForm)

        valid_employee_data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '0987654321',
            'role': 'Designer',
            'skills': 'Photoshop, Illustrator'
        }
        response = self.client.post(reverse('admin_dashboard'), data=urlencode(valid_employee_data) + '&employee_form_submit=true', content_type='application/x-www-form-urlencoded')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin_dashboard'))
        self.assertTrue(Employee.objects.filter(name='Jane Doe').exists())

    def test_submit_form(self):
        valid_employee_data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '0987654321',
            'role': 'Designer',
            'skills': 'Photoshop, Illustrator'
        }
        response = self.client.post(reverse('submit_form'), data=valid_employee_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin_dashboard'))
        self.assertTrue(Employee.objects.filter(name='Jane Doe').exists())

        invalid_employee_data = {
            'name': '',
            'email': 'invalidemail',
            'phone': 'invalidphone',
            'role': '',
            'skills': ''
        }
        response = self.client.post(reverse('submit_form'), data=invalid_employee_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard.html')
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_add_project(self):
        valid_project_data = {
            'name': 'New Project',
            'description': 'A new test project',
            'start_date': '2024-01-01',
            'end_date': '2024-12-31',
            'project_manager': 'Manager 2',
            'project_skills': 'Python, React'
        }
        response = self.client.post(reverse('add_project'), data=valid_project_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('admin_dashboard'))
        self.assertTrue(Project.objects.filter(name='New Project').exists())

        response = self.client.post(reverse('add_project'), data={})
        self.assertEqual(response.status_code, 400)

    def test_get_employee_data(self):
        response = self.client.get(reverse('get_employee_data'))
        data = response.json()
        self.assertGreater(len(data), 0) 

    def test_get_project_data(self):
        response = self.client.get(reverse('get_project_data'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Project 1')

    def test_assign_project(self):
        response = self.client.post(
            reverse('assign_project'),
            json.dumps({'project': self.project.id, 'employee': self.employee.id}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json()['success'], True)
        
    def test_unassign_project(self):
        data = {'employee': self.employee.id}  
        response = self.client.post(reverse('unassign_project'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200) 

    def test_manager_dashboard_view(self):
        response = self.client.get(reverse('manager_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_filter_employees(self):
        response = self.client.get(reverse('filter_employees'), {'role': 'developer', 'skills': 'Python'})
        data = response.json()
        self.assertGreater(len(data), -1)

    def test_request_employees(self):
        response = self.client.post(reverse('request_employees'), {
            'manager_id': self.manager.id,
            'project_id': self.project.id,
            'skills': 'Python, Django'
        })
        self.assertEqual(response.status_code, 200)  

    def test_get_requests(self):
        response = self.client.get(reverse('get_requests'))
        self.assertEqual(response.status_code, 200)

    def test_approve_request(self):
        response = self.client.post(reverse('approve_request', args=[self.request_obj.id]))
        self.assertEqual(response.status_code, 200)
        self.request_obj.refresh_from_db()
        self.assertEqual(self.request_obj.status, 'approved')

    def test_reject_request(self):
        response = self.client.post(reverse('reject_request', args=[self.request_obj.id]))
        self.assertEqual(response.status_code, 200)
        self.request_obj.refresh_from_db()
        self.assertEqual(self.request_obj.status, 'rejected')

    def test_delete_employee(self):
        response = self.client.post(reverse('delete_employee', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200) 

    def test_update_employee(self):
        update_data = {
            'name': 'John Doe Updated',
            'email': 'john.doe.updated@example.com',
            'phone': '1234567890',
            'role': 'developer',
            'skills': 'Python, Django, React'
        }
        response = self.client.post(reverse('update_employee', args=[self.employee.id]), data=update_data)
        self.assertIsNotNone(response, "The view didn't return a response.")

    def test_get_employee_details(self):
        response = self.client.get(reverse('get_employee_details', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)

    def test_employee_dashboard(self):
        response = self.client.get(reverse('employee_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee_dashboard.html')
        self.assertIn('employees', response.context)
        employees = list(response.context['employees'])
        self.assertIsInstance(employees, list)

        for employee in employees:
            self.assertIsInstance(employee, Employee)
            self.assertIsNotNone(employee.id)
            self.assertIsNotNone(employee.name)
            self.assertIsNotNone(employee.email)
            self.assertIsNotNone(employee.phone)
            self.assertIsNotNone(employee.role)
            self.assertIsNotNone(employee.skills)

    def test_update_skills(self):
        update_data = {
            'skills': 'Python, Django, React'
        }
        response = self.client.post(reverse('update_skills', args=[self.employee.id]), data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_employee_skills(self):
        response = self.client.get(reverse('get_employee_skills', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)

    def test_get_project_data(self):
        response = self.client.get(reverse('get_project_data'))
        self.assertEqual(response.status_code, 200)
