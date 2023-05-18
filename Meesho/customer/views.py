from django.shortcuts import render, redirect
from common.models import Seller
from customer.models import Customer
from seller.models import Product

# Create your views here.


def customer_master(request):
    return render(request, "customer/customer_master.html")


def customer_home(request):
    products = Product.objects.all()
    return render(request, "customer/customer_home.html", {"products": products})


def change_password(request):
    msg = ""
    if request.method == "POST":
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        if new_password == confirm_password:
            if len(new_password) >= 8:
                customer = Customer.objects.get(id=request.session["customer"])
                if customer.password == old_password:
                    customer.password == confirm_password
                    customer.save()
                    msg = "password changed successfully"

                else:
                    msg = "invalid password"
            else:
                msg = "password should be min 8 characters"

        else:
            msg = "password does not match"

    return render(request, "customer/change_password.html", {"message": msg})



# test 
# def change_password(request):
#     msg = ''
#     if request.method == 'POST' :
#         old_password = request.POST['old_password'] 
#         new_password = request.POST['new_password']
#         confirm_password = request.POST['confirm_password']


#         if new_password == confirm_password:
#                 if len(new_password) >=8:
#                     seller = Seller.objects.get(id = request.session['seller'])
#                     if seller.password == old_password:
#                         seller.password = confirm_password
#                         seller.save()
#                         msg = 'password changed successfully'
                    
#                     else:
#                         msg = 'invalid password'
#                 else:
#                     msg = 'password should be min 8 characters'
                    
#         else :
#             msg = 'password does not match' 

# test 





def my_cart(request):
    return render(request, "customer/my_cart.html")


def my_orders(request):
    return render(request, "customer/my_orders.html")


def profile(request):
    return render(request, "customer/profile.html")


def product_details(request):
    return render(request, "customer/product_details.html")


def logout(request):
    del request.session["customer"]
    request.session.flush()
    return redirect("common:home")
