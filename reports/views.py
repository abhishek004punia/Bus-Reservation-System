from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bookings.models import Booking
from payments.models import Payment


@login_required
def reports_dashboard(request):
    total_bookings = Booking.objects.count()

    confirmed_bookings = Booking.objects.filter(
        status="CONFIRMED"
    ).count()

    total_revenue = sum(
        payment.amount for payment in Payment.objects.filter(status="SUCCESS")
    )

    context = {
        "total_bookings": total_bookings,
        "confirmed_bookings": confirmed_bookings,
        "total_revenue": total_revenue,
    }

    return render(
        request,
        "reports/dashboard.html",
        context,
    )