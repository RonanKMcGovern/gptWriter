import os
import csv
import json
from dotenv import load_dotenv
import openai

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        return json.dumps(list(csvreader))

def get_openai_response(user_input, crm_input, sample_output):
    messages = [
        {"role": "system", "content": "You are a helpful assistant and JSON expert."},
        {"role": "user", "content": "I am going to provide you with some input data and a command on how I would like to update that data. I expect a response in JSON format that will be helpful as an input for me to update a database."},
        {"role": "assistant", "content": "Thanks for this guidance."},
        {"role": "user", "content": f"Here is a sample output: {sample_output}."},
        {"role": "assistant", "content": "Thanks for this sample output."},
        {"role": "user", "content": f"Here is the input data: {crm_input}."},
        {"role": "assistant", "content": "Thanks for this input data."},
        {"role": "user", "content": f"Here is the command: {user_input}."},
    ]
    
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

def main():
    # Load .env file
    load_dotenv(dotenv_path='.env')

    # Setup OpenAI
    openai.api_key = os.getenv('OPENAI_API_KEY')

    user_input = read_file("userInput.txt")
    crm_input = read_csv_file('crmInput.csv')
    sample_output = read_file("sampleOutput.txt")

    get_openai_response(user_input, crm_input, sample_output)

if __name__ == '__main__':
    main()
