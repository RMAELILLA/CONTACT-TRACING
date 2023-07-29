def collect_information():
    contact_details = {
        "Name": input("Enter your name: "),
        "Email Address": input("Enter your email address: "),
        "Phone Number": input("Enter your phone number: ")
    }

    vaccination_options = [
        "Not yet",
        "1st Dose",
        "2nd Dose (Fully Vaccinated)",
        "1st (Booster)",
        "2nd (Completed Booster Shot)"
    ]
    vaccination_response = int(input("1. Have you been vaccinated for COVID-19? (Enter the corresponding number)\n" +
                                     "\n".join(f"{i}. {option}" for i, option in enumerate(vaccination_options, start=1)) +
                                     "\nYour choice: "))
    contact_details["Vaccination Status"] = vaccination_options[vaccination_response - 1]

    covid_symptoms_options = [
        "Fever", "Cough", "Colds", "Muscle Cramps", "Sore throat", "Diarrhea",
        "Headache", "Shortness of breath", "Difficulty in breathing",
        "Loss of Taste", "Loss of Smell", "None of the above"
    ]
    print("\n2. Do you experience any COVID-like symptoms in the past 7 days?")
    print("Enter 'y' for Yes and 'n' for No (e.g., ynnynny).")
    symptoms_response = input("".join(f"{i}. {option}\n" for i, option in enumerate(covid_symptoms_options, start=1)))
    contact_details["COVID-like Symptoms"] = ", ".join(
        symptom for symptom, response in zip(covid_symptoms_options, symptoms_response) if response.lower() == 'y'
    )

    if (
        (exposure_response.lower() == 'y' or contact_symptoms_response.lower() == 'y') and
        (testing_options[testing_response - 1] == "Yes-positive" or testing_options[testing_response - 1] == "Yes-Pending")
    ):
        contact_details["Location of Most Recent Visit"] = input("\nWhen was your most recent visit to this location? ")
        contact_details["Places Visited Since Most Recent Visit"] = input("\nSince then until today, what places have you been? (beside home) ")