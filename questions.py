import tkinter as tk
from tkinter import messagebox
from questions2 import AdditionalQuestionsFrame

class QuestionsFrame(tk.Frame):
    def __init__(self, master, reset_callback):
        super().__init__(master)
        self.master = master
        self.reset_callback = reset_callback
        self.contact_info = {}
        self.contact_info_completed = False
        self.additional_questions_displayed = False
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

        self.additional_questions_frame = None

        self.answers = []
        self.current_question = 0

        self.selected_option = tk.StringVar()

        self.question_label = tk.Label(self, text=self.questions[self.current_question])
        self.question_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

        self.option_frame = tk.Frame(self)
        self.option_frame.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        self.next_button = tk.Button(self, text="Next", command=self.save_answer)
        self.next_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.show_regular_question()
    
    def back_callback(self):
        self.additional_questions_frame.destroy()
        self.answers = []
        self.contact_info = {}
        self.show_next_question()

    def reset(self):
        self.contact_info_completed = False
        self.additional_questions_displayed = False
        self.contact_info = {}
        self.answers = []
        self.current_question = 0
        self.selected_option.set("")
        self.show_regular_question()

    def save_answer(self):
        answer = self.selected_option.get()
        if answer:
            if not self.contact_info_completed:
                contact_info = self.get_contact_info()
                if contact_info:
                    self.contact_info = contact_info
                    self.contact_info_completed = True
                else:
                    messagebox.showerror("Error", "Please fill in all contact details.")
                    return
            else:
                self.answers.append(answer)
                self.selected_option.set("")

                if self.current_question == 4 and any(answer.startswith("Yes") for answer in self.answers[3:]):
                    if self.answers[3] == "Yes - Positive" or self.answers[4] == "Yes - Positive" or self.answers[4] == "Yes - Pending":
                        self.show_additional_questions()
                        return

                self.show_next_question()
        else:
            messagebox.showerror("Error", "Please select an option for the current question.")

    def show_next_question(self):
        if self.additional_questions_displayed:
            return

        self.additional_questions_displayed = False

        if self.current_question == 1 and len(self.answers) >= 2 and self.answers[1] == "Yes":
            self.additional_questions_displayed = True
            self.show_additional_questions()
        elif self.current_question == 2 and len(self.answers) >= 3 and self.answers[2] == "Yes":
            self.additional_questions_displayed = True
            self.show_additional_questions()
        elif self.current_question == 3 and len(self.answers) >= 4 and self.answers[3] == "Yes":
            self.additional_questions_displayed = True
            self.show_additional_questions()
        elif self.current_question == 4 and len(self.answers) >= 5 and any(answer.startswith("Yes") for answer in self.answers[4:]):
            self.additional_questions_displayed = True
            self.show_additional_questions()
        else:
            if self.current_question < len(self.questions) - 1:
                self.current_question += 1
                self.show_regular_question()
            else:
                self.display_contact_details()

    def show_regular_question(self):
        self.question_label.config(text=self.questions[self.current_question])
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        for option in self.options[self.current_question]:
            tk.Radiobutton(self.option_frame, text=option, variable=self.selected_option, value=option).pack(anchor='w')

    def show_additional_questions(self):
        self.question_label.config(text="Additional Questions:")
        self.next_button.config(text="Next", command=self.save_additional_question)
        for widget in self.option_frame.winfo_children():
            widget.destroy()

        self.additional_questions_frame = AdditionalQuestionsFrame(
            self, self.contact_info, self.show_next_question, self.back_callback
        )
        self.additional_questions_frame.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
    
    def back_callback(self):
        self.additional_questions_frame.destroy()
        self.show_next_question()

    def save_additional_question(self):
        self.answers.extend(self.additional_questions_frame.answers)
        for key, value in self.contact_info.items():
            self.answers.append(f"{key}: {value}")

        self.additional_questions_frame.destroy()
        self.display_contact_details()
        self.reset_application()

    def get_contact_info(self):
        name = self.master.contact_info_frame.entry_name.get()
        email = self.master.contact_info_frame.entry_email.get()
        phone = self.master.contact_info_frame.entry_phone.get()

        if name and email and phone:
            return {
                "Name": name,
                "Email": email,
                "Phone": phone
            }
        else:
            return None

    def display_contact_details(self):
        contact_info_message = "Contact Details:\n"
        for key, value in self.contact_info.items():
            contact_info_message += f"{key}: {value}\n"

        message = contact_info_message + "\nAnswers to Questions:\n"
        for i in range(len(self.questions)):
            message += f"{i + 1}. {self.questions[i]}\nAnswer: {self.answers[i]}\n"

        messagebox.showinfo("Contact Tracing Information", message)
        self.back_callback()

        self.contact_info_completed = False
        self.contact_info = {}
