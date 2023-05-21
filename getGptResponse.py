import os
from dotenv import load_dotenv
import csv
import openai
import json

# Load .env file
load_dotenv(dotenv_path='.env')

# Setup OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_openai_response(context):
    messages = [
        {"role": "system", "content": "You are a helpful assistant and json expert."},
        {"role": "user", "content": context},
        {"role": "assistant", "content": "Thanks for this information."},
        {"role": "user", "content": "Based on this information, provide an HTML code snippet that begins with a title in <h1> format, continues with a three-bullet summary using <ul> tags, and finishes with a summary of no more than 300 words. Make sure to start your response with the title."}
    ]
    
    try:
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages
        )
        response_text = response.choices[0].message['content']
        print(f"OpenAI Response text: {response_text[:50]}")
        return response_text
    except Exception as e:
        print(f"Error generating OpenAI response: {str(e)}")
        raise Exception(f"Failed to generate OpenAI response. {str(e)}")

def read_user_input():
    with open("userInput.txt", "r") as file:
        return file.read()

def read_crm_input():
    with open('crmInput.csv', 'r') as file:
        csvreader = csv.reader(file)
        # return the CSV data as string
        return json.dumps(list(csvreader))

def main():
    userInput = read_user_input()
    crmInput = read_crm_input()

    context = userInput + " " + crmInput
    get_openai_response(context)

if __name__ == '__main__':
    main()
