from django.http import HttpResponse

def register_view(request):
    return HttpResponse("Register Page")
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect("login")

    return render(
        request,
        "account/register.html"
    )