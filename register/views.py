from django.shortcuts import render, redirect
from .forms import IdentityVerificationForm
from django.contrib.auth import authenticate, login

def verify_identity(request):
    if request.method == "POST":
        form = IdentityVerificationForm(request.POST)
        if form.is_valid():
            identity = form.save()  # save and get the instance
            return render(request, "register/login.html", {
                "full_names": identity.full_names,
                "surname": identity.surname,
                "id_number": identity.id_number,
                "cellphone": identity.cellphone,
            })
    else:
        form = IdentityVerificationForm()  # empty form for GET

    return render(request, "register/verify.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # or dashboard
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "register/login.html")
