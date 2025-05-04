Hostel Management System

Welcome to the Hostel Management System – a simple yet powerful desktop application developed in Python using Tkinter and SQLite.

This application is specially designed to assist hostel wardens in managing students, rooms, and payments with ease — all through an intuitive graphical interface.



Features
	•	Login System for authentication.
	•	Student Management (Add, View, Search, Delete).
	•	Room Management (View occupancy, automatic assignment).
	•	Payment Management (Add and View Payments).
	•	Automatic Room Assignment:
	•	100 Rooms available.
	•	Each room can accommodate 2 students maximum.
	•	Manual Student ID Input.
	•	Search Functionality:
	•	Search students by ID, Name, Age, or Course.
	•	One-Window System:
	•	Navigation happens within a single main window.
	•	Consistent Mint Green and Light Purple Theme.
	•	Error Handling for better user experience.



Technologies Used
	•	Python 3.x
	•	Tkinter for GUI development
	•	SQLite3 for database management
	•	Ttk (for better styled widgets)

 Login Credentials
  •username is wadern
  •password is password 

  Installation Instructions
	1.	Make sure Python 3.x is installed.
Download it from https://www.python.org
	2.	Install dependencies (Tkinter usually comes preinstalled):
 3.	Download or clone the project files:
	•	main.py
	•	db_handler.py
	4.	Place both files in the same directory.
	5.	Run the application:

 Application Walkthrough

1. Login Screen
	•	The system starts with a Login window.
	•	Displays title: Hostel Management System.
	•	Enter Username and Password.
	•	On correct credentials, it navigates to the Main Menu.



2. Main Dashboard
	•	Displays title: Main Menu.
	•	Three major options available:
	•	Manage Students
	•	Manage Rooms
	•	Manage Payments
	•	Navigation happens inside the same window (no popups).



3. Manage Students
	•	Title: Manage Students.
	•	Form fields:
	•	Student ID
	•	Name
	•	Age
	•	Course
	•	Buttons:
	•	Add Student: Adds a student and auto-assigns a room.
	•	Delete Student: Deletes selected student.
	•	Room Assignment:
	•	System automatically checks for available rooms.
	•	Max 2 students per room.
	•	Search Function:
	•	Search bar and label placed neatly side-by-side.
	•	Search by ID, Name, or Course.
	•	Student records are displayed in a clean table view.



4. Manage Rooms
	•	Displays all rooms (1–100).
	•	Shows room status:
	•	Available
	•	Occupied (with student names if available).



5. Manage Payments
	•	Form to input payment details:
	•	Student ID
	•	Payment Amount
	•	Buttons:
	•	Add Payment
	•	View Payments
	•	Payment history displayed in table format.



Themes and Styles
	•	Background Colors: Mint Green and Light Purple.
	•	Button Highlights: White and Light Green shades.
	•	Font: Calibri or system default sans-serif.
	•	Consistent spacing and element sizing across screens.
	•	Responsive layout with scrolling where necessary.



Error Handling
	•	Catches wrong input types (e.g., letters instead of numbers for Age/Amount).
	•	Warning messages if required fields are missing.
	•	Login attempts with wrong credentials are gracefully handled.



Future Improvements
	•	Add multiple user roles (e.g., Admin, Staff).
	•	Password change/reset functionality.
	•	Better room visualization (graphical floor plan).
	•	Hostel Fee management.
	•	Student attendance tracking.



Credits
	•	Developed by: Blesings phiri
	•	Language: Python
	•	Tools: Tkinter, SQLite3

  
