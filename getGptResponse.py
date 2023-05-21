import os
import csv
import json
from dotenv import load_dotenv
import openai

# Load .env file
load_dotenv(dotenv_path='.env')

# Setup OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        return json.dumps(list(csvreader))

def get_openai_response(user_input, crm_input_file="crmInput.csv", sample_output_file="sampleOutput.txt"):
    # Read the contents from the files
    crm_input = read_csv_file(crm_input_file)
    sample_output = read_file(sample_output_file)

    messages = [
        {"role": "system", "content": "You are a helpful assistant and JSON expert."},
        {"role": "user", "content": "I am going to provide you with some input data along with a command. I would like you provide me with a JSON object as a response with same keys as the sample output I will provide."},
        {"role": "assistant", "content": "Thanks for this guidance."},
        {"role": "user", "content": f"Here is a sample output: {sample_output}."},
        {"role": "assistant", "content": "Thanks for this sample output."},
        {"role": "user", "content": f"Here is the input data: {crm_input}."},
        {"role": "assistant", "content": "Thanks for this input data."},
        {"role": "user", "content": f"Here is the command: {user_input}."},
    ]

    print(messages)
    
    try:
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages
        )
        response_text = response.choices[0].message['content']
        
        # Write to file instead of console
        with open('gptResponse.txt', 'w') as file:
            file.write(response_text)
        
        return response_text
    except Exception as e:
        raise Exception(f"Failed to generate OpenAI response: {str(e)}") from e

def process_openai_response(user_input):

    user_input = read_file(user_input)

    return get_openai_response(user_input)
# Example usage
if __name__ == '__main__':
    user_input = read_file("userInput.txt")
    response = process_openai_response(user_input)
    print(response)