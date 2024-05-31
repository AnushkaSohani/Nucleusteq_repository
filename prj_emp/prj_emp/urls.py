from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('add_project/', views.add_project, name='add_project'),
    path('api/employees/', views.get_employee_data, name='get_employee_data'),
    path('api/projects/', views.get_project_data, name='get_project_data'),
    path('assign_project/', views.assign_project, name='assign_project'),
    path('unassign_project/', views.unassign_project, name='unassign_project'),
    path('manager_dashboard/', views.manager_dashboard_view, name='manager_dashboard'),
    path('api/filter_employees/', views.filter_employees, name='filter_employees'),
    path('api/request_employees/', views.request_employees, name='request_employees'),
    path('api/requests/', views.get_requests, name='get_requests'),
    path('api/requests/<int:request_id>/approve/', views.approve_request, name='approve_request'),
    path('api/requests/<int:request_id>/reject/', views.reject_request, name='reject_request'),
    path('api/employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('admin_dashboard/update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('get_employee_details/<int:employee_id>/', views.get_employee_details, name='get_employee_details'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('admin_dashboard/update_skills/<int:employee_id>/', views.update_skills, name='update_skills'),
    path('get_employee_skills/<int:employee_id>/', views.get_employee_skills, name='get_employee_skills'),
    path('get_project_info/<int:employee_id>/', views.get_project_info, name='get_project_info'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)