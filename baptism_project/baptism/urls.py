from django.urls import path
from .views import baptism_form_view,upload_parish_details,success_page,login_view, register_view,upload_baptism_advanced,upload_field_table
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.homePage, name='home'), 
    path('add/', baptism_form_view, name='add_baptism'),
     # Add this line
    path('upload-parish/', upload_parish_details, name='upload_parish'),
    path('parish-success/', success_page, name='parish_success'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('register/', register_view, name='register'),
    path('upload-baptism-advanced/', upload_baptism_advanced, name='upload_baptism_advanced'),
    path('upload-field/', upload_field_table, name='upload_field'),
    path('field-table-success/', success_page, name='field_table_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('secretary_dashboard/',views.secretary_dashboard,name='secretary_dashboard'),
    path('priest_dashboard/',views.priest_dashboard,name='priest_dashboard'),
]


