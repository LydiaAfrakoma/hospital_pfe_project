from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser



from .forms import (
    DoctorForm, PharmacistForm, AccountantForm, ReceptionistForm, PresenceAbsenceForm,
    MedicationForm, PatientForm, PrescriptionForm, ScheduleForm,
    FinancialReportForm, AccountUpdateForm, DoctorScheduleForm, AssignPatientForm,LoginForm
)
from hospital_app.models import Doctor, Pharmacist, Accountant, Receptionist, PresenceAbsence, Medication, Patient, Prescription, Schedule, FinancialReport



#Authentification Part 



def loginPage(request):
    if request.method == 'POST':
        # Process the form data and authenticate the user
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication succeeded, log in the user
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL name
        else:
            # User authentication failed, display an error message
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Display the login form
        return render(request, 'login.html')


from django.views.decorators.http import require_POST

@require_POST
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == 1:  # Admin
                return redirect('admin_home')
            elif user_type == 2:  # Doctor
                return redirect('doctor_home')
            elif user_type == 3:  # Pharmacist
                return redirect('pharmacist_home')
            elif user_type == 4:  # Receptionist
                return redirect('receptionist_home')
            elif user_type == 5:  # Accountant
                return redirect('accountant_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')


#Log Out 

def logout_user(request):
    logout(request)
    # Redirect to the desired page after logout
    return redirect('home')  # Update 'home' with the URL name of your homepage

def get_user_details(request):
    if request.user.is_authenticated:
        user = request.user
        return HttpResponse("User: " + user.email + " User Type: " + str(user.user_type))
    else:
        return HttpResponse("Please Login First")


# Admin Views

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = DoctorForm()
    return render(request, 'create_doctor.html', {'form': form})


def create_pharmacist(request):
    if request.method == 'POST':
        form = PharmacistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = PharmacistForm()
    return render(request, 'create_pharmacist.html', {'form': form})


def create_accountant(request):
    if request.method == 'POST':
        form = AccountantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = AccountantForm()
    return render(request, 'create_accountant.html', {'form': form})


def create_receptionist(request):
    if request.method == 'POST':
        form = ReceptionistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = ReceptionistForm()
    return render(request, 'create_receptionist.html', {'form': form})


def manage_presence_absence(request):
    if request.method == 'POST':
        form = PresenceAbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = PresenceAbsenceForm()
    return render(request, 'manage_presence_absence.html', {'form': form})


# Pharmacist View

def manage_medications(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = MedicationForm()
    return render(request, 'manage_medications.html', {'form': form})


# Doctor Views

def manage_patients(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = PatientForm()
    return render(request, 'manage_patients.html', {'form': form})


def manage_prescriptions(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = PrescriptionForm()
    return render(request, 'manage_prescriptions.html', {'form': form})


def schedule_patients(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = ScheduleForm()
    return render(request, 'schedule_patients.html', {'form': form})


# Accountant Views

def provide_financial_reports(request):
    if request.method == 'POST':
        form = FinancialReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = FinancialReportForm()
    return render(request, 'provide_financial_reports.html', {'form': form})


def update_account(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = AccountUpdateForm()
    return render(request, 'update_account.html', {'form': form})


# Receptionist Views

def take_presence_absence_list(request):
    if request.method == 'POST':
        form = PresenceAbsenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = PresenceAbsenceForm()
    return render(request, 'take_presence_absence_list.html', {'form': form})


def view_doctor_schedules(request):
    if request.method == 'POST':
        form = DoctorScheduleForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            schedules = Schedule.objects.filter(doctor=doctor)
            return render(request, 'view_doctor_schedules.html', {'doctor': doctor, 'schedules': schedules})
    else:
        form = DoctorScheduleForm()
    return render(request, 'view_doctor_schedules.html', {'form': form})


def assign_patients(request):
    if request.method == 'POST':
        form = AssignPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
    else:
        form = AssignPatientForm()
    return render(request, 'assign_patients.html', {'form': form})
