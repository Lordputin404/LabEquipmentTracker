import tkinter as tk
from screens.dashboard import Dashboard
from screens.equipment import Equipment
from screens.add_equipment import AddEquipment


class App:
    def __init__(self, root):
        self.root = root

        self.root.title("Lab Equipment Tracker")
        self.root.geometry("1000x600")
        self.root.minsize(900, 550)

        self.show_dashboard()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_screen()
        Dashboard(self.root, self.show_dashboard, self.show_equipment, self.show_add_equipment)

    def show_equipment(self):
        self.clear_screen()
        Equipment(self.root, self.show_dashboard, self.show_equipment, self.show_add_equipment)

    def show_add_equipment(self):
        self.clear_screen()
        AddEquipment(self.root, self.show_dashboard, self.show_equipment)


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()