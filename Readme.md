# Lab Equipment Tracker

A desktop-based laboratory equipment management system built using Python, Tkinter, and MySQL.

The application provides a simple interface for managing laboratory equipment with CRUD operations, search functionality, condition tracking, and a dynamic dashboard.

## Features

- Dynamic dashboard with equipment statistics
- View laboratory equipment
- Add new equipment
- Edit existing equipment
- Delete equipment
- Search equipment
- Track equipment condition
  - Working
  - Maintenance
  - Damaged
- Store purchase dates
- MySQL database integration
- Environment variable based database configuration
- Dark-themed user interface

## Technologies Used

- Python
- Tkinter
- MySQL
- mysql-connector-python
- python-dotenv

## Project Structure

```text
LabEquipmentTracker/
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
├── README.md
│
├── database/
│   └── db.py
│
└── screens/
    ├── dashboard.py
    ├── equipment.py
    ├── add_equipment.py
    └── edit_equipment.py
```

## Database Setup

The project uses MySQL.

Create the database:

```sql
CREATE DATABASE lab_equipment_db;
USE lab_equipment_db;
```

Create the equipment table:

```sql
CREATE TABLE equipment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    lab_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    condition_status VARCHAR(30) NOT NULL,
    purchase_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Lordputin404/LabEquipmentTracker
cd LabEquipmentTracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Database Configuration

Create a `.env` file in the project root:

```env
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=lab_equipment_db
```

Replace `your_mysql_password` with your local MySQL password.

Do not commit the `.env` file to GitHub.

## Run the Application

Make sure MySQL is running, then execute:

```bash
python main.py
```

The application will open on the dashboard.

## Usage

### Dashboard

Displays total equipment and condition-wise statistics along with recently added equipment.

### Equipment

View, search, edit, and delete laboratory equipment.

### Add Equipment

Add new equipment by entering its name, category, lab, quantity, purchase date, and condition.

### Edit Equipment

Select an equipment item and update its details.

### Delete Equipment

Select an equipment item and delete it after confirmation.

## Requirements

- Python 3.x
- MySQL Server

Python packages are listed in `requirements.txt`.

## Security

Database credentials are stored in the `.env` file and excluded from Git using `.gitignore`.

## License

This project was developed as a college mini project.