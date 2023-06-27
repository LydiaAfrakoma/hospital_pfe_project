from django.urls import path
from . import views

urlpatterns = [
    # Login URLs
   # Login URLs
    path('login/', views.loginPage, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),  # Updated URL pattern with trailing slash
    path('user-details/', views.get_user_details, name='user_details'),
    path('logout/', views.logout_user, name='logout'),

    # Admin URLs
    path('create-doctor/', views.create_doctor, name='create_doctor'),
    path('create-pharmacist/', views.create_pharmacist, name='create_pharmacist'),
    path('create-accountant/', views.create_accountant, name='create_accountant'),
    path('create-receptionist/', views.create_receptionist, name='create_receptionist'),
    path('manage-presence-absence/', views.manage_presence_absence, name='manage_presence_absence'),

    # Pharmacist URLs
    path('manage-medications/', views.manage_medications, name='manage_medications'),

    # Doctor URLs
    path('manage-patients/', views.manage_patients, name='manage_patients'),
    path('manage-prescriptions/', views.manage_prescriptions, name='manage_prescriptions'),
    path('schedule-patients/', views.schedule_patients, name='schedule_patients'),

    # Accountant URLs
    path('provide-financial-reports/', views.provide_financial_reports, name='provide_financial_reports'),
    path('update-account/', views.update_account, name='update_account'),

    # Receptionist URLs
    path('take-presence-absence-list/', views.take_presence_absence_list, name='take_presence_absence_list'),
    path('view-doctor-schedules/', views.view_doctor_schedules, name='view_doctor_schedules'),
    path('assign-patients/', views.assign_patients, name='assign_patients'),
]
