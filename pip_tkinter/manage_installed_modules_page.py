import tkinter as tk
from tkinter import ttk

class ManageInstalledPage(tk.Tk):
    """
    Ask user about what to do :
    1. Install
    2. Uninstall or Update
    """

    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.parent = root
        self.parent.title("PIP Package Manager")
        self.parent.rowconfigure(0, weight=1)
        self.parent.columnconfigure(0, weight=1)
        theme_style = ttk.Style()
        if 'clam' in theme_style.theme_names():
            theme_style.theme_use('clam')

if __name__ == "__main__":

    # If you want to check GUI
    root = tk.Tk()
    # root.resizable(width='false', height='false')
    manage_installed_app = ManageInstalledPage(root)
    root.mainloop()
