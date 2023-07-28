import tkinter as tk
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
        self.questions_frame.grid_forget()

    def show_contact_info_frame(self):
        self.questions_frame.grid_forget()
        self.contact_info_frame.grid()

    def show_questions_frame(self):
        self.contact_info_frame.grid_forget()
        self.questions_frame.grid()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()