from django.shortcuts import render, redirect
from .forms import IdentityVerificationForm
from django.contrib.auth import authenticate, login

def verify_identity(request):
    if request.method == "POST":
        form = IdentityVerificationForm(request.POST)
        if form.is_valid():
            identity = form.save()  # save and get the instance
            return render(request, "register/success.html", {
                "full_names": identity.full_names,
                "surname": identity.surname,
                "id_number": identity.id_number,
                "cellphone": identity.cellphone,
            })
    else:
        form = IdentityVerificationForm()  # empty form for GET

    return render(request, "register/verify.html", {"form": form})

