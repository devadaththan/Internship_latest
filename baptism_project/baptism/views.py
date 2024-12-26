from django.shortcuts import render, redirect
from .forms import BaptismForm,ParishDetailsForm,BaptismAdvancedForm,FieldTableForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import LoginDetails
from .forms import LoginForm, RegisterForm
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



@login_required
def dashboard(request):
    # Fetch baptism applications associated with the logged-in user
    applications = Baptism.objects.filter(user_id=request.user.id)

    # Print the current user's details to the console
    print(f"Current logged-in user: {request.user.username}")
    print(f"User's email: {request.user.email}")
    print(f"User's ID: {request.user.id}")
    return render(request, 'baptism/dashboard.html', {'applications': applications})


@login_required
def secretary_dashboard(request):
    # Fetch baptism applications associated with the logged-in user
    applications = Baptism.objects.all()

    # # Print the current user's details to the console
    # print(f"Current logged-in user: {request.user.username}")
    # print(f"User's email: {request.user.email}")
    # print(f"User's ID: {request.user.id}")
    return render(request, 'baptism/secretary_dashboard.html', {'applications': applications})


@login_required
def priest_dashboard(request):
    # Fetch baptism applications associated with the logged-in user
    # applications = Baptism

    # # Print the current user's details to the console
    # print(f"Current logged-in user: {request.user.username}")
    # print(f"User's email: {request.user.email}")
    # print(f"User's ID: {request.user.id}")
    return render(request, 'baptism/priest_dashboard.html')



def logout_view(request):
    logout(request)
    return redirect('login')

def homePage(request):
    return render(request, 'baptism/index.html')

@login_required  # Ensure only logged-in users can access this view
def baptism_form_view(request):
    if request.method == "POST":
        form = BaptismForm(request.POST)
        if form.is_valid():
            baptism = form.save(commit=False)  # Don't save to the database yet
            baptism.user_id = request.user.id  # Assign the current logged-in user's ID
            baptism.save()  # Save to the database
            return redirect('field_table_success')  # Replace with your success URL
    else:
        form = BaptismForm()
    return render(request, 'baptism/baptism_form.html', {'form': form})



def upload_parish_details(request):
    if request.method == 'POST':
        form = ParishDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_table_success')  # Redirect to the success page
    else:
        form = ParishDetailsForm()
    return render(request, 'baptism/upload_parish_details.html', {'form': form})


def success_page(request):
    return render(request, 'baptism/success.html')



from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import LoginDetails
from django.utils.timezone import now


from django.contrib.auth.decorators import login_required

def login_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        try:
            # Fetch user details from the custom LoginDetails model
            login_details = LoginDetails.objects.get(user=request.user)
            role = login_details.role  # Assuming you have a 'role' field in your LoginDetails model

            # Redirect to the appropriate dashboard based on the role
            if role == 'Priest':
                return redirect('priest_dashboard')
            elif role == 'Admin':
                return redirect('/admin-dashboard/')
            elif role == 'Public':
                return redirect('dashboard')
            elif role == 'Secretary':
                return redirect('secretary_dashboard')
            else:
                messages.error(request, "Unknown role")
                return redirect('/login/')

        except LoginDetails.DoesNotExist:
            # Fallback if no custom LoginDetails entry exists
            if request.user.is_staff:  # Check for Django's admin users
                return redirect('/admin-dashboard/')
            else:
                return redirect('/user-dashboard/')  # Default user dashboard

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            # First, try checking the custom LoginDetails model
            try:
                login_details = LoginDetails.objects.get(user__username=user_name)
                user = login_details.user  # Access the related User model instance

                if user.check_password(password):
                    login_details.last_login = now()  # Update last login if needed
                    login_details.save()
                    login(request, user)

                    role = login_details.role
                    if role == 'Priest':
                        return redirect('priest_dashboard')
                    elif role == 'Admin':
                        return redirect('/admin-dashboard/')
                    elif role == 'Public':
                        return redirect('dashboard')
                    elif role == 'Secretary':
                        return redirect('secretary_dashboard')
                    else:
                        messages.error(request, "Unknown role")
                        return redirect('/login/')

                else:
                    messages.error(request, "Invalid username or password")
            except LoginDetails.DoesNotExist:
                user = authenticate(request, username=user_name, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Welcome back!")
                    if user.is_staff:
                        return redirect('/admin-dashboard/')
                    else:
                        return redirect('/user-dashboard/')
                else:
                    messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Form is not valid")
    else:
        form = LoginForm()

    return render(request, 'baptism/login.html', {'form': form})





from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import LoginDetails

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the user and login details in a single operation
            user = form.save(commit=True)  # Now only saving once

            messages.success(request, "Account created successfully!")
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')  # Redirect to a page after registration
    else:
        form = RegisterForm()

    return render(request, 'baptism/register.html', {'form': form})







def upload_baptism_advanced(request):
    if request.method == 'POST':
        form = BaptismAdvancedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_table_success')  # Redirect to the desired page
    else:
        form = BaptismAdvancedForm()
    return render(request, 'baptism/upload_baptism_advanced.html', {'form': form})



def upload_field_table(request):
    if request.method == 'POST':
        form = FieldTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_table_success')  # Update this with your success page URL name
    else:
        form = FieldTableForm()
    
    return render(request, 'baptism/upload_field_table.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import BaptismForm
from .models import Baptism



