from django.shortcuts import redirect, render

from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def base(response):

    return render(response, "base.html", {})

def index(response):

    return render(response, "index.html", {})

def signin(request):

    if request.method == "POST":

        username = request.POST['username']

        pass1 = request.POST['pass1']

        user = authenticate(username = username, password = pass1)

        if user is not None:

            login(request, user)

            fname = user.first_name

            return render(request, "index.html", {'fname': fname})

        else: 
            
            messages(request, "Bad Credentials!!")

            return redirect("index")

    return render(request, "signin.html", {})

def signup(request):

    if request.method == "POST":

        username = request.POST['username']

        fname = request.POST['fname']

        lname = request.POST['lname']

        email = request.POST['email']

        pass1 = request.POST['pass1']

        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):

            messages.errror(request, "Username already exist")

            return redirect('index')
        
        if User.objects.filter(email=email):

            messages.errror(request, "Email already exist")

            return redirect('index')
        
        if len(username) > 10:

            messages.errror(request, "Username must be under 10 characters")

            return redirect('index')
        
        if pass1 != pass2:

            messages.error(request, "Password didn't match!!")

        myuser = User.objects.create_user(username, email, pass1)

        myuser.first_name = fname

        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('index')

    return render(request, "signup.html", {})

def signout(request):

    logout(request)

    messages.success(request, "Logged Out Successfully")

    return redirect('index')
