# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.task_list, name='task_list'),
#     path('add/', views.add_task, name='add_task'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
#     path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
#     path('register/', views.register, name='register'),
#     path('', views.home, name='home'),
# ]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),       # Home page
    path('tasks/', views.task_list, name='tasks'),  # Tasks page
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]