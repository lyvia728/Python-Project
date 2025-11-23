
from django.shortcuts import render
from .forms import IdentityVerificationForm

def verify_identity(request):
    if request.method == "POST":
        form = IdentityVerificationForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ saves to database
            return render(request, "register/success.html", {"form": form})
    else:
        form = IdentityVerificationForm()

    return render(request, "register/verify.html", {"form": form})
