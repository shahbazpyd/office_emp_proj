from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Department, Role, Employee
from .forms import EmployeeForm
from datetime import datetime

class EmployeeAppTests(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

        # Create basic data
        self.dept = Department.objects.create(name='IT', location='New York')
        self.role = Role.objects.create(name='Developer')
        self.emp = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            dept=self.dept,
            role=self.role,
            salary=80000,
            bonus=5000,
            phone=1234567890,
            hire_date=datetime.now()
        )

    def test_department_creation(self):
        """Test that a department model is created correctly"""
        self.assertEqual(self.dept.name, 'IT')
        self.assertEqual(str(self.dept), 'IT')

    def test_employee_creation(self):
        """Test that an employee model is created correctly"""
        self.assertEqual(self.emp.first_name, 'John')
        self.assertEqual(str(self.emp), 'John Doe 1234567890')

    def test_index_view(self):
        """Test the dashboard view loads correctly for an authenticated user"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        # Check context data
        self.assertEqual(response.context['total_emps'], 1)
        self.assertEqual(response.context['total_salary'], 80000)

    def test_all_emp_view(self):
        """Test the view employees page"""
        response = self.client.get(reverse('all_emp'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_employee_form_valid(self):
        """Test that EmployeeForm is valid with correct data"""
        form_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'dept': self.dept.id,
            'role': self.role.id,
            'salary': 90000,
            'bonus': 6000,
            'phone': 9876543210
        }
        form = EmployeeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_employee_form_invalid(self):
        """Test that EmployeeForm is invalid without a first name"""
        form_data = {
            'first_name': '',
            'last_name': 'Smith',
            'dept': self.dept.id,
            'role': self.role.id,
            'salary': 90000,
            'bonus': 6000,
            'phone': 9876543210
        }
        form = EmployeeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
