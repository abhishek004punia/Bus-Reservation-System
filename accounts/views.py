from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from buses.models import Bus
from routes.models import Route
from drivers.models import Driver
from schedules.models import Schedule
from bookings.models import Booking
from payments.models import Payment
from users.models import User
from django.db.models import Sum

def home(request):

    context = {
        "total_buses": Bus.objects.count(),
        "total_routes": Route.objects.count(),
        "total_drivers": Driver.objects.count(),
        "total_schedules": Schedule.objects.count(),
        "total_bookings": Booking.objects.count(),
        "total_users": User.objects.count(),
        "total_revenue": Payment.objects.filter(
            status="SUCCESS"
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0,
    }

    return render(request, "home.html", context)

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