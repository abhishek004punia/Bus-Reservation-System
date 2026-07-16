from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Booking
from .forms import BookingForm
from schedules.models import Schedule


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        "bookings/booking_list.html",
        {"bookings": bookings},
    )


@login_required
def create_booking(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.schedule = schedule
            booking.save()

            return redirect("booking_list")

    else:
        form = BookingForm()

    return render(
        request,
        "bookings/create_booking.html",
        {
            "form": form,
            "schedule": schedule,
        },
    )