import csv
import json

def update_crm_data():
    # Read the input variables from updateJson.json
    with open("updateJson.json", "r") as file:
        data = json.load(file)
        csv_file = data["csv_file"]
        search_value = data["search_value"]
        update_key = data["update_key"]
        update_value = data["update_value"]

    # Open the CSV file and create a list to hold the updated data
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        crm_data = list(reader)

    # Variable to store the update explanation
    update_explanation = ""

    # Iterate through the CRM data and update the key-value pair for the search value
    for prospect in crm_data:
        if prospect['Company'] == search_value:
            # Check if the value is already up to date
            if prospect[update_key] != update_value:
                update_explanation = f"Updated '{update_key}' for '{search_value}' from '{prospect[update_key]}' to '{update_value}'."
                prospect[update_key] = update_value
            else:
                update_explanation = f"No update made. '{update_key}' for '{search_value}' is already '{update_value}'."

    # Write the updated data back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        fieldnames = crm_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(crm_data)

    # Log the update explanation to the console
    print(update_explanation)

# Example usage
update_crm_data()
