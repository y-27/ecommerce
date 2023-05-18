from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('customer_master', views.customer_master,name='customer_master'),
    path('customer_home', views.customer_home,name='customer_home'),
    path('change_password', views.change_password,name='change_password'),
    path('my_cart', views.my_cart,name='my_cart'),
    path('my_orders', views.my_orders,name='my_orders'),
    path('profile', views.profile,name='profile'),
    path('product_details', views.product_details,name='product_details'),
    path('logout', views.logout,name='logout'),

    

]