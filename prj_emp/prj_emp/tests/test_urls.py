from django.test import TestCase, Client
from django.urls import reverse, resolve
from prj_emp.models import CustomUser, Employee, Project, Request, EmployeeProject # type: ignore
from prj_emp import views # type: ignore
import json

class UrlTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', email='testuser@example.com')
        self.employee = Employee.objects.create(name='Test Employee', email='testemployee@example.com', phone='1234567890', role='Developer', skills='Python, Django')
        self.project = Project.objects.create(name='Test Project', description='Test Project Description', start_date='2023-01-01', end_date='2023-12-31', project_manager='Manager Name', project_skills='Python, Django')
        self.employee_project = EmployeeProject.objects.create(employee=self.employee, project=self.project)
        self.client.login(username='testuser', password='testpassword')

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.user_login)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard_url(self):
        url = reverse('admin_dashboard')
        self.assertEqual(resolve(url).func, views.admin_dashboard_view)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_submit_form_url(self):
        url = reverse('submit_form')
        self.assertEqual(resolve(url).func, views.submit_form)
        response = self.client.post(url, {'name': 'Form Name', 'description': 'Form Description'})
        self.assertEqual(response.status_code, 200)

    def test_add_project_url(self):
        url = reverse('add_project')
        self.assertEqual(resolve(url).func, views.add_project)
        data = {
            'name': 'New Project',
            'description': 'New Project Description',
            'start_date': '2024-06-01',  
            'end_date': '2024-12-31',   
            'project_manager': 'Manager Name',
            'project_skills': 'Python, Django'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) 

    def test_get_employee_data_url(self):
        url = reverse('get_employee_data')
        self.assertEqual(resolve(url).func, views.get_employee_data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_get_project_data_url(self):
        url = reverse('get_project_data')
        self.assertEqual(resolve(url).func, views.get_project_data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_assign_project_url(self):
        url = reverse('assign_project')
        self.assertEqual(resolve(url).func, views.assign_project)
        data = json.dumps({'employee': self.employee.id, 'project': self.project.id})
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_unassign_project_url(self):
        url = reverse('unassign_project')
        self.assertEqual(resolve(url).func, views.unassign_project)
        data = json.dumps({'employee': self.employee.id})
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

        self.employee.refresh_from_db()
        self.assertNotIn(self.project, self.employee.project_set.all())

    def test_manager_dashboard_url(self):
        url = reverse('manager_dashboard')
        self.assertEqual(resolve(url).func, views.manager_dashboard_view)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_filter_employees_url(self):
        url = reverse('filter_employees')
        self.assertEqual(resolve(url).func, views.filter_employees)
        response = self.client.get(url, {'skill': 'Python', 'availability': 'Full-Time'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_request_employees_url(self):
        url = reverse('request_employees')
        self.assertEqual(resolve(url).func, views.request_employees)
        response = self.client.post(url, {'project_id': self.project.id, 'skills_required': 'Python, Django'})
        self.assertEqual(response.status_code, 200)  

    def test_get_requests_url(self):
        url = reverse('get_requests')
        self.assertEqual(resolve(url).func, views.get_requests)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_approve_request_url(self):
        request = Request.objects.create(manager=self.employee, project=self.project, skills='Python')
        url = reverse('approve_request', args=[request.id])
        self.assertEqual(resolve(url).func, views.approve_request)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        request.refresh_from_db()
        self.assertEqual(request.status, 'approved')

    def test_reject_request_url(self):
        request = Request.objects.create(manager=self.employee, project=self.project, skills='Python')
        url = reverse('reject_request', args=[request.id])
        self.assertEqual(resolve(url).func, views.reject_request)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        request.refresh_from_db()
        self.assertEqual(request.status, 'rejected')

    def test_delete_employee_url(self):
        url = reverse('delete_employee', args=[self.employee.id])
        self.assertEqual(resolve(url).func, views.delete_employee)
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(Employee.DoesNotExist):
            Employee.objects.get(id=self.employee.id)

    def test_get_employee_details_url(self):
        url = reverse('get_employee_details', args=[self.employee.id])
        self.assertEqual(resolve(url).func, views.get_employee_details)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_update_employee_url(self):
        url = reverse('update_employee', args=[self.employee.id])
        self.assertEqual(resolve(url).func, views.update_employee)
        data = {'name': 'Updated Employee Name', 'role': 'Senior Developer'}
        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Employee details updated successfully')

        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, 'Updated Employee Name')
        self.assertEqual(self.employee.role, 'Senior Developer')

    def test_employee_dashboard_url(self):
        url = reverse('employee_dashboard')
        self.assertEqual(resolve(url).func, views.employee_dashboard)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_skills_url(self):
        url = reverse('update_skills', args=[self.employee.id])
        self.assertEqual(resolve(url).func, views.update_skills)
        data = {
            'skills': 'Python, Django, React'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Employee skills updated successfully')

    def test_get_employee_skills_url(self):
        url = reverse('get_employee_skills', args=[self.employee.id])
        self.assertEqual(resolve(url).func, views.get_employee_skills)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_get_project_info_url(self):
        url = reverse('get_project_info', args=[self.employee.id])
        self.assertEqual(resolve(url).func, views.get_project_info)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
