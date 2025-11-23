
from django.shortcuts import render
from .forms import IdentityVerificationForm
from .forms import IdentityVerificationForm

def verify_identity(request):
    if request.method == "POST":
        form = IdentityVerificationForm(request.POST)
        if form.is_valid():
            form.save()  # ✅ saves to database
            return render(request, "register/success.html", {"form": form})
    else:
        identity = form.save()
        return render(request, "register/success.html", {
              "full_names": identity.full_names,
              "surname": identity.surname,
              "id_number": identity.id_number,
              "cellphone": identity.cellphone,
})
