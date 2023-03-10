from django.urls import path
from django.contrib.auth import views as auth_views

from account import views

urlpatterns = [
    # Main page url
    path('', views.dashboard, name='dashboard'),


    # Register url
    path('register/', views.register, name='register'),


    # Login/Logout urls

    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password change urls
    path('password-change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # Reset passwords urls
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # Edit urls
    path('edit/', views.edit, name='edit'),

    # Users urls
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<username>/', views.user_detail,name='user_detail'),


]
