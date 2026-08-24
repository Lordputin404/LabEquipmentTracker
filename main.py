import tkinter as tk
from database.db import get_equipment_stats
from screens.dashboard import Dashboard


def main():
    stats = get_equipment_stats()
    print("Equipment statistics:", stats)

    root = tk.Tk()
    root.title("Lab Equipment Tracker")
    root.geometry("1000x600")
    root.minsize(900, 550)

    Dashboard(root)

    root.mainloop()


if __name__ == "__main__":
    main()