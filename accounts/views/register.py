from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username already exists
        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                "Username already exists. Please choose another username."
            )

            return render(
                request,
                "account/register.html"
            )

        # Create new user
        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(
            request,
            "Registration successful! Please log in."
        )

        return redirect("login")

    return render(
        request,
        "account/register.html"
    )