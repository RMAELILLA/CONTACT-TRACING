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