
🏥 Hospital Management System

📌 Overview

This project is a simple Hospital Management System designed for learning purposes.
It includes models and modules for managing patients, staff, surgeries, and hospital workflows.
The structure is clean and extendable so you can grow the project step-by-step.


---

🚀 Features

Patient management (add, update, list records)

Staff management (roles, permissions, info)

Surgery workflow (before / during / after operation)

Object-oriented structure (OOP)

SQLite or SQL-based storage (optional)

Easy to expand with new modules



---

📂 Project Structure

Hospital/
│── models/
│   ├── patient.py
│   ├── staff.py
│   ├── surgery.py
│   └── ...
│
│── database/
│   └── hospital.db   (optional)
│
│── ui/
│   └── main.py       (optional)
│
│── utils/
│   └── validator.py
│
└── README.md


---

⚙️ Technologies

Python

SQL / SQLite

Tkinter (if UI added)

OOP principles



---

🧪 Example Code

class Patient:
    def __init__(self, name, age, national_id):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.records = []

    def add_record(self, record):
        self.records.append(record)


---

📈 To-Do (Future Plans)

[ ] Add surgery management module

[ ] Add appointment scheduling

[ ] Add admin dashboard

[ ] Add API support

[ ] Add reporting system



---

🤝 Contribution

Feel free to contribute!
Issues and pull requests are welcome.


---

📧 Contact

GitHub: MelikaArshad

