from django.urls import path,re_path
from app import views

urlpatterns = [
    path('app/login/', views.CustomLoginView.as_view(),name='login'),
    path('', views.home_view,name='home'),
    path('register/', views.register_user,name='register'),
    # path('login/', views.login_user,name='login'),
   
    path('logout/', views.logout_user,name='logout'),
    path('create-report/', views.create_report,name='create-report'),  
    path('editReport/<int:id>', views.Edit_Report, name='editReport'),
   
]
