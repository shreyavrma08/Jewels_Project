from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name= request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phoneno")
        msg = request.POST.get("message")
        c= Contact(name=name,email=email, phone=phone,msg=msg)
        c.save()
        return redirect('/contact')
    data=Contact.objects.all()
    return render(request,"contact.html",{'data':data})

def products(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,"products.html")
def loginView(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/home')
    
        else:
            
          return render(request,"login.html",{'error':"Username or password is incorrect"})


    # No backend authenticated the credentials


    return render(request,"login.html")
def signupView(request):
    if request.method == "POST":
        firstName= request.POST.get('firstName')
        lastName= request.POST.get('lastName')
        username= request.POST.get('userName')
        email= request.POST.get('email')
        password= request.POST.get('password')
        cpassword= request.POST.get('cpassword')

        if password==cpassword:
         user = User.objects.create_user(username,email,password)
         user.first_name= firstName
         user.last_name=lastName
         user.save()
         return redirect("/login")
    return render(request,"signup.html")


def logoutView(request):
    logout(request)
    return redirect('/home')