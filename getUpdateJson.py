import json

# Read the file
with open('gptResponse.txt', 'r') as file:
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
