import json

def extract_json_from_file(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        json_str = file.read()

    # Find the JSON object in the text
    start_index = json_str.find("{")
    end_index = json_str.rfind("}") + 1
    json_str = json_str[start_index:end_index]

    # Convert JSON string to dictionary
    json_dict = json.loads(json_str)

    # Write to new JSON file
    with open('updateJson.json', 'w') as file:
        json.dump(json_dict, file, indent=4)

# Example usage
if __name__ == '__main__':
    file_path = 'gptResponse.txt'
    extract_json_from_file(file_path)