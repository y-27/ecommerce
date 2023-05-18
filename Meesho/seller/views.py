from django.shortcuts import render,redirect
from common.models import Seller
from seller.models import Product




# Create your views here.

def master(request):
    return render(request, 'seller/master.html')

def home(request):
    seller1 = Seller.objects.get(id = request.session['seller'])
    return render(request, 'seller/home.html',{'seller' : seller1})

def addproduct(request):
    msg=''
    if request.method == 'POST' :
        product_name = request.POST['name']
        description = request.POST['Description']
        stock = request.POST['p_stock']
        code = request.POST['p_code']
        price = request.POST['price']
        image = request.FILES['image']
        product_exist =Product.objects.filter(seller = request.session['seller'],code = code).exists()


        if not product_exist :
            product = Product(
                product_name = product_name,
                description = description,
                stock = stock,
                code = code,
                price = price,
                image = image,
                seller_id = request.session['seller']

            )

            product.save()
            msg ='product added successfully'

        else :     
            msg = 'message already exist'



    return render(request, 'seller/addproduct.html',{'message':msg})

def change_password(request):
    msg = ''
    if request.method == 'POST' :
        old_password = request.POST['old_password'] 
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']


        if new_password == confirm_password:
                if len(new_password) >=8:
                    seller = Seller.objects.get(id = request.session['seller'])
                    if seller.password == old_password:
                        seller.password = confirm_password
                        seller.save()
                        msg = 'password changed successfully'
                    
                    else:
                        msg = 'invalid password'
                else:
                    msg = 'password should be min 8 characters'
                    
        else :
            msg = 'password does not match'  
               

    return render(request, 'seller/change_password.html',{'message':msg})

def update(request):
    return render(request, 'seller/udate.html')

def recent_orders(request):
    return render(request, 'seller/recent_orders.html')

def profile(request):
    return render(request, 'seller/profile.html')

def product_cataloge(request):
    products = Product.objects.filter(seller=request.session['seller'])
    return render(request, 'seller/product_cataloge.html',{'products':products})

def order_history(request):
    return render(request, 'seller/order_history.html')

def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('common:home')









