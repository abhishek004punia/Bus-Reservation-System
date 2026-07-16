from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from bookings.models import Booking
import uuid
from .models import Payment


@login_required
def payment_summary(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    return render(
        request,
        "payments/payment_summary.html",
        {
            "booking": booking,
        },
    )

@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    payment, created = Payment.objects.get_or_create(
        booking=booking,
        defaults={
            "amount": booking.schedule.fare,
            "status": "SUCCESS",
            "transaction_id": uuid.uuid4().hex[:12].upper(),
        },
    )

    return render(
        request,
        "payments/payment_success.html",
        {
            "booking": booking,
            "payment": payment,
        },
    )