from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser, Request, RequestEmployees, Employee, Project, EmployeeProject
from django.contrib import messages
from .forms import CustomUserCreationForm, EmployeeUpdateForm, EmployeeForm, EmployeeSkillsUpdateForm, ProjectForm, RequestForm
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.db.models import Q
from django.urls import reverse
import logging
import json
import traceback

logger = logging.getLogger('django')

def home(request):
    logger.info('Home view accessed')
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            logger.info('User registered successfully')
            return redirect('register')
        else:
            logger.warning(f'User registration failed: {form.errors}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            logger.info(f'User {username} logged in successfully')
            if user.user_type == 'admin':
                return redirect('admin_dashboard')
            elif user.user_type == 'manager':
                return redirect('manager_dashboard')
            else:
                return redirect('employee_dashboard')
        else:
            logger.warning(f'Login failed for username: {username}')
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def admin_dashboard_view(request):
    employee_form = EmployeeForm()
    project_form = ProjectForm()
    projects = Project.objects.all()
    employees = Employee.objects.all()

    if request.method == 'POST':
        if 'employee_form_submit' in request.POST:
            employee_form = EmployeeForm(request.POST)
            if employee_form.is_valid():
                employee_form.save()
                logger.info('Employee form submitted and saved successfully')
                return redirect('admin_dashboard')
        elif 'project_form_submit' in request.POST:
            project_form = ProjectForm(request.POST)
            if project_form.is_valid():
                project_form.save()
                logger.info('Project form submitted and saved successfully')
                return redirect('admin_dashboard')
        elif 'updateEmployee' in request.POST:
            employee_form = EmployeeForm()

    return render(request, 'admin_dashboard.html', {'employee_form': employee_form, 'project_form': project_form, 'employees': employees})

def submit_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Employee form submitted and saved successfully')
            return redirect('admin_dashboard')
        else:
            logger.warning(f'Employee form submission failed: {form.errors}')
            return render(request, 'admin_dashboard.html', {'form': form})
    else:
        form = EmployeeForm()
    return render(request, 'admin_dashboard.html', {'form': form})

def add_project(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            project_manager = request.POST.get('project_manager')
            project_skills = request.POST.get('project_skills')
            
            project = Project.objects.create(
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                project_manager=project_manager,
                project_skills=project_skills
            )
            logger.info(f'Project "{name}" added successfully')
            return redirect('admin_dashboard')
        except Exception as e:
            logger.error(f'Error adding project: {e}')
            return HttpResponseBadRequest('Failed to add project')

    return render(request, 'admin_dashboard.html')

def get_employee_data(request):
    employees = Employee.objects.all()
    data = [{'id': emp.id, 'name': emp.name, 'email': emp.email, 'phone': emp.phone, 'role': emp.role, 'skills': emp.skills} for emp in employees]
    logger.info('Employee data retrieved')
    return JsonResponse(data, safe=False)

def get_project_data(request):
    projects = Project.objects.all()
    data = [{'id': project.id, 'name': project.name, 'description': project.description, 'start_date': project.start_date, 'end_date': project.end_date, 'project_manager': project.project_manager, 'project_skills': project.project_skills} for project in projects]
    logger.info('Project data retrieved')
    return JsonResponse(data, safe=False)

def assign_project(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            project_id = data.get('project')
            employee_id = data.get('employee')

            project = Project.objects.get(pk=project_id)
            employee = Employee.objects.get(pk=employee_id)

            existing_assignment = EmployeeProject.objects.filter(employee=employee, project=project).first()
            if existing_assignment:
                logger.info(f'Project {project_id} already assigned to employee {employee_id}')
                return JsonResponse({'success': True, 'message': 'Project already assigned to employee.'})

            EmployeeProject.objects.create(employee=employee, project=project)
            logger.info(f'Project {project_id} assigned to employee {employee_id} successfully')
            return JsonResponse({'success': True, 'message': 'Project assigned to employee successfully.'})
        except (Project.DoesNotExist, Employee.DoesNotExist):
            logger.error('Project or employee not found')
            return JsonResponse({'success': False, 'error': 'Project or employee not found.'}, status=404)
        except Exception as e:
            logger.error(f'Error assigning project: {e}')
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        logger.warning('Method not allowed for assign_project')
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

def unassign_project(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            employee_id = data.get('employee')

            employee_project = EmployeeProject.objects.get(employee_id=employee_id)
            employee_project.delete()
            logger.info(f'Project unassigned from employee {employee_id} successfully')
            return JsonResponse({'success': True, 'message': 'Project unassigned from employee successfully.'})
        except EmployeeProject.DoesNotExist:
            logger.error('Employee project not found')
            return JsonResponse({'success': False, 'error': 'Employee project not found.'})
        except Exception as e:
            logger.error(f'Error unassigning project: {e}')
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        logger.warning('Method not allowed for unassign_project')
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

def manager_dashboard_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save()
            selected_employees = request.POST.getlist('selected_employees')
            for employee_id in selected_employees:
                RequestEmployees.objects.create(request=request_obj, employee_id=employee_id)
            logger.info('Request form submitted and saved successfully')
            return redirect('manager_dashboard')
    else:
        form = RequestForm()

    available_employees = Employee.objects.exclude(id__in=EmployeeProject.objects.values('employee_id'))
    return render(request, 'manager_dashboard.html', {'form': form, 'employees': available_employees})

def filter_employees(request):
    skills = request.GET.get('skills', '')
    unassigned = request.GET.get('unassigned', '') == 'true'

    employees = Employee.objects.all()
    if skills:
        employees = employees.filter(skills__icontains=skills)
    if unassigned:
        employees = employees.filter(
            Q(id__in=Employee.objects.exclude(id__in=EmployeeProject.objects.values('employee_id'))) |
            Q(id__in=Employee.objects.filter(id__in=EmployeeProject.objects.filter(project__isnull=True).values('employee_id')))
        )

    employee_data = [{'id': emp.id, 'name': emp.name, 'email': emp.email, 'phone': emp.phone, 'role': emp.role, 'skills': emp.skills} for emp in employees]
    logger.info('Filtered employee data retrieved')
    return JsonResponse(employee_data, safe=False)

def request_employees(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save()
            selected_employees = request.POST.getlist('selected_employees')
            for employee_id in selected_employees:
                RequestEmployees.objects.create(request=request_obj, employee_id=employee_id)
            logger.info('Request form submitted and saved successfully')
            return redirect('manager_dashboard')
    else:
        form = RequestForm()

    available_employees = Employee.objects.exclude(id__in=EmployeeProject.objects.values('employee_id'))
    return render(request, 'manager_dashboard.html', {'form': form, 'employees': available_employees})

def get_requests(request):
    requests = Request.objects.all()
    request_data = [{'id': req.id, 'manager_id': req.manager.id, 'project_id': req.project.id, 'skills': req.skills, 'status': req.status, 'employee_ids': list(RequestEmployees.objects.filter(request=req).values_list('employee_id', flat=True))} for req in requests]
    logger.info('Request data retrieved')
    return JsonResponse(request_data, safe=False)

def approve_request(request, request_id):
    if request.method == 'POST':
        req = get_object_or_404(Request, id=request_id)
        req.status = 'approved'
        req.save()

        employee_ids = list(RequestEmployees.objects.filter(request_id=request_id).values_list('employee_id', flat=True))
        project_id = req.project_id

        for employee_id in employee_ids:
            EmployeeProject.objects.create(employee_id=employee_id, project_id=project_id)
        logger.info(f'Request {request_id} approved and EmployeeProject records created')
        return JsonResponse({'message': 'Request approved and EmployeeProject records created'})

    logger.warning('Invalid request method for approve_request')
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def reject_request(request, request_id):
    try:
        req = get_object_or_404(Request, id=request_id)
        req.status = 'rejected'
        req.save()
        logger.info(f'Request {request_id} rejected successfully')
        return JsonResponse({'message': 'Request rejected successfully.'})
    except Exception as e:
        logger.error(f'Error rejecting request {request_id}: {e}')
        return JsonResponse({'error': str(e)}, status=400)

def delete_employee(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        employee.delete()
        logger.info(f'Employee {employee_id} deleted successfully')
        return JsonResponse({'message': 'Employee deleted successfully'}, status=200)
    except Employee.DoesNotExist:
        logger.error(f'Employee {employee_id} not found')
        return JsonResponse({'error': 'Employee not found'}, status=404)
    except Exception as e:
        logger.error(f'Error deleting employee {employee_id}: {e}')
        return JsonResponse({'error': str(e)}, status=500)

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        form = EmployeeUpdateForm(data, instance=employee)
        if form.is_valid():
            form.save()
            logger.info(f'Employee {employee_id} details updated successfully')
            return JsonResponse({'message': 'Employee details updated successfully'})
        else:
            logger.warning(f'Form validation failed for employee {employee_id}: {form.errors}')
            return JsonResponse({'message': 'Form is not valid'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

def get_employee_details(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    data = {'name': employee.name, 'email': employee.email, 'phone': employee.phone, 'role': employee.role, 'skills': employee.skills}
    logger.info(f'Employee details retrieved for employee {employee_id}')
    return JsonResponse(data)

def employee_dashboard(request):
    employees = Employee.objects.all()
    logger.info('Employee dashboard accessed')
    return render(request, 'employee_dashboard.html', {'employees': employees})

def update_skills(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        form = EmployeeSkillsUpdateForm(data, instance=employee)
        if form.is_valid():
            form.save()
            logger.info(f'Skills updated for employee {employee_id}')
            return JsonResponse({'message': 'Employee skills updated successfully'})
        else:
            logger.warning(f'Skills update form validation failed for employee {employee_id}: {form.errors}')
            return JsonResponse({'message': 'Form is not valid', 'errors': form.errors}, status=400)
    logger.warning('Invalid request method for update_skills')
    return JsonResponse({'message': 'Invalid request method'}, status=400)

def get_employee_skills(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    data = {'skills': employee.skills}
    logger.info(f'Skills retrieved for employee {employee_id}')
    return JsonResponse(data)

def get_project_info(request, employee_id):
    try:
        employee_project = EmployeeProject.objects.get(employee_id=employee_id)
        project = employee_project.project
        data = {'project_id': project.id, 'project_name': project.name, 'project_manager': project.project_manager}
        logger.info(f'Project info retrieved for employee {employee_id}')
        return JsonResponse(data)
    except EmployeeProject.DoesNotExist:
        logger.error(f'No project found for employee {employee_id}')
        return JsonResponse({'error': 'No project found for the given employee ID'}, status=404)
