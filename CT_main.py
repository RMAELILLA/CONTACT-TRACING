import tkinter as tk
from tkinter import messagebox
import csv
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

        self.collected_data = []

    def show_contact_info_frame(self):
        self.questions_frame.grid_forget()
        self.contact_info_frame.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.reset_application()

    def show_questions_frame(self):
        contact_info = self.contact_info_frame.get_contact_info()
        if contact_info:
            self.questions_frame.contact_info = contact_info
            self.contact_info_frame.grid_forget()
            self.show_next_question()
        else:
            tk.messagebox.showerror("Error", "Please fill in all contact details.")

    def show_next_question(self):
        if self.questions_frame.current_question < len(self.questions_frame.questions):
            self.questions_frame.grid()
            self.questions_frame.show_regular_question()
        else:
            self.display_contact_details()

    def display_contact_details(self):
        contact_info_message = "Contact Details:\n"
        for key, value in self.questions_frame.contact_info.items():
            contact_info_message += f"{key}: {value}\n"

        message = contact_info_message + "\nAnswers to Questions:\n"
        for i in range(len(self.questions_frame.questions)):
            message += f"{i + 1}. {self.questions_frame.questions[i]}\nAnswer: {self.questions_frame.answers[i]}\n"

        self.collected_data.append(self.questions_frame.contact_info)
        self.collected_data[-1].update(dict(zip(self.questions_frame.questions, self.questions_frame.answers)))

        messagebox.showinfo("Contact Tracing Information", message)
        self.reset_application()

        if self.questions_frame.current_question == len(self.questions_frame.questions):
            self.write_to_csv()

    def reset_application(self):
        if self.questions_frame:
            self.questions_frame.reset()
            self.questions_frame.destroy()
            self.questions_frame = None

        self.contact_info_frame.reset()

    def write_to_csv(self):
        try:
            with open("ctdata.csv", mode="w", newline="") as csvfile:
                fieldnames = ["Name", "Email", "Phone"] + self.questions_frame.questions
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for data in self.collected_data:
                    writer.writerow(data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write to CSV file: {e}")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
