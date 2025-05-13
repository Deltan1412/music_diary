from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.enter, name="enter"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page ='enter'), name='logout'),
    path('home/', views.homepage, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('user_administration/', views.user_administration, name='user_administration'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    path('create_entry/', views.create_entry, name='create_entry'),
    path('entry_manager/', views.entry_manager, name='entry_manager'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]