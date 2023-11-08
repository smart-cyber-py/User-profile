from django.urls import path
from .views import *
from django.contrib.auth import views
urlpatterns = [
    path('',landing,name="landing"),
    path('dashboard/',dashboard,name="dashboard"),
    path('dashboard/<str:username>/edit/',edit_profile.as_view(),name="edit_profile"),
    path('register/',register,name='register'),
    # user login and logout urls
    
    path('login/',views.LoginView.as_view(),name="login"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    
    # user change password
    path("password_change/",views.PasswordChangeView.as_view(),name="password_change"),
    path('password_change/done/',views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    # user password reset
    
    path("password_reset/",views.PasswordResetView.as_view(),name="password_reset"),
    path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("password_reset_complete/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]