from django import forms
from .models import Baptism,ParishDetails,LoginDetails,BaptismAdvanced,FieldTable

class BaptismForm(forms.ModelForm):
    class Meta:
        model = Baptism
        fields = [
            'place_of_baptism',
            'date_of_baptism',
            'time_of_baptism',
            'child_name_first',
            'child_name_second',
            'dob',
            'mother_name',
            'father_name',
            'contact_no',
            'email',
        ]
        widgets = {
            'date_of_baptism': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_of_baptism': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }




class ParishDetailsForm(forms.ModelForm):
    class Meta:
        model = ParishDetails
        fields = [
            'parent_parish_id', 'name_of_parish', 'place_of_parish', 
            'address', 'email', 'contact_no', 'status'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4}),
        }


from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import LoginDetails

class LoginForm(forms.Form):
    user_name = forms.CharField(max_length=255, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get('user_name')
        password = cleaned_data.get('password')

        if user_name and password:
            try:
                user = User.objects.get(username=user_name)
            except User.DoesNotExist:
                raise forms.ValidationError("User does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Invalid password")

            try:
                login_details = user.logindetails  # Access related LoginDetails
                if login_details.status == 'Inactive':
                    raise forms.ValidationError("Account is inactive")
            except LoginDetails.DoesNotExist:
                raise forms.ValidationError("User details not found")

        return cleaned_data



from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from .models import LoginDetails


from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, Group
from .models import LoginDetails

class RegisterForm(forms.ModelForm):
    user_name = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)  # To confirm the password
    role = forms.ChoiceField(choices=LoginDetails.ROLE_CHOICES)
    contact_no = forms.CharField(max_length=15)
    email = forms.EmailField()
    status = forms.ChoiceField(choices=LoginDetails.STATUS_CHOICES, initial='Active')  # Default to Active
    parish_id = forms.IntegerField(initial=1)  # Set default to 1 if not provided

    class Meta:
        model = LoginDetails
        fields = ['user_name', 'password', 'contact_no', 'email', 'role', 'status', 'parish_id']

    def clean_user_name(self):
        username = self.cleaned_data['user_name']
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists. Please choose another one.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Check if the passwords match
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        # Create the user
        user = User.objects.create_user(
            username=self.cleaned_data['user_name'],
            password=self.cleaned_data['password'],  # This automatically hashes the password
            email=self.cleaned_data['email']
        )

        # Save the LoginDetails, link it to the created User
        login_details = super().save(commit=False)
        login_details.user = user
        if commit:
            login_details.save()

        # Assign the user to the corresponding group based on role
        self.assign_group(user, self.cleaned_data['role'])

        return user  # Return the created user

    def assign_group(self, user, role):
        try:
            group = Group.objects.get(name=role)  # Assuming the 'role' is the group name
            user.groups.add(group)
        except Group.DoesNotExist:
            # Handle case where the group doesn't exist
            pass







class BaptismAdvancedForm(forms.ModelForm):
    class Meta:
        model = BaptismAdvanced
        fields = [
            'basic_baptism_id',
            'q_id',
            'priest_id',
            'question',
            'question_type',
            'compulsary',
            'status',
            'field_id',
            'data_varchar',
        ]
        widgets = {
            'question': forms.Textarea(attrs={'rows': 4}),
        }

class FieldTableForm(forms.ModelForm):
    class Meta:
        model = FieldTable
        fields = ['order_no', 'type', 'data', 'choice', 'q_id', 'status']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.Textarea(attrs={'class': 'form-control'}),
            'choice': forms.Select(attrs={'class': 'form-control'}),
            'order_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'q_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

