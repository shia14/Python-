
import tkinter as tk
from tkinter import messagebox, ttk
import db_handler

# Color theme
BG_COLOR = "#FFFFFF"  # White
ACCENT_COLOR = "#98FF98"  # Mint green
SECONDARY_COLOR = "#D8BFD8"  # Light purple
TEXT_COLOR = "#000000"  # Black

# Initialize database
db_handler.create_tables()

class HostelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hostel Management System")
        self.geometry("900x650")
        self.configure(bg=BG_COLOR)
        self.frames = {}
        self.active_frame = None
        self.show_frame(LoginPage)

    def show_frame(self, page_class):
        if self.active_frame:
            self.active_frame.destroy()
        frame = page_class(parent=self, controller=self)
        self.active_frame = frame
        frame.pack(fill="both", expand=True)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        self.controller = controller
        tk.Label(self, text="Hostel Login", font=("Arial", 22), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=20)
        tk.Label(self, text="Username:", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
        self.username_entry = tk.Entry(self, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        self.username_entry.pack()
        tk.Label(self, text="Password:", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        self.password_entry.pack()
        tk.Button(self, text="Login", command=self.login, bg=ACCENT_COLOR, fg=TEXT_COLOR, width=20).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin123":
            self.controller.show_frame(Dashboard)
        else:
            messagebox.showerror("Login Failed", "Incorrect Username or Password")

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        self.controller = controller
        tk.Label(self, text="Dashboard", font=("Arial", 26), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=20)
        tk.Button(self, text="Manage Students", command=lambda: controller.show_frame(ManageStudents),
                  bg=ACCENT_COLOR, fg=TEXT_COLOR, width=30, height=2).pack(pady=10)
        tk.Button(self, text="Manage Rooms", command=lambda: controller.show_frame(PlaceholderPage),
                  bg=ACCENT_COLOR, fg=TEXT_COLOR, width=30, height=2).pack(pady=10)
        tk.Button(self, text="Manage Payments", command=lambda: controller.show_frame(PlaceholderPage),
                  bg=ACCENT_COLOR, fg=TEXT_COLOR, width=30, height=2).pack(pady=10)

class ManageStudents(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        self.controller = controller
        tk.Label(self, text="Manage Students", font=("Arial", 22), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

        form_frame = tk.Frame(self, bg=BG_COLOR)
        form_frame.pack(pady=10)
        tk.Label(form_frame, text="Student ID:", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(form_frame, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Name:", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Age:", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=2, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(form_frame, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Room No:", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, padx=5, pady=5)
        self.room_entry = tk.Entry(form_frame, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        self.room_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(self, text="Add Student", command=self.add_student, bg=ACCENT_COLOR, fg=TEXT_COLOR, width=20).pack(pady=5)

        search_frame = tk.Frame(self, bg=BG_COLOR)
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="Search:", bg=BG_COLOR, fg=TEXT_COLOR).grid(row=0, column=0)
        self.search_entry = tk.Entry(search_frame, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        self.search_entry.grid(row=0, column=1)
        tk.Button(search_frame, text="Search", command=self.search_student, bg=ACCENT_COLOR, fg=TEXT_COLOR).grid(row=0, column=2, padx=5)

        table_frame = tk.Frame(self, bg=BG_COLOR)
        table_frame.pack(pady=10, fill="both", expand=True)
        self.student_table = ttk.Treeview(table_frame, columns=("ID", "Name", "Age", "Room"))
        for col in ("ID", "Name", "Age", "Room"):
            self.student_table.heading(col, text=col)
        self.student_table["show"] = "headings"
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.student_table.yview)
        self.student_table.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.student_table.pack(fill="both", expand=True)

        tk.Button(self, text="Delete Selected", command=self.delete_student, bg=ACCENT_COLOR, fg=TEXT_COLOR).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(Dashboard), bg=SECONDARY_COLOR, fg=TEXT_COLOR).pack(pady=10)

        self.refresh_table()

    def add_student(self):
        student_id = self.id_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        room = self.room_entry.get()
        if student_id and name and age and room:
            db_handler.add_student(student_id, name, age, room)
            self.refresh_table()
        else:
            messagebox.showerror("Error", "Fill all fields.")

    def delete_student(self):
        selected = self.student_table.selection()
        if selected:
            student_id = self.student_table.item(selected[0])['values'][0]
            db_handler.delete_student(student_id)
            self.refresh_table()

    def search_student(self):
        keyword = self.search_entry.get()
        results = db_handler.search_student(keyword)
        self.student_table.delete(*self.student_table.get_children())
        for row in results:
            self.student_table.insert("", "end", values=row)

    def refresh_table(self):
        for i in self.student_table.get_children():
            self.student_table.delete(i)
        for row in db_handler.view_students():
            self.student_table.insert("", "end", values=row)

class PlaceholderPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=BG_COLOR)
        self.controller = controller
        tk.Label(self, text="Coming Soon", font=("Arial", 22), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=20)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(Dashboard),
                  bg=SECONDARY_COLOR, fg=TEXT_COLOR).pack(pady=10)

if __name__ == "__main__":
    app = HostelApp()
    app.mainloop()
