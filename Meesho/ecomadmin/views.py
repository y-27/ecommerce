from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request, 'ecomadmin/master.html')

def admin_home(request):
    return render(request, 'ecomadmin/admin_home.html')

def approve_seller(request):
    return render(request, 'ecomadmin/approve_seller.html')

def view_customer(request):
    return render(request, 'ecomadmin/view_customer.html')

def view_seller(request):
    return render(request, 'ecomadmin/view_seller.html')

