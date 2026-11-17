# Smart Lost and Found System — Python Full Stack Development

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/Database-MySQL%20%7C%20SQLite-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed%20%26%20Ready%20to%20Run-brightgreen.svg)]()

> **CS3711 – Summer Internship Project Report Implementation**  
> **Student:** Pavithran V (Reg No: 420423104056)  
> **Department:** Computer Science and Engineering, Adhiparasakthi Engineering College (Autonomous), Melmaruvathur  
> **Internship Organization:** Novalis Infotech, Perungalathur, Chennai (15.06.2026 – 15.07.2026)  
> **Mentors:** Dr. C. Dhaya, Ph.D (HOD) & Ms. S. Swetha, M.E (Faculty Mentor)

---

## 🌟 Key Highlights & Features

1. **Django MVT Architecture (Model-View-Template):**
   - High-level modular architecture separating data models (Item, LostItem, Skill), business logic views, and HTML templates.
2. **Dual Reporting Workflow:**
   - Dedicated forms for **Report Lost Item** and **Report Found Item** with location, date, category, description, and image attachments.
3. **Smart Matching Algorithm (92% Similarity):**
   - Automated comparison comparing opposing status (lost &harr; ound), matching category, and location proximity to immediately suggest potential matches.
4. **Real-Time Client-Side Search:**
   - Instant live search filtering with vanilla JavaScript DOM manipulation alongside multi-field backend search using Django ORM Q lookups.
5. **Exact Internship Report Color Theme:**
   - Extracted directly from Chapter 5, 7, and 8:
     - Header Navy: #1e2963
     - Background: #f4f7fc
     - Primary Action: #4f46e5
     - Status Badges: LOST (#fee2e2, text #ef4444), FOUND (#dcfce7, text #16a34a), CLAIMED (#f1f5f9, text #64748b)
     - Smart Match Banner: #eef2ff with #c7d2fe border
6. **Practice Implementations Included:**
   - Practice 1: Report form with green status indicator banner
   - Practice 2: Real-time search filter and client-side form validation
   - Practice 3: Django template loop at /items/
7. **Role-Based Workflows:**
   - User authentication, personal dashboard to track submitted reports, and administrative claim resolution.

---

## 📁 Repository Structure

`
smart-lost-and-found-system/
├── manage.py                          # Django management CLI
├── run_server.py                      # 1-click Python launcher with browser auto-open
├── run.bat                            # Windows double-click runner
├── setup.bat                          # Automated 1-click environment setup
├── seed_data.py                       # Pre-populates database with report data
├── requirements.txt                   # Project dependencies
├── index.html                         # Standalone interactive browser preview
├── demo_preview.html                  # Practice preview
├── db.sqlite3                         # Pre-seeded database with sample reports
├── lost_and_found/                    # Project settings package
│   ├── settings.py                    # MySQL & SQLite dual configuration
│   ├── urls.py                        # Root URL configuration + media serving
│   ├── asgi.py
│   └── wsgi.py
├── items/                             # Core Application
│   ├── admin.py                       # Django Admin configuration
│   ├── forms.py                       # ItemForm with custom validation
│   ├── models.py                      # Item, LostItem, Skill models
│   ├── views.py                       # MVT logic & smart match algorithm
│   ├── urls.py                        # Routes (/report/, /search/, /items/, etc.)
│   └── templates/items/
│       ├── base.html                  # Base template with navbar & footer
│       ├── home.html                  # Figure 8.1 Home page
│       ├── report.html                # Page 20 Report form
│       ├── list.html                  # Search & filter view
│       ├── detail.html                # Details & claim resolution
│       ├── dashboard.html             # User personal dashboard
│       ├── items.html                 # Practice 3 template loop
│       ├── practice_1.html            # Chapter 7.1 HTML/CSS replica
│       ├── login.html                 # Authentication login
│       └── register.html              # Account registration
├── static/
│   ├── css/style.css                  # Custom styling & report color variables
│   └── js/script.js                   # Live search & form validation
└── media/items/                       # Uploaded item photo directory
`

---

## 🚀 Quick Start (Ready to Run)

### Option 1: Fast Launch (Windows)
Double-click un.bat or run:
`powershell
python run_server.py
`
This starts the Django development server and opens **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** automatically.

### Option 2: Standard Setup From Scratch
`powershell
# 1. Clone the repository
git clone https://github.com/pavi-stark/smart-lost-and-found-system.git
cd smart-lost-and-found-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run database migrations
python manage.py migrate

# 4. Seed database with report records & test accounts
python seed_data.py

# 5. Start development server
python manage.py runserver
`

### Option 3: Browser Standalone Preview
Double-click index.html to open the interactive frontend directly in your browser without needing Python installed.

---

## 🔑 Pre-Configured Test Accounts

| Role | Username | Password |
|---|---|---|
| **Administrator (Manage Claims & Admin Panel)** | dmin | dminpassword123 |
| **Student / Reporter (Pavithran V)** | pavithran | pavithranpassword123 |

Access Django Admin Panel at **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**.

---

## 📄 License & Attribution
Developed by **Pavithran V** as part of the CS3711 Summer Internship in Python Full Stack Development at **Novalis Infotech**, Perungalathur, Chennai.
