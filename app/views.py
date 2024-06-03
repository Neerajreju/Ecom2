from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from urllib import request
from .models import Products, Customers
from django.db.models import Count
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "app/home.html")
def Contact(request):
    return render(request, "app/contact.html")

def About(request):
    return render(request, "app/about.html")

def cart(request):
    return render(request, "app/cart.html")

def buy(request):
    return render(request, "app/buy.html")


class CategoryView(View):
    def get(self,request,val):
        product = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title')
        return render(request, "app/category.html",locals())


class CategoryTitle(View):
    def get(self, request,val):
        product = Products.objects.filter(category=val)
        title = Products.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html",locals())
class ProductDetailView(View):
    def get(self , request , pk):
        product = Products.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request , 'app/CustomerRegistrationForm.html' , locals())


    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer registration successfuk')
        else:
            messages.warning(request, 'invalid input data')
        return render(request , 'app/CustomerRegistrationForm.html' , locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, "app/profile.html" , locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customers(user=user, name=name, locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, 'Profile saved succesful')
        else:
            messages.warning(request,"invalid input data")
        return render(request , 'app/profile.html' , locals())

def adressView (request):
    add = Customers.objects.filter(user=request.user)
    return render(request ,'app/adress.html',locals())


