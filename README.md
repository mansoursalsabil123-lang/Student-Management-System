# 🎓 Student Management System

A simple **Student Management System** developed using Python and Tkinter. This project provides a graphical interface for managing student information and analyzing their grades.

## ✨ Features

- **Login System:** Access the application using administrator credentials.
- **Add Students:** Register students with their name, grade, and department.
- **View Students:** Display the list of registered students and their information.
- **Grade Statistics:** Calculate the number of students, highest grade, lowest grade, and average grade.
- **Logout:** Exit the dashboard and return to the login page.
- **Input Validation:** Check that required fields are filled in and grades are between 0 and 20.

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** — graphical user interface (GUI)
- **Built-in Python functions** — grade calculations and data management

## 📁 Project Structure

```text
Student-Management-System/
│
├── main.py       # Main application with graphical interface
├── pyth.py       # Basic grade statistics exercise
└── README.md     # Project documentation
```

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

Tkinter is usually included with Python. On Ubuntu, if needed, install it using:

```bash
sudo apt install python3-tk
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR-REPOSITORY
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## 🔐 Login Credentials

Use the following demo credentials to access the dashboard:

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `1234` |

**Note:** These are demonstration credentials hardcoded in the source code. They are not suitable for a production application.

## 📊 Grade Statistics

The application calculates:

- **Total Students:** Number of students registered during the current session.
- **Highest Grade:** Maximum grade recorded.
- **Lowest Grade:** Minimum grade recorded.
- **Average Grade:** Sum of all grades divided by the number of students.

Grades must be between 0 and 20.

## 💾 Data Storage

Student information is stored in Python lists while the application is running. The data is not saved to a database or file, so it is lost when the application closes.

## 🎯 Project Objectives

This project demonstrates the practical use of:

- Python functions and conditional statements
- Lists and loops
- Basic data validation
- Arithmetic operations and statistics
- Tkinter widgets and event handling
- Multiple windows in a desktop application

## 🔮 Future Improvements

- Add permanent data storage using SQLite or MySQL.
- Implement student search, editing, and deletion.
- Improve the user interface and layout.
- Add secure authentication and password management.
- Handle invalid grade inputs and empty student lists.
- Export student records and statistics to CSV or Excel.

## 👩‍💻 Author

**Salsabil Mansour**

Computer Science Student | ISSAT Sousse

---

*Developed as a Python programming project to practice GUI development, data management, and basic statistical calculations.*
