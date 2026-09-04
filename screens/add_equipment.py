import tkinter as tk
from tkinter import messagebox
from database.db import get_connection


class AddEquipment:
    def __init__(self, parent):
        self.parent = parent

        self.frame = tk.Frame(
            parent,
            bg="#0f1117"
        )
        self.frame.pack(
            fill="both",
            expand=True
        )

        # Header
        tk.Label(
            self.frame,
            text="Add Equipment",
            font=("Arial", 26, "bold"),
            bg="#0f1117",
            fg="#f3f4f6"
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 5)
        )

        tk.Label(
            self.frame,
            text="Add a new item to laboratory inventory",
            font=("Arial", 11),
            bg="#0f1117",
            fg="#8b93a1"
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 25)
        )

        # Form
        form = tk.Frame(
            self.frame,
            bg="#171a21"
        )
        form.pack(
            fill="x",
            padx=35,
            pady=10
        )

        self.name_var = tk.StringVar()
        self.category_var = tk.StringVar()
        self.lab_var = tk.StringVar()
        self.quantity_var = tk.StringVar()
        self.purchase_date_var = tk.StringVar()
        self.condition_var = tk.StringVar(value="Working")

        self.create_field(form, "Equipment Name", self.name_var, 0)
        self.create_field(form, "Category", self.category_var, 1)
        self.create_field(form, "Lab Name", self.lab_var, 2)
        self.create_field(form, "Quantity", self.quantity_var, 3)
        self.create_field(
            form,
            "Purchase Date (YYYY-MM-DD)",
            self.purchase_date_var,
            4
        )

        # Condition
        tk.Label(
            form,
            text="Condition",
            font=("Arial", 10, "bold"),
            bg="#171a21",
            fg="#f3f4f6"
        ).grid(
            row=5,
            column=0,
            sticky="w",
            padx=25,
            pady=(15, 5)
        )

        condition_menu = tk.OptionMenu(
            form,
            self.condition_var,
            "Working",
            "Maintenance",
            "Damaged"
        )

        condition_menu.config(
            bg="#20242d",
            fg="#f3f4f6",
            activebackground="#292e38",
            activeforeground="#f3f4f6",
            relief="flat",
            width=25
        )

        condition_menu.grid(
            row=5,
            column=1,
            sticky="w",
            padx=25,
            pady=(15, 5)
        )

        # Add button
        tk.Button(
            form,
            text="Add Equipment",
            font=("Arial", 10, "bold"),
            bg="#4f8cff",
            fg="white",
            activebackground="#3d73d1",
            activeforeground="white",
            relief="flat",
            padx=25,
            pady=10,
            cursor="hand2",
            command=self.add_equipment
        ).grid(
            row=6,
            column=0,
            columnspan=2,
            sticky="w",
            padx=25,
            pady=30
        )

    def create_field(self, parent, label, variable, row):
        tk.Label(
            parent,
            text=label,
            font=("Arial", 10, "bold"),
            bg="#171a21",
            fg="#f3f4f6"
        ).grid(
            row=row,
            column=0,
            sticky="w",
            padx=25,
            pady=8
        )

        entry = tk.Entry(
            parent,
            textvariable=variable,
            font=("Arial", 10),
            bg="#20242d",
            fg="#f3f4f6",
            insertbackground="#f3f4f6",
            relief="flat",
            width=35
        )

        entry.grid(
            row=row,
            column=1,
            sticky="w",
            padx=25,
            pady=8,
            ipady=7
        )

    def add_equipment(self):
        name = self.name_var.get().strip()
        category = self.category_var.get().strip()
        lab = self.lab_var.get().strip()
        quantity = self.quantity_var.get().strip()
        condition = self.condition_var.get()
        purchase_date = self.purchase_date_var.get().strip()

        if not name or not category or not lab or not quantity:
            messagebox.showwarning(
                "Missing Information",
                "Please fill all required fields."
            )
            return

        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showwarning(
                "Invalid Quantity",
                "Quantity must be a positive number."
            )
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
                INSERT INTO equipment
                (
                    equipment_name,
                    category,
                    lab_name,
                    quantity,
                    condition_status,
                    purchase_date
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = (
                name,
                category,
                lab,
                int(quantity),
                condition,
                purchase_date if purchase_date else None
            )

            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Equipment added successfully!"
            )

            self.clear_form()

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                f"Could not add equipment.\n\n{error}"
            )

    def clear_form(self):
        self.name_var.set("")
        self.category_var.set("")
        self.lab_var.set("")
        self.quantity_var.set("")
        self.purchase_date_var.set("")
        self.condition_var.set("Working")