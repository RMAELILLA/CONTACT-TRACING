import csv

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

    exposure_response = input("\n3. Have you had exposure to a probable confirmed COVID case in the last 14 days? (y/n): ")
    contact_details["Exposure to Probable Confirmed COVID Cases"] = "Yes" if exposure_response.lower() == 'y' else "No"

    contact_symptoms_response = input("\n4. Have you had contact with someone with COVID-like symptoms in the past 7 days? (y/n): ")
    contact_details["Contact with COVID-like Symptoms"] = "Yes" if contact_symptoms_response.lower() == 'y' else "No"

    testing_options = ["No", "Yes-positive", "Yes-Negative", "Yes-Pending"]
    testing_response = int(input("\n5. Have you been tested for COVID-19 in the last 14 days? (Enter the corresponding number)\n" +
                                 "\n".join(f"{i}. {option}" for i, option in enumerate(testing_options, start=1)) +
                                 "\nYour choice: "))
    contact_details["COVID-19 Testing Status"] = testing_options[testing_response - 1]

    if (
        (exposure_response.lower() == 'y' or contact_symptoms_response.lower() == 'y') and
        (testing_options[testing_response - 1] == "Yes-positive" or testing_options[testing_response - 1] == "Yes-Pending")
    ):
        contact_details["Location of Most Recent Visit"] = input("\nWhen was your most recent visit to this location? ")
        contact_details["Places Visited Since Most Recent Visit"] = input("\nSince then until today, what places have you been? (beside home) ")

    other_contact_details = {
        "Name": input("\nOther Contact Details - Name: "),
        "Relation to the contact person": input("Other Contact Details - Relation to the contact person: "),
        "Contact Number": input("Other Contact Details - Contact Number: ")
    }

    with open("contact_tracing_info.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=[*contact_details, *other_contact_details])
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({**contact_details, **other_contact_details})