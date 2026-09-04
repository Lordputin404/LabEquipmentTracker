import tkinter as tk
from tkinter import ttk, messagebox
from database.db import get_connection
from screens.edit_equipment import EditEquipment


class Equipment:
    def __init__(
        self,
        parent,
        show_dashboard,
        show_equipment,
        show_add_equipment
    ):
        self.parent = parent

        self.show_dashboard = show_dashboard
        self.show_equipment = show_equipment
        self.show_add_equipment = show_add_equipment

        # =========================
        # MAIN FRAME
        # =========================

        self.frame = tk.Frame(
            parent,
            bg="#0f1117"
        )
        self.frame.pack(
            fill="both",
            expand=True
        )

        # =========================
        # HEADER
        # =========================

        tk.Label(
            self.frame,
            text="Equipment",
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
            text="Manage laboratory equipment",
            font=("Arial", 11),
            bg="#0f1117",
            fg="#8b93a1"
        ).pack(
            anchor="w",
            padx=35
        )

        # =========================
        # TOP NAVIGATION
        # =========================

        nav_frame = tk.Frame(
            self.frame,
            bg="#171a21"
        )
        nav_frame.pack(
            fill="x",
            padx=35,
            pady=(15, 0)
        )

        tk.Button(
            nav_frame,
            text="Dashboard",
            font=("Arial", 10),
            bg="#171a21",
            fg="#8b93a1",
            activebackground="#171a21",
            activeforeground="#f3f4f6",
            relief="flat",
            cursor="hand2",
            command=self.show_dashboard
        ).pack(side="left", padx=(0, 20))

        tk.Button(
            nav_frame,
            text="Equipment",
            font=("Arial", 10, "bold"),
            bg="#171a21",
            fg="#f3f4f6",
            activebackground="#171a21",
            activeforeground="#f3f4f6",
            relief="flat",
            cursor="hand2",
            command=self.show_equipment
        ).pack(side="left", padx=20)

        tk.Button(
            nav_frame,
            text="Add Equipment",
            font=("Arial", 10),
            bg="#171a21",
            fg="#8b93a1",
            activebackground="#171a21",
            activeforeground="#f3f4f6",
            relief="flat",
            cursor="hand2",
            command=self.show_add_equipment
        ).pack(side="left", padx=20)

        # =========================
        # TOOLBAR
        # =========================

        toolbar = tk.Frame(
            self.frame,
            bg="#0f1117"
        )
        toolbar.pack(
            fill="x",
            padx=35,
            pady=(25, 0)
        )

        # Search box
        self.search_var = tk.StringVar()

        self.search_entry = tk.Entry(
            toolbar,
            textvariable=self.search_var,
            font=("Arial", 10),
            bg="#171a21",
            fg="#f3f4f6",
            insertbackground="#f3f4f6",
            relief="flat",
            width=30
        )
        self.search_entry.pack(
            side="right",
            ipady=8
        )

        # Search button
        tk.Button(
            toolbar,
            text="Search",
            font=("Arial", 10, "bold"),
            bg="#4f8cff",
            fg="white",
            activebackground="#3d73d1",
            activeforeground="white",
            relief="flat",
            padx=18,
            pady=8,
            cursor="hand2",
            command=self.search_equipment
        ).pack(
            side="right",
            padx=(10, 10)
        )

        # Refresh button
        tk.Button(
            toolbar,
            text="Refresh",
            font=("Arial", 10),
            bg="#20242d",
            fg="#f3f4f6",
            activebackground="#292e38",
            activeforeground="#f3f4f6",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.load_equipment
        ).pack(
            side="right"
        )

        # Edit button
        tk.Button(
            toolbar,
            text="Edit",
            font=("Arial", 10, "bold"),
            bg="#20242d",
            fg="#f3f4f6",
            activebackground="#292e38",
            activeforeground="#f3f4f6",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.edit_equipment
        ).pack(
            side="left"
        )

        # Delete button
        tk.Button(
            toolbar,
            text="Delete",
            font=("Arial", 10, "bold"),
            bg="#7f1d1d",
            fg="#ffffff",
            activebackground="#991b1b",
            activeforeground="#ffffff",
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.delete_equipment
        ).pack(
            side="left",
            padx=(10, 0)
        )

        # =========================
        # TABLE CONTAINER
        # =========================

        table_frame = tk.Frame(
            self.frame,
            bg="#171a21"
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=30
        )

        # =========================
        # TABLE STYLE
        # =========================

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#171a21",
            foreground="#f3f4f6",
            fieldbackground="#171a21",
            rowheight=38,
            borderwidth=0,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#20242d",
            foreground="#f3f4f6",
            font=("Arial", 10, "bold"),
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#2d5fa8")
            ],
            foreground=[
                ("selected", "#ffffff")
            ]
        )

        # =========================
        # TABLE
        # =========================

        columns = (
            "id",
            "name",
            "category",
            "lab",
            "quantity",
            "condition",
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.table.tag_configure(
            "working",
            foreground="#4ade80"
        )

        self.table.tag_configure(
            "maintenance",
            foreground="#facc15"
        )

        self.table.tag_configure(
            "damaged",
            foreground="#f87171"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )

        self.table.configure(
            yscrollcommand=scrollbar.set
        )

        headings = {
            "id": "ID",
            "name": "Equipment",
            "category": "Category",
            "lab": "Lab",
            "quantity": "Quantity",
            "condition": "Condition",
        }

        for column in columns:
            self.table.heading(
                column,
                text=headings[column]
            )

        self.table.column(
            "id",
            width=50,
            anchor="center"
        )

        self.table.column(
            "name",
            width=180
        )

        self.table.column(
            "category",
            width=120
        )

        self.table.column(
            "lab",
            width=150
        )

        self.table.column(
            "quantity",
            width=80,
            anchor="center"
        )

        self.table.column(
            "condition",
            width=110,
            anchor="center"
        )

        self.table.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(15, 0),
            pady=15
        )

        scrollbar.pack(
            side="right",
            fill="y",
            padx=(0, 15),
            pady=15
        )

        # Load database records
        self.load_equipment()

    # =========================
    # LOAD EQUIPMENT
    # =========================

    def load_equipment(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id,
                   equipment_name,
                   category,
                   lab_name,
                   quantity,
                   condition_status
            FROM equipment
            ORDER BY id DESC
        """)

        records = cursor.fetchall()

        # Clear existing rows
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert fresh records
        for record in records:
            condition = record[5].lower()

            if condition == "working":
                tag = "working"
            elif condition == "maintenance":
                tag = "maintenance"
            elif condition == "damaged":
                tag = "damaged"
            else:
                tag = ""

            self.table.insert(
                "",
                "end",
                values=record,
                tags=(tag,)
            )

        cursor.close()
        connection.close()

    # =========================
    # SEARCH EQUIPMENT
    # =========================

    def search_equipment(self):
        search_text = self.search_var.get().strip()

        connection = get_connection()
        cursor = connection.cursor()

        if search_text:
            query = """
                SELECT id,
                       equipment_name,
                       category,
                       lab_name,
                       quantity,
                       condition_status
                FROM equipment
                WHERE equipment_name LIKE %s
                   OR category LIKE %s
                   OR lab_name LIKE %s
                   OR condition_status LIKE %s
                ORDER BY id DESC
            """

            value = f"%{search_text}%"

            cursor.execute(
                query,
                (value, value, value, value)
            )

        else:
            cursor.execute("""
                SELECT id,
                       equipment_name,
                       category,
                       lab_name,
                       quantity,
                       condition_status
                FROM equipment
                ORDER BY id DESC
            """)

        records = cursor.fetchall()

        # Clear table
        for item in self.table.get_children():
            self.table.delete(item)

        # Add search results
        for record in records:
            condition = record[5].lower()

            if condition == "working":
                tag = "working"
            elif condition == "maintenance":
                tag = "maintenance"
            elif condition == "damaged":
                tag = "damaged"
            else:
                tag = ""

            self.table.insert(
                "",
                "end",
                values=record,
                tags=(tag,)
            )

        cursor.close()
        connection.close()

    def edit_equipment(self):
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select an equipment to edit."
            )
            return

        item = self.table.item(selected[0])
        equipment_id = item["values"][0]

        self.frame.destroy()
        EditEquipment(
        self.parent,
        equipment_id,
        self.show_equipment
    )

    def delete_equipment(self):
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select an equipment to delete."
            )
            return

        item = self.table.item(selected[0])
        equipment_id = item["values"][0]
        equipment_name = item["values"][1]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete\n"
            f"'{equipment_name}'?"
        )

        if not confirm:
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM equipment WHERE id = %s",
                (equipment_id,)
            )

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Equipment deleted successfully!"
            )

            self.load_equipment()

        except Exception as error:
            messagebox.showerror(
                "Database Error",
                f"Could not delete equipment.\n\n{error}"
            )