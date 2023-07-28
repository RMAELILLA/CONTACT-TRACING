    # Prompt each frame for each number
import tkinter as tk
from tkinter import messagebox

class QuestionsFrame(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        self.master = master
        self.back_callback = back_callback

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
             "Difficulty in Breathing", "Loss of Taste", "Loss of Smell"],
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

    # prompt only 
        #if in number 3-4 = "yes" and in number 5 ="Yes-Positve or Yes-pending"
            # When was your most visit to this location?
            # Since then until today, what places have you been? (beside home)