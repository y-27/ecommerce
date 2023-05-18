import random
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.conf import settings

from common.models import Seller
from customer.models import Customer

# Create your views here.


def master(request):
    return render(request, 'common/master.html')

def home(request):
    return render(request, 'common/home.html')

def sellerlogin(request):
    msg = ''

    if request.method == 'POST' :
        user_name = request.POST['username']
        password = request.POST['password']

        try :
            seller = Seller.objects.get(user_name = user_name, password = password)
            request.session['seller'] = seller.id
            return redirect('seller:home')
        
        except :
            msg = 'incorrect username or password '


    return render(request, 'common/sellerlogin.html',{'message':msg})

def sellersignup(request):
    msg = ''
    if request.method == 'POST' :
        seller_name = request.POST['name']
        seller_address = request.POST['address']
        seller_email = request.POST['email']
        seller_gender = request.POST['gender']
        seller_phone = request.POST['phone_no']
        seller_photo = request.FILES['photo']
        seller_company = request.POST['company']
        seller_ac_holder_name = request.POST['ac_holder_name']
        seller_ifsc = request.POST['ifsc']
        seller_branch = request.POST['branch']
        seller_ac_no = request.POST['ac_no']
        s_username = random.randint(1111,9999)
        s_password = 'sel-'+str(s_username)

        seller_exist = Seller.objects.filter(e_mail = seller_email).exists()


        if not seller_exist :

            new_seller = Seller(
            name = seller_name,
            address = seller_address,
            e_mail = seller_email,
            gender = seller_gender,
            phone_no = seller_phone,
            photo = seller_photo,
            company_name = seller_company,
            ac_holder_name = seller_ac_holder_name,
            ifsc = seller_ifsc,
            branch = seller_branch,
            ac_no = seller_ac_no,
            user_name = s_username,
            password = s_password
        )


            new_seller.save()
            msg = 'Account Created Succesfully'

        else :
             msg = 'email already exist '

        # msg = 'Hi your username is:'+str(s_username)+'and your password is:'+s_password
        # send_mail(
        #     'username and password',
        #     msg,
        #     settings.EMAIL_HOST_USER ,
        #     [seller_email]
        # )
        


    return render(request, 'common/sellersignup.html',{'message' : msg})

def adminlogin(request):
    return render(request, 'common/adminlogin.html')

def customerlogin(request):
    msg = ''
    if request.method == 'POST':
        c_username = request.POST['username']
        c_password = request.POST['password']

        try :
            customer = Customer.objects.get(e_mail = c_username,password = c_password)
            request.session['customer'] = customer.id
            return redirect ('customer:customer_home')
        except :
            msg = 'username or password incorrect '


    return render(request, 'common/customerlogin.html',{'message':msg})

def customersignup(request):

    if request.method == 'POST':
        c_name = request.POST['name']
        c_email =request.POST['email']
        c_address =request.POST['address']
        c_gender =request.POST['gender']
        c_phone =request.POST['phn']
        c_password =request.POST['password']

        new_customer = Customer(
            name = c_name,
            e_mail = c_email,
            address = c_address,
            gender = c_gender,
            phone = c_phone,
            password =c_password
        )

        new_customer.save()
        

    return render(request, 'common/customersignup.html')
















