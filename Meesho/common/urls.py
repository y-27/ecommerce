from django.urls import path
from . import views

app_name='common'

urlpatterns = [
    path('master', views.master,name='master'),
    path('home', views.home,name='home'),
    path('sellerlogin', views.sellerlogin,name='sellerlogin'),
    path('sellersignup', views.sellersignup,name='sellersignup'),
    path('adminlogin', views.adminlogin,name='adminlogin'),
    path('customerlogin', views.customerlogin,name='customerlogin'),
    path('customersignup', views.customersignup,name='customersignup'),
    

]