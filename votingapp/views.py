from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request,"index.html")

def register(request):
    return render(request, "register.html")

def parties(request):
    parties = [
        {"name": "ANC", "logo": "ANC Logo.png", "leader": "ANC Leader.png"},
        {"name": "DA", "logo": "DA Logo.png", "leader": "DA Leader.png"},
        {"name": "EFF", "logo": "EFF Logo.png", "leader": "EFF Leader.png"},
        {"name": "IFP", "logo": "IFP Logo.png", "leader": "IFP Leader.png"},
        {"name": "FF+", "logo": "FF+ Logo.png", "leader": "FF+ Leader.png"},
        {"name": "ActionSA", "logo": "ActionSA Logo.png", "leader": "ActionSA Leader.png"},
        {"name": "PAC", "logo": "PAC Logo.png", "leader": "PAC Leader.png"},
        {"name": "UDM", "logo": "UDM Logo.png", "leader": "UDM Leader.png"},
        {"name": "Al Jama-ah", "logo": "Al Jama-ah Logo.png", "leader": "Al Jama-ah Leader.png"},
    ]
    return render(request, "parties.html", {"parties": parties})

def submit_vote(request):
    if request.method == "POST":
        selected = request.POST.get("selected_party")
        return render(request, "index.html", {"message": f"You voted for {selected}!"})
        messages.success(request, f"Thank you for voting for {selected_party}!")
    return redirect("index.html")
