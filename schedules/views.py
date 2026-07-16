from django.shortcuts import render, redirect
from .models import Schedule
from .forms import ScheduleForm


def schedule_list(request):
    schedules = Schedule.objects.all()

    return render(
        request,
        "schedules/schedule_list.html",
        {"schedules": schedules},
    )


def add_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("schedule_list")

    else:
        form = ScheduleForm()

    return render(
        request,
        "schedules/add_schedule.html",
        {"form": form},
    )