from django.urls import path
from . import views

app_name='ecomadmin'

urlpatterns = [
     
     
    path('master', views.master,name='master'), 
    path('admin_home', views.admin_home,name='admin_home'),
    path('approve_seller', views.approve_seller,name='approve_seller'),
    path('view_customer', views.view_customer,name='view_customer'),
    path('view_seller', views.view_seller,name='view_seller'),



]