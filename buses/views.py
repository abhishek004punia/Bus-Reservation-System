from django.shortcuts import render, redirect
from .models import Bus
from .forms import BusForm


def bus_list(request):
    buses = Bus.objects.all()

    return render(request, "buses/bus_list.html", {
        "buses": buses
    })


def add_bus(request):
    if request.method == "POST":
        form = BusForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("bus_list")

    else:
        form = BusForm()

    return render(request, "buses/add_bus.html", {
        "form": form
    })
