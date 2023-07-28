import tkinter as tk
from tkinter import messagebox

class QuestionsFrame(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        self.master = master
        self.back_callback = back_callback
        self.contact_info = {}

        self.questions = [
            "Have you been vaccinated for COVID-19?",
            "Do you experience any COVID-like symptoms in the past 7 days such as:",
            "Have you had exposure to a probable confirmed COVID cases in the last 14 days?",
            "Have you had contact with COVID-like symptoms in the past 7 days?",
            "Have you been tested for COVID-19 in the last 14 days?"
        ]

        self.options = [
            ["Not yet", "1st Dose", "2nd Dose (Fully Vaccinated)", "1st (Booster)", "2nd (Completed Booster Shot)"],
            ["Fever", "Cough", "Colds", "Muscle Cramps", "Sore Throat", "Diarrhea", "Headache", "Shortness of Breath",
             "Difficulty in Breathing", "Loss of Taste", "Loss of Smell", "None of the above"],
            ["No", "Yes"],
            ["No", "Yes"],
            ["No", "Yes - Positive", "Yes - Negative", "Yes - Pending"]
        ]

        self.answers = []
        self.current_question = 0
        self.display_additional_questions = False
        self.completed = False

        self.selected_option = tk.StringVar()

        self.question_label = tk.Label(self, text=self.questions[self.current_question])
        self.question_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.option_frame = tk.Frame(self)
        self.option_frame.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        self.next_button = tk.Button(self, text="Next", command=self.save_answer)
        self.next_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.show_next_question()

    def save_answer(self):
        answer = self.selected_option.get()
        if answer:
            self.answers.append(answer)
            self.selected_option.set("")  # Reset the selected_option variable
            self.show_next_question()
        else:
            messagebox.showerror("Error", "Please select an option for the current question.")

    def show_next_question(self):
        if self.display_additional_questions:
            self.show_additional_questions()
        elif self.completed:
            return
        else:
            if self.current_question == 2 and len(self.answers) >= 3:
                if self.answers[2] == "Yes":
                    self.display_additional_questions = True
                    self.show_additional_questions()
                    return
            elif self.current_question == 3 and len(self.answers) >= 4:
                if self.answers[3] == "Yes":
                    self.display_additional_questions = True
                    self.show_additional_questions()
                    return
            elif self.current_question == 4 and len(self.answers) >= 5:
                if "Yes" in self.answers[4]:
                    self.display_additional_questions = True
                    self.show_additional_questions()
                    return

            if self.current_question < len(self.questions):
                self.show_regular_question()
                self.current_question += 1
            else:
                self.display_contact_details()

    def show_regular_question(self):
        self.question_label.config(text=self.questions[self.current_question])
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        for option in self.options[self.current_question]:
            tk.Radiobutton(self.option_frame, text=option, variable=self.selected_option, value=option).pack(anchor='w')

    def show_additional_questions(self):
        if self.current_question == 2:
            self.question_label.config(text="When was your most visit to this location?")
            self.show_entry_for_location_visit()
        elif self.current_question == 3:
            self.question_label.config(text="Since then until today, what places have you been? (besides home)")
            self.show_entry_for_places_visited()

    def display_contact_details(self):
        contact_info_message = "Contact Details:\n"
        for key, value in self.contact_info.items():
            contact_info_message += f"{key}: {value}\n"

        message = contact_info_message + "\nAnswers to Questions:\n"
        for i in range(len(self.questions)):
            message += f"{i + 1}. {self.questions[i]}\nAnswer: {self.answers[i]}\n"

        messagebox.showinfo("Contact Tracing Information", message)
        self.back_callback()