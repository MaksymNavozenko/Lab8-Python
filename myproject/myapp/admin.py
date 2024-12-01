from django.contrib import admin
from .models import Employee, Department, Position, Project, ProjectExecution


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_code', 'last_name', 'first_name', 'middle_name', 'phone', 'education', 'department_code', 'position_code')
    search_fields = ('employee_code', 'last_name', 'first_name', 'middle_name', 'phone')
    list_filter = ('education', 'department_code', 'position_code')
    ordering = ('last_name', 'first_name')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_code', 'name', 'phone', 'room_number')
    search_fields = ('department_code', 'name', 'phone')
    list_filter = ('room_number',)
    ordering = ('name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_code', 'title', 'salary', 'bonus_percent')
    search_fields = ('position_code', 'title')
    ordering = ('title',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_number', 'name', 'deadline', 'budget')
    search_fields = ('project_number', 'name')
    list_filter = ('deadline',)
    ordering = ('deadline',)


@admin.register(ProjectExecution)
class ProjectExecutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'execution_code', 'project_number', 'department_code', 'start_date')
    search_fields = ('execution_code', 'project_number__name', 'department_code__name')
    list_filter = ('start_date', 'department_code')
    ordering = ('start_date',)
