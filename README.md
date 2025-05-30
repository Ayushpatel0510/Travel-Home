
🏠 TravelHome - Property Booking Web App

TravelHome is a Django-based web application that allows users to register, log in, browse and book properties, and manage bookings. Hosts can list properties and manage them through a dedicated dashboard.

📦 Features
- User registration and login with password confirmation
- Property listings and detail pages
- Booking system with check-in, check-out, and guest fields
- User dashboard to manage bookings
- Host dashboard to manage property listings
- Property browsing through search feature and filters
- Django messages for feedback
- CSRF protection
- Admin dashboard to manage users, bookings, and properties

🛠 Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Javascript (or custom styling)
- **Database:** SQLite (can be configured to PostgreSQL)
- **Server:** Django’s built-in dev server 
- **Templating Engine:** Django Templates

⚙️ Requirements
- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional but recommended)
- PostgreSQL or SQLite (default: SQLite)

🚀 Setup Instructions

1. Clone the repository
   git clone https://github.com/Ayushpatel0510/Travel-Home.git
   cd travelhome

2. Set up a virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

   If requirements.txt is missing, install manually:
   pip install django

4. Run initial migrations
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser (for admin access)
   python manage.py createsuperuser

6. Run the development server
   python manage.py runserver

   Visit http://127.0.0.1:8000/ in your browser.


🔧 Configuration Notes
- CSRF protection is enabled by default. Make sure all POST forms have {% csrf_token %} in templates.
- Static files are served via Django in dev; for production, configure using WhiteNoise or collectstatic.

👨‍💻 Author
Created by Ayush Patel
