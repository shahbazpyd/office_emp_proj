import csv
from datetime import datetime

from django.db.models import Q, Count, Sum
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee, Department, Role
from .forms import EmployeeForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        total_emps = Employee.objects.count()
        total_salary = Employee.objects.aggregate(Sum('salary'))['salary__sum'] or 0
        
        # Get count of employees per department
        dept_data = list(Employee.objects.values('dept__name').annotate(count=Count('id')))
        
        # Get count of employees per role
        role_data = list(Employee.objects.values('role__name').annotate(count=Count('id')))
        
        context = {
            'total_emps': total_emps,
            'total_salary': total_salary,
            'dept_data': dept_data,
            'role_data': role_data,
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')

@login_required
def all_emp(request):
    emp_list = Employee.objects.all().order_by('-id')
    paginator = Paginator(emp_list, 10)  # Show 10 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'emps': page_obj
    }
    return render(request, 'view_all_emp.html', context)

@login_required
def search_emp_ajax(request):
    query = request.GET.get('q', '')
    if query:
        emps = Employee.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(dept__name__icontains=query) |
            Q(role__name__icontains=query)
        ).order_by('-id')
    else:
        emps = Employee.objects.all().order_by('-id')
    
    data = []
    for emp in emps[:50]: # limit to 50 for search dropdown/results
        data.append({
            'id': emp.id,
            'name': f"{emp.first_name} {emp.last_name}",
            'role': emp.role.name,
            'dept': emp.dept.name,
            'location': emp.dept.location,
            'phone': emp.phone,
            'salary': emp.salary,
            'hire_date': emp.hire_date.strftime("%b %d, %Y") if emp.hire_date else ""
        })
    return JsonResponse({'employees': data})

@login_required
def export_emp_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employees_export.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Department', 'Role', 'Salary', 'Bonus', 'Phone', 'Hire Date'])

    employees = Employee.objects.all().select_related('dept', 'role')
    for emp in employees:
        writer.writerow([
            emp.id, 
            emp.first_name, 
            emp.last_name, 
            emp.dept.name, 
            emp.role.name, 
            emp.salary, 
            emp.bonus, 
            emp.phone, 
            emp.hire_date
        ])
    return response

@login_required
def add_emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            new_emp = form.save(commit=False)
            new_emp.hire_date = datetime.now()
            new_emp.save()
            messages.success(request, f"Employee {new_emp.first_name} {new_emp.last_name} added successfully!")
            return redirect('all_emp')
        else:
            messages.error(request, "There was an error adding the employee. Please check the form.")
    else:
        form = EmployeeForm()
    
    return render(request, 'add_emp.html', {'form': form})

@login_required
def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return redirect('remove_emp')
        except:
            return HttpResponse("Something Went Wrong!")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)

@login_required
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        dept = request.POST.get('dept', '')
        role = request.POST.get('role', '')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Something Went Wrong!")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def create_department(request):
    if request.method == "POST":
        name = request.POST['name']
        location = request.POST['location']
        new_dept = Department(name=name, location=location)
        new_dept.save()
        return redirect('create_department')
    elif request.method == "GET":
        departments = Department.objects.all()
        context = {
            'departments': departments
        }
        return render(request, 'create_department.html', context)
    else:
        return HttpResponse("Something Went Wrong!")

@login_required
def create_role(request):
    if request.method == "POST":
        name = request.POST['name']
        new_role = Role(name=name)
        new_role.save()
        return redirect('create_role')
    elif request.method == "GET":
        roles = Role.objects.all()
        context = {
            'roles': roles
        }
        return render(request, 'create_role.html', context)
    else:
        return HttpResponse("Something Went Wrong!")