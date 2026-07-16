from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Booking
from .forms import BookingForm, SearchForm
from schedules.models import Schedule
from django.http import HttpResponse
from reportlab.pdfgen import canvas


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

            # No seats available
            if schedule.available_seats <= 0:
                messages.error(request, "No seats available!")
                return redirect("search_bus")

            # Prevent duplicate seat booking
            seat = form.cleaned_data["seat_number"]

            if Booking.objects.filter(
                schedule=schedule,
                seat_number=seat,
                status="CONFIRMED",
            ).exists():

                messages.error(request, f"Seat {seat} is already booked.")
                return render(
                    request,
                    "bookings/create_booking.html",
                    {
                        "form": form,
                        "schedule": schedule,
                    },
                )

            booking = form.save(commit=False)
            booking.user = request.user
            booking.schedule = schedule
            booking.status = "CONFIRMED"
            booking.save()

            # Reduce available seats
            schedule.available_seats -= 1
            schedule.save()

            messages.success(request, "Booking successful!")

            return redirect("booking_detail", pk=booking.pk)

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

def search_bus(request):
    schedules = None

    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            source = form.cleaned_data["source"]
            destination = form.cleaned_data["destination"]
            travel_date = form.cleaned_data["travel_date"]

            schedules = Schedule.objects.filter(
                route__source__icontains=source,
                route__destination__icontains=destination,
                travel_date=travel_date,
                is_active=True,
            )

    else:
        form = SearchForm()

    return render(
        request,
        "bookings/search_bus.html",
        {
            "form": form,
            "schedules": schedules,
        },
    )

@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(
        Booking,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "bookings/booking_detail.html",
        {
            "booking": booking,
        },
    )



@login_required
def download_ticket(request, pk):
    booking = get_object_or_404(
        Booking,
        pk=pk,
        user=request.user
    )

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="ticket_{booking.id}.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.setTitle("Bus Reservation Ticket")

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(170, 800, "BUS RESERVATION TICKET")

    pdf.setFont("Helvetica", 12)

    y = 760

    pdf.drawString(50, y, f"Booking ID : BRS{booking.id:06d}")
    y -= 25

    pdf.drawString(50, y, f"Passenger : {booking.passenger_name}")
    y -= 25

    pdf.drawString(50, y, f"Age : {booking.passenger_age}")
    y -= 25

    pdf.drawString(50, y, f"Gender : {booking.passenger_gender}")
    y -= 25

    pdf.drawString(50, y, f"Mobile : {booking.mobile_number}")
    y -= 25

    pdf.drawString(50, y, f"Bus : {booking.schedule.bus}")
    y -= 25

    pdf.drawString(50, y, f"Route : {booking.schedule.route}")
    y -= 25

    pdf.drawString(50, y, f"Travel Date : {booking.schedule.travel_date}")
    y -= 25

    pdf.drawString(50, y, f"Departure : {booking.schedule.departure_time}")
    y -= 25

    pdf.drawString(50, y, f"Arrival : {booking.schedule.arrival_time}")
    y -= 25

    pdf.drawString(50, y, f"Seat Number : {booking.seat_number}")
    y -= 25

    pdf.drawString(50, y, f"Fare : ₹ {booking.schedule.fare}")
    y -= 25

    pdf.drawString(50, y, f"Status : {booking.status}")

    pdf.save()

    return response