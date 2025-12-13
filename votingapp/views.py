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
    if request.method == 'POST':
        selected_party_id = request.POST.get('selected_party')
        if not selected_party_id:
            messages.error(request, "No party selected.")
            return redirect('parties')

        try:
            party = Party.objects.get(id=selected_party_id)
            Vote.objects.create(party=party)
            messages.success(request, f"Your vote for {party.name} has been recorded.")
        except Party.DoesNotExist:
            messages.error(request, "Invalid party selection.")

        return redirect('results')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Party, Vote


# Home page
def index(request):
    return render(request, 'index.html')

# Register page
def register(request):
    if request.method == 'POST':
        id_number = request.POST.get('ID_number')
        full_name = request.POST.get('full_name')
        surname = request.POST.get('surname')
        cellphone = request.POST.get('cellphone')

        # ✅ Create a user (using ID_number as username for simplicity)
        user = User.objects.create_user(
            username=id_number,
            first_name=full_name,
            last_name=surname,
            password=cellphone  # ⚠️ For demo only, better to use a secure password
        )

        messages.success(request, "✅ Thank you for registering, you can now log in!")
        return redirect('login')

    return render(request, 'register.html')

# Login page
def login_view(request):
    if request.method == 'POST':
        id_number = request.POST.get('ID_number')
        cellphone = request.POST.get('cellphone')

        # ✅ Authenticate using ID_number as username and cellphone as password
        user = authenticate(request, username=id_number, password=cellphone)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('index')
        else:
            messages.error(request, "❌ Invalid ID number or cellphone.")
            return redirect('login')

    return render(request, 'login.html')

def parties(request):
    parties = Party.objects.all()
    return render(request, 'parties.html', {"parties": parties})


def results(request):
    parties = Party.objects.all()
    total_votes = Vote.objects.count()

    results_data = []
    for party in parties:
        votes = Vote.objects.filter(party=party).count()
        percentage = (votes / total_votes * 100) if total_votes > 0 else 0
        results_data.append({
            "name": party.name,
            "votes": votes,
            "percentage": round(percentage, 2),
            "logo": party.logo,
            "leader": party.leader,
        })

    return render(request, 'results.html', {"results": results_data})

def vote(request):
    if request.method == "POST":
        selected_party_id = request.POST.get("selected_party")

        if not selected_party_id:
            messages.error(request, "No party selected.")
            return redirect("home")

        try:
            party = Party.objects.get(id=selected_party_id)
        except Party.DoesNotExist:
            messages.error(request, "Invalid party selection.")
            return redirect("home")

        # CREATE A NEW VOTE
        Vote.objects.create(party=party)

        messages.success(request, f"You voted for {party.name}")
        return redirect("results")

    return redirect("home")