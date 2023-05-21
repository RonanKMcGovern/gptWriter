from getGptResponse import get_openai_response
from getUpdateJson import extract_json_from_file
from updateData import update_crm_data

def process_command(command):
    # Generate OpenAI response
    response = get_openai_response(command)

    # Save response to a file
    with open('gptResponse.txt', 'w') as file:
        file.write(response)

    # Extract JSON from the response
    extract_json_from_file('gptResponse.txt')

    # Update CRM data
    update_crm_data()

# Example usage
if __name__ == '__main__':
    command = "Update 123 Industries email to yowdy@michael.johnson"
    process_command(command)
