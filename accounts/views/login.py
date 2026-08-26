from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("profile")

    return render(
        request,
        "account/login.html"
    )