from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register', views.RegisterUser, name='register'),
    path('signin', views.LoginUser, name='signin'),
    path('logout', views.logoutUser, name='logout'),
    path('join', views.Join, name='join'),
    path('profile', views.userProfile, name='profile'),
    path('settings', views.AccountSettings, name='settings'),

     #password reset
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name ='accounts/password_reset_email.html',
        subject_template_name = 'accounts/password_reset_subject.txt'), 
        name = 'password_reset' ),
    
    path('reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'),
        name = 'password_reset_done' ),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'),
        name = 'password_reset_confirm' ),

    path('reset/complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
        name = 'password_reset_complete' ),

#change pass
    path(
        "password_change/", auth_views.PasswordChangeView.as_view(
         template_name='accounts/password_change_form.html'),
         name="password_change",
    ),
    path(
      "password_change/done", auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'),
        name="password_change_done",
    ),
]