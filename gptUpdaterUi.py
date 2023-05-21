from getGptResponse import get_openai_response
from getUpdateJson import extract_json_from_file
from updateData import update_crm_data

def process_command(command):
    # Generate OpenAI response
    temp = get_openai_response(command)

    # Save response to a file
    with open('gptResponse.txt', 'w') as file:
        file.write(temp)

    # Extract JSON from the response
    extract_json_from_file('gptResponse.txt')

    # Update CRM data
    response = update_crm_data()

    # Return response
    return response

