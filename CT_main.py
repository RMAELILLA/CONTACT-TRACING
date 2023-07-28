import tkinter as tk
from tkinter import messagebox
from contact_info import ContactInfoFrame
from questions import QuestionsFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Contact Tracing App")
        self.contact_info_frame = ContactInfoFrame(self, self.show_questions_frame)
        self.questions_frame = QuestionsFrame(self, self.show_contact_info_frame)

        self.contact_info_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.questions_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.questions_frame.grid_forget()  # Hide the QuestionsFrame initially

    def show_contact_info_frame(self):
        self.questions_frame.grid_forget()
        self.contact_info_frame.grid()

    def show_questions_frame(self):
        contact_info = self.contact_info_frame.get_contact_info()
        if contact_info:
            self.questions_frame.contact_info = contact_info
            self.contact_info_frame.grid_forget()
            self.questions_frame.grid()
        else:
            tk.messagebox.showerror("Error", "Please fill in all contact details.")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()