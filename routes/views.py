from django.shortcuts import render, redirect
from .models import Route
from .forms import RouteForm


def route_list(request):
    routes = Route.objects.all()

    return render(
        request,
        "routes/route_list.html",
        {"routes": routes},
    )


def add_route(request):
    if request.method == "POST":
        form = RouteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("route_list")

    else:
        form = RouteForm()

    return render(
        request,
        "routes/add_route.html",
        {"form": form},
    )
