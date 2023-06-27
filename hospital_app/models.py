# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# # Overriding the Default Django Auth User and adding One More Field (user_type)


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, "Admin"),
        (2, "Doctor"),
        (3, "Pharmacist"),
        (4, "Receptionist"),
        (5, "Accountant"),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

# Rest of your models and signals...



class Admin(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Doctor(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor_profile')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pharmacist(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='pharmacist_profile')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Receptionist(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='receptionist_profile')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Accountant(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='accountant_profile')
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Patient Model
class Patient(models.Model):
    name = models.CharField(max_length=100)


# Prescription Model
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)


# Schedule Model
class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()


# FinancialReport Model
class FinancialReport(models.Model):
    accountant = models.ForeignKey(Accountant, on_delete=models.CASCADE)
    report_text = models.TextField()


# Medication Model
class Medication(models.Model):
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


# PresenceAbsence Model
class PresenceAbsence(models.Model):
    receptionist = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=True)


# Creating Django Signals

# It's like a trigger in the database. It will run only when data is added in the CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data for Admin, Doctor, Pharmacist, Receptionist, or Accountant
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        elif instance.user_type == 2:
            Doctor.objects.create(admin=instance)
        elif instance.user_type == 3:
            Pharmacist.objects.create(admin=instance)
        elif instance.user_type == 4:
            Receptionist.objects.create(admin=instance)
        elif instance.user_type == 5:
            Accountant.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin_profile.save()
    elif instance.user_type == 2:
        instance.doctor_profile.save()
    elif instance.user_type == 3:
        instance.pharmacist_profile.save()
    elif instance.user_type == 4:
        instance.receptionist_profile.save()
    elif instance.user_type == 5:
        instance.accountant_profile.save()
