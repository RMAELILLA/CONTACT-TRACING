import tkinter as tk
from tkinter import messagebox

class QuestionsFrame(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        self.master = master
        self.back_callback = back_callback
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
        if self.current_question == 2:
            self.question_label.config(text="When was your most visit to this location?")
            self.show_entry_for_location_visit()
        elif self.current_question == 3:
            self.question_label.config(text="Since then until today, what places have you been? (besides home)")
            self.show_entry_for_places_visited()
        elif self.current_question == 4:
            if any(answer.startswith("Yes") for answer in self.answers[3:]):
                if self.answers[3] == "Yes - Positive" or self.answers[4] == "Yes - Positive" or self.answers[4] == "Yes - Pending":
                    self.question_label.config(text="Additional question for Positive case:")
                    self.show_additional_question_positive_case()
                else:
                    self.additional_questions_displayed = True
                    self.show_additional_questions()
        elif self.current_question == 5:
            self.additional_questions_displayed = True
            self.show_additional_questions()

    def show_additional_question_positive_case(self):
        self.selected_option.set("")
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        tk.Radiobutton(self.option_frame, text="Yes", variable=self.selected_option, value="Yes").pack(anchor='w')
        tk.Radiobutton(self.option_frame, text="No", variable=self.selected_option, value="No").pack(anchor='w')
        self.next_button.config(command=self.save_additional_question_positive_case)
    
    def save_additional_question_positive_case(self):
        answer = self.selected_option.get()
        if answer:
            self.answers.append(answer)
            self.show_next_question()
        else:
            messagebox.showerror("Error", "Please select an option for the current question.")

    def show_entry_for_location_visit(self):
        self.selected_option.set("")
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        self.location_visit_entry = tk.Entry(self.option_frame)
        self.location_visit_entry.pack(padx=10, pady=5)
        self.next_button.config(command=self.save_location_visit)

    def save_location_visit(self):
        location_visit = self.location_visit_entry.get()
        if location_visit:
            self.answers.append(location_visit)
            self.show_next_question()
        else:
            messagebox.showerror("Error", "Please enter the location visit.")

    def show_entry_for_places_visited(self):
        self.selected_option.set("")
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        self.places_visited_entry = tk.Entry(self.option_frame)
        self.places_visited_entry.pack(padx=10, pady=5)
        self.next_button.config(command=self.save_places_visited)

    def save_places_visited(self):
        places_visited = self.places_visited_entry.get()
        if places_visited:
            self.answers.append(places_visited)
            self.show_next_question()
        else:
            messagebox.showerror("Error", "Please enter the places visited.")

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