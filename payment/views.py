from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from payment.models import Recharge
from django.contrib.auth.views import LoginView
from django.urls import path

# code for managing data and time 

today_date = timezone.now().date()
expire_date = today_date + timedelta(days=30)

# code to get the days left_out
# days_left = today_date - expire_date
  
# Code after login...
# @login_required
# def index(request,*args, **kwargs):    
#     if request.method == 'POST':
#         promo_code = request.POST['srch']
#         # Your code start here...
#         if promo_code:

#              # comparing the code with exact code in database
#             result = Recharge.objects.filter(code = promo_code).exists()

        #   checking the promo_code for coupon...
            # if result:

                # rslt = Recharge.objects.get(code = promo_code)              
                # print(rslt.expiry_date)
                # rslt.expiry_date = expire_date
                # rslt.save()
                # print("Your Real expire date is...")
                # print(expire_date)
                # print("your account expiry date is....")
                # print(rslt.expiry_date)


            #  Redirecting to Homepage...
                # return render(request,'index.html',{'result':result})                         
# Default page....
    # return render(request,'payment.html')

# Home page view

@login_required
def index(request,*args, **kwargs):

    if (today_date > expire_date):

        # code for the loading payment page..
        if request.method == 'POST':
            promo_code = request.POST['srch']

            if promo_code:

                result = Recharge.objects.filter(code=promo_code).exists()

                if result:

                     return render(request, 'index.html', {'result': result})

        return render(request, 'payment.html')

    else:
        
        return render(request, 'index.html') 



# web-page for the contact..

def contact(request):
    return render(request,'about.html')

def home(request):
    return render(request,'index.html')


    