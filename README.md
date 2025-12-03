# Python-Project
# 🇿🇦 Voting South Africa (Django Project)

A secure, simulated online voting system built using the **Django** framework. This project includes voter registration, eligibility checks (age 18+), a voting booth, and a real-time results dashboard.

## ✨ Features

* **Voter Registration:** Captures comprehensive details (ID, address, ward, contact info) with **data validation**.
* **Eligibility Check:** Verifies voters are **18 years or older**.
* **Confirmation:** Uses **Twilio SendGrid (Email)** and **Twilio (SMS)** for registration and vote confirmation.
* **Single Vote Enforcement:** Prevents registered users from voting more than once.
* **Results Dashboard:** Displays aggregated vote counts and percentages by political party.

## 🚀 Getting Started

### Prerequisites

* Python (3.8+)
* Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/IEC_Voting_System.git](https://github.com/your-username/IEC_Voting_System.git)
    cd IEC_Voting_System
    ```

2.  **Setup Virtual Environment & Install Dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a file named **`.env`** in the root directory and populate it with your keys (Twilio, SendGrid, etc.). **Add this file to `.gitignore`!**

4.  **Database Setup:**
    ```bash
    python manage.py makemigrations voter_management
    python manage.py migrate
    ```

5.  **Create Superuser (Admin Access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## 🗳️ Usage

1.  **Set Up Parties:** Access the admin panel (`/admin/`) and create entries in the **Party** model (e.g., "Party A", "Party B").
2.  **Register:** Navigate to `/register/` and register a user.
3.  **Vote:** Log in and visit the `/vote/` page.
4.  **Results:** View the current tally at `/results/`.
