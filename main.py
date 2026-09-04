import tkinter as tk
from screens.add_equipment import AddEquipment


def main():
    root = tk.Tk()
    root.title("Lab Equipment Tracker")
    root.geometry("1000x600")
    root.minsize(900, 550)

    AddEquipment(root)

    root.mainloop()


if __name__ == "__main__":
    main()