import tkinter as tk
from database.db import get_equipment_stats


class Dashboard:
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

        # Colors
        self.bg = "#0f1117"
        self.panel = "#171a21"
        self.card = "#1d212b"
        self.border = "#292e3a"
        self.text = "#f3f4f6"
        self.muted = "#8b93a1"
        self.accent = "#4f8cff"

        # Main frame
        self.main_frame = tk.Frame(
            parent,
            bg=self.bg
        )
        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # =========================
        # TOP NAVIGATION
        # =========================

        self.topbar = tk.Frame(
            self.main_frame,
            bg=self.panel,
            height=70
        )
        self.topbar.pack(
            fill="x"
        )
        self.topbar.pack_propagate(False)

        # Logo / Brand
        tk.Label(
            self.topbar,
            text="LAB//CONTROL",
            font=("Arial", 17, "bold"),
            bg=self.panel,
            fg=self.text
        ).pack(
            side="left",
            padx=30
        )

        # Navigation
        nav_frame = tk.Frame(
            self.topbar,
            bg=self.panel
        )
        nav_frame.pack(
            side="right",
            padx=25
        )

        nav_items = [
            ("Dashboard", self.show_dashboard),
            ("Equipment", self.show_equipment),
            ("Add Equipment", self.show_add_equipment)
        ]

        for item, command in nav_items:
            tk.Button(
                nav_frame,
                text=item,
                font=("Arial", 10),
                bg=self.panel,
                fg=self.muted,
                activebackground=self.panel,
                activeforeground=self.text,
                relief="flat",
                borderwidth=0,
                cursor="hand2",
                command=command
            ).pack(
                side="left",
                padx=10
            )

        # =========================
        # CONTENT
        # =========================

        content = tk.Frame(
            self.main_frame,
            bg=self.bg
        )
        content.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=30
        )

        # Heading
        tk.Label(
            content,
            text="Laboratory Equipment",
            font=("Arial", 27, "bold"),
            bg=self.bg,
            fg=self.text
        ).pack(
            anchor="w"
        )

        tk.Label(
            content,
            text="Inventory & condition overview",
            font=("Arial", 11),
            bg=self.bg,
            fg=self.muted
        ).pack(
            anchor="w",
            pady=(5, 25)
        )

        # =========================
        # STATISTICS
        # =========================

        stats_frame = tk.Frame(
            content,
            bg=self.bg
        )
        stats_frame.pack(
            fill="x"
        )

        total, working, maintenance, damaged = get_equipment_stats()

        stats = [
            (str(total), "TOTAL ITEMS"),
            (str(working), "WORKING"),
            (str(maintenance), "MAINTENANCE"),
            (str(damaged), "DAMAGED")
        ]

        for value, title in stats:
            self.create_stat_card(
                stats_frame,
                value,
                title
            )

        # =========================
        # QUICK ACTIONS
        # =========================

        tk.Label(
            content,
            text="QUICK ACTIONS",
            font=("Arial", 10, "bold"),
            bg=self.bg,
            fg=self.muted
        ).pack(
            anchor="w",
            pady=(30, 12)
        )

        actions_frame = tk.Frame(
            content,
            bg=self.bg
        )
        actions_frame.pack(
            fill="x"
        )

        actions = [
            ("+  Add Equipment", self.show_add_equipment),
            ("Equipment List", self.show_equipment)
        ]

        for action, command in actions:
            tk.Button(
                actions_frame,
                text=action,
                font=("Arial", 10, "bold"),
                bg=self.card,
                fg=self.text,
                activebackground=self.border,
                activeforeground=self.text,
                relief="flat",
                padx=20,
                pady=12,
                cursor="hand2",
                command=command
            ).pack(
                side="left",
                padx=(0, 10)
            )

        # =========================
        # RECENT EQUIPMENT
        # =========================

        tk.Label(
            content,
            text="RECENT EQUIPMENT",
            font=("Arial", 10, "bold"),
            bg=self.bg,
            fg=self.muted
        ).pack(
            anchor="w",
            pady=(30, 12)
        )

        recent_frame = tk.Frame(
            content,
            bg=self.panel
        )
        recent_frame.pack(
            fill="both",
            expand=True
        )

        equipment = [
            ("Dell OptiPlex", "Computer Lab", "Working"),
            ("Epson Projector", "Multimedia Lab", "Maintenance"),
            ("Cisco Switch", "Networking Lab", "Working")
        ]

        for name, lab, status in equipment:
            row = tk.Frame(
                recent_frame,
                bg=self.panel,
                height=45
            )
            row.pack(
                fill="x",
                padx=15,
                pady=3
            )
            row.pack_propagate(False)

            tk.Label(
                row,
                text=name,
                font=("Arial", 10, "bold"),
                bg=self.panel,
                fg=self.text,
                width=25,
                anchor="w"
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=lab,
                font=("Arial", 10),
                bg=self.panel,
                fg=self.muted,
                width=25,
                anchor="w"
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=status,
                font=("Arial", 10),
                bg=self.panel,
                fg=self.accent,
                anchor="w"
            ).pack(
                side="left"
            )

    def create_stat_card(self, parent, value, title):
        card = tk.Frame(
            parent,
            bg=self.card,
            height=110
        )
        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )
        card.pack_propagate(False)

        tk.Label(
            card,
            text=value,
            font=("Arial", 25, "bold"),
            bg=self.card,
            fg=self.text
        ).pack(
            anchor="w",
            padx=18,
            pady=(18, 2)
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 9, "bold"),
            bg=self.card,
            fg=self.muted
        ).pack(
            anchor="w",
            padx=18
        )