# Create covid contact tracing app with GUI (Tkinter)
# Create a program that ask user for information found in covid contact tracing app

# Contact Details
    # Name
    # Email Address
    # Phone Number

# create another 2 frame after contact details
# first frame should consist the first five questions
    # Prompt each frame for each number
    # 1. Have you been vaccinated for COVID-19?
        # Not yet
        # 1st Dose
        # 2nd Dose (Fully Vaccinated)
        # 1st (Booster)
        # 2nd (Completed Booster Shot)
    # 2. Do you experience any COVID like symptoms in the past 7 days such as:
        # Fever
        # Cough
        # Colds
        # Muscle Cramps
        # sore throat
        # Diarrhea
        # Headache
        # Shortness of breath
        # Difficulty in breathing
        # Loss of Taste
        # Loss of Smell
        # None of the above
    # 3. Have you had exposure to a probable confirmed COVID cases in the last 14 days?
        # No
        # Yes
    # 4. Have you had contact with COVID like symptoms in the past 7 days?
        # NO
        # Yes
    # 5. Have you been tested for COVID-19 in the last 14 days?
        # No
        # Yes-postive
        # Yes-Negative
        # Yes-Pending

# 2nd frame should prompt only if
    # if in question number 3 and question number 4 += "yes" and if question number 5 ="Yes-Positve or Yes-pending"
        # When was your most visit to this location?
        # Since then until today, what places have you been? (beside home)
    # PROMPT ONLY IF it met the above conditions