import csv

def get_user_input(prompt, options=None):
    while True:
        try:
            if options:
                response = int(input(prompt))
                if 1 <= response <= len(options):
                    return response
                else:
                    raise ValueError
            else:
                response = input(prompt).strip().lower()
                if response in ['y', 'n']:
                    return response
                elif not response:
                    raise ValueError
                else:
                    raise ValueError
        except ValueError:
            print("Invalid input. Please try again.")

def collect_information():
    while True:
        try:
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
            print("\n1. Have you been vaccinated for COVID-19?")
            vaccination_response = get_user_input(
                "\n".join(f"{i}. {option}" for i, option in enumerate(vaccination_options, start=1)) + "\nYour choice: ",
                vaccination_options
            )
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

            print("\n3. Have you had exposure to a probable confirmed COVID case in the last 14 days?")
            exposure_response = get_user_input("Enter 'y' for Yes and 'n' for No: ")
            contact_details["Exposure to Probable Confirmed COVID Cases"] = "Yes" if exposure_response == 'y' else "No"

            print("\n4. Have you had contact with someone with COVID-like symptoms in the past 7 days?")
            contact_symptoms_response = get_user_input("Enter 'y' for Yes and 'n' for No: ")
            contact_details["Contact with COVID-like Symptoms"] = "Yes" if contact_symptoms_response == 'y' else "No"

            testing_options = ["No", "Yes-positive", "Yes-Negative", "Yes-Pending"]
            print("\n5. Have you been tested for COVID-19 in the last 14 days?")
            testing_response = get_user_input(
                "\n".join(f"{i}. {option}" for i, option in enumerate(testing_options, start=1)) + "\nYour choice: ",
                testing_options
            )
            contact_details["COVID-19 Testing Status"] = testing_options[testing_response - 1]

            if (
                (exposure_response == 'y' or contact_symptoms_response == 'y') and
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

            print("Information successfully recorded in 'contact_tracing_info.csv'.\n")

            another_entry_response = get_user_input("Do you want to record information for another contact tracing? (y/n): ")
            if another_entry_response == 'n':
                break

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    collect_information()