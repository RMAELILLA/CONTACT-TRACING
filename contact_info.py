import tkinter as tk
from tkinter import messagebox

class ContactInfoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_name = tk.Label(self, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)

        self.label_email = tk.Label(self, text="Email Address:")
        self.label_email.grid(row=1, column=0, padx=10, pady=5)

        self.label_phone = tk.Label(self, text="Phone Number:")
        self.label_phone.grid(row=2, column=0, padx=10, pady=5)

        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)

        self.entry_phone = tk.Entry(self)
        self.entry_phone.grid(row=2, column=1, padx=10, pady=5)

        self.submit_contact_button = tk.Button(self, text="Submit", command=self.save_contact_info)
        self.submit_contact_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def save_contact_info(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if name and email and phone:
            contact_info = {
                "Name": name,
                "Email": email,
                "Phone": phone
            }
            return contact_info
        else:
            messagebox.showerror("Error", "Please fill in all contact details.")
            return None

    def get_contact_info(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if name and email and phone:
            return {
                "Name": name,
                "Email": email,
                "Phone": phone
            }
        else:
            return None