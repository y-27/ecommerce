from django.urls import path
from . import views

app_name='seller'

urlpatterns = [
    path('master', views.master,name='master'),
    path('home', views.home,name='home'),
    path('addproduct', views.addproduct,name='addproduct'),
    path('change_password', views.change_password,name='change_password'),
    path('order_history', views.order_history,name='order_history'),
    path('product_cataloge', views.product_cataloge,name='product_cataloge'),
    path('profile', views.profile,name='profile'),
    path('recent_orders', views.recent_orders,name='recent_orders'),
    path('update', views.update,name='update'),
    path('logout', views.logout,name='logout'),

]