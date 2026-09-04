import tkinter as tk
from screens.equipment import Equipment


def main():
    root = tk.Tk()
    root.title("Lab Equipment Tracker")
    root.geometry("1000x600")
    root.minsize(900, 550)

    Equipment(root)

    root.mainloop()


if __name__ == "__main__":
    main()