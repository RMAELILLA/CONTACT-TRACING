import tkinter as tk
from contact_info import ContactInfoFrame

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("COVID Contact Tracing App")
        self.contact_info_frame = ContactInfoFrame(self, self.show_questions_frame)
        self.questions_frame = QuestionsFrame(self, self.show_contact_info_frame)