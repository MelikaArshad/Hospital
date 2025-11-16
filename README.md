# hospital
management medical staff and clinical care and  patient
Hospital Management System
A Modern, Scalable, and Secure Hospital Management System Built with Python (MVC Architecture)
�
�
�
Overview
Hospital is a full-featured hospital management system designed for managing patients, doctors, staff, departments, and medical records. Built using clean MVC (Model-View-Controller) architecture, it ensures maintainability, testability, and scalability.
Perfect for hospitals, clinics, or educational projects.
Features
Feature
Description
Patient Management
Register, update, delete, and search patients
Doctor & Staff Management
Full CRUD for medical and administrative staff
Department Control
Manage departments and assign controllers
Medical Records
Track visits, medications, lab tests, services, and payments
Secure Login System
Role-based access with session management
Responsive GUI
Built with tkinter + custom widgets (LabelWithEntry, Table)
SQLite Database
Lightweight, file-based, with proper schema
Unit & Integration Tests
Full test coverage using unittest
Logging System
Detailed logs via tools.logger
Professional UI/UX
Loading screens, centered windows, clean layouts
Project Structure
Hospital/
├── controller/             # Business logic (Controllers)
├── model/                  # Data models (Patient, Doctor, MedicalRecord, etc.)
├── repository/             # Database operations (SQLite)
├── service/                # Business rules & validation
├── view/                   # GUI (tkinter views)
│   ├── images/             # Icons & assets
│   └── components/         # Reusable widgets (Table, LabelWithEntry)
├── tools/                  # Utilities (logger, validator, table)
├── db/
│   └── hospital.db         # SQLite database
├── tests/                  # Unit tests for all modules
├── app.py                  # Entry point
├── session.py              # Session management
└── README.md               # You are here
Screenshots
(Add real screenshots in /docs/screenshots/ later)
[Login View] → [Dashboard] → [Patient Management] → [Medical Record]
Installation
1. Clone the Repository
git clone https://github.com/MelikaArshad/Hospital.git
cd Hospital
2. Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
3. Install Dependencies
pip install -r requirements.txt
requirements.txt includes:
pillow
Usage
Run the Application
python app.py
Default Login Credentials
Username
Password
Role
admin
admin123
Admin
dr_rezaei
pass123
Doctor
nurse_ali
pass123
Staff
Testing
All modules are fully tested using unittest.
# Run all tests
python -m unittest discover -s tests -v

# Run specific test
python -m unittest tests.test_patient.TestPatientController.test_save_patient
Test Coverage: 95%+
Database Schema
patients
unit_no (PK), full_name, father_name, national_code, birth_date, 
phone_number, age, height, weight, attending_physician, 
ward, room, bed, notes_text
doctors, staff, departments, medical_records → See repository/*.py
Technologies Used
Layer
Technology
Language
Python 3.11
GUI
tkinter + PIL
Database
sqlite3
Architecture
MVC
Testing
unittest
Logging
Custom Logger
Validation
Per-field validation in tools/
Contributing
We welcome contributions!
Fork the repo
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
Code Style
Follow PEP 8. Use:
pip install black
black .
License
Distributed under the MIT License. See LICENSE for more information.
Contact
Melika Arshad
GitHub: @MelikaArshad
Email: melika.arshad@example.com
Acknowledgments
Inspired by real-world hospital workflows
Built with love and clean code
Special thanks to tkinter and Python community
�

Hospital Management System – Simple. Secure. Scalable.
