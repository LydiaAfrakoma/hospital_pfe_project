from django import forms
from .models import Doctor, Pharmacist, Accountant, Receptionist, PresenceAbsence, Medication, Patient, Prescription, Schedule, FinancialReport


#Login Page 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Admin Forms

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['admin', 'address']


class PharmacistForm(forms.ModelForm):
    class Meta:
        model = Pharmacist
        fields = ['admin', 'address']


class AccountantForm(forms.ModelForm):
    class Meta:
        model = Accountant
        fields = ['admin', 'address']


class ReceptionistForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = ['admin', 'address']


class PresenceAbsenceForm(forms.ModelForm):
    class Meta:
        model = PresenceAbsence
        fields = ['doctor', 'date', 'is_present']


# Pharmacist Form

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['pharmacist', 'name']


# Doctor Forms

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'medication', 'dosage']


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'patient', 'appointment_date', 'appointment_time']


# Accountant Forms

class FinancialReportForm(forms.ModelForm):
    class Meta:
        model = FinancialReport
        fields = ['accountant', 'report_text']


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Accountant
        fields = ['admin', 'address']


# Receptionist Forms

class DoctorScheduleForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())


class AssignPatientForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'patient', 'appointment_date', 'appointment_time']
