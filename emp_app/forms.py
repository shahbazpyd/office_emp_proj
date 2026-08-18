from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # We exclude hire_date since it's automatically set to datetime.now() in our view
        fields = ['first_name', 'last_name', 'dept', 'role', 'salary', 'bonus', 'phone']
        
        # We define widgets to inject Bootstrap classes so we don't lose our nice UI
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Jane'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Doe'}),
            'dept': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '60000'}),
            'bonus': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '5000'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1234567890'}),
        }
