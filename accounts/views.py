from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.role = "CUSTOMER"    #Default role
            user.save()


            login(request,user)
            return redirect("dashboard")  # Login page baad me banayenge

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {
        "form": form
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("home")