from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import Productform,Cartfrom
from .models import *
from django.contrib import messages    #for messages
from django.db.models import Q    #for search query

# Create your views here.

# Home Page

def home(request):
        if 'u' in request.session.keys():
                lgnid = request.session['u']


                obj = Product.objects.all()
                form = Cartfrom(request.POST)

        # Search Query Start

                try:
                #cart ke liye use kiya try
                        if request.method == "POST":

                                query_for_search =request.POST['ser']
                                results = Product.objects.filter( Q(Product_name=query_for_search) | Q(Product_description=query_for_search))
                                return render(request , "resultpage.html",{"results":results})
        # Search Query End
                except: #cart
                        if form.is_valid():
                                form.save()
                                return redirect('cart')
        else:
                lgnid = ""
                obj = Product.objects.all()


        return render(request, "index.html", {"obj" : obj,"lgnid":lgnid})


# About Page

def about(request):

        return render(request,"about.html")

# Details Page

def detailview(request,pk):
        obj2 = Product.objects.get(pk=pk)
        return render(request,"detailpro.html",{"obj2":obj2})


# SignUp Page

def signup(request):
        form = Productform(request.POST)
        if form.is_valid():
                form.save()
                return redirect('login')
        return render(request,"signup.html",{"form":form})

# Login Page

def login(request):
        if request.method == "POST":
                try:
                        m = Productlogin.objects.get(username=request.POST['username'])
                        if m.password == request.POST['password']:
                                request.session['u']= m.username

                                messages.success(request, f' {m.username} Your-Login Successfull')      # for messages
                                return redirect('home')
                        else:
                                messages.info(request,'incorrect username and password')    # for messages
                                return redirect("login")


                except:
                        messages.info(request, 'incorrect username and password')          # for messages
                        return redirect("login")

        return render(request, "login.html")


# Cart Page

def cartview(request):
        if 'u' in request.session.keys():

                query = Cart.objects.all()
                totalitem =Cart.objects.all().count()
                total = 0
                for i in query:                                 # Product price calculating in cart
                        print(i.Prod_price)
                        total += i.Prod_price
        else:
                return redirect('login')

        return render(request,"cart.html",{"query":query,"total":total,"totalitem":totalitem})


# Item Delete Option In Cart

def itemdelete(request,pk):

    getpro = Cart.objects.get(pk=pk)
    getpro.delete()
    return redirect('cart')

# Forgot Password

def forgotpassword(request):

        if request.method == "POST":
                user = request.POST['username']
                userans = request.POST['question']
                try:
                        qry1 = Productlogin.objects.get(username=user)
                        if str(userans) == str(qry1.question):
                                print(user)

                                return redirect(f'/home/changepassword/{user}/changepassword/')
                except:
                        messages.success(request, 'Please Enter Valid Details')                 # for messages
                        return redirect('forgotpassword')
        return render(request,"forgotpassword.html")

# Change Password

def changepassword(request,usnm):
        qry = Productlogin.objects.get(username = usnm)
        form =Productform(request.POST or None ,instance=qry)
        if form.is_valid():
                form.save()
                return redirect("login")
        return render(request,"changepassword.html",{"form":form})

# LogOut

def logout(request):

         del request.session['u']

         return redirect('home')



# BY AKSHAY PATEL
# BY AKSHAY PATEL
# BY AKSHAY PATEL
# BY AKSHAY PATEL
