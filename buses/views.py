from django.shortcuts import render, redirect
from .models import Bus
from .forms import BusForm
from django.shortcuts import get_object_or_404



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

def edit_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)

    if request.method == "POST":
        form = BusForm(request.POST, instance=bus)

        if form.is_valid():
            form.save()
            return redirect("bus_list")

    else:
        form = BusForm(instance=bus)

    return render(request, "buses/add_bus.html", {
        "form": form
    })


def delete_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)

    if request.method == "POST":
        bus.delete()
        return redirect("bus_list")

    return render(request, "buses/delete_bus.html", {
        "bus": bus
    })
