from django.shortcuts import render
from .models import Employee, Department, Position, Project, ProjectExecution

def index(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    positions = Position.objects.all()
    projects = Project.objects.all()
    project_executions = ProjectExecution.objects.all()
    return render(request, 'index.html', {
        'employees': employees,
        'departments': departments,
        'positions': positions,
        'projects': projects,
        'project_executions': project_executions,
    })
