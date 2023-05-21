import json

# Read the file
with open('gptResponse.txt', 'r') as file:
    json_str = file.read()

# Convert JSON string to dictionary
json_dict = json.loads(json_str)

# Write to new JSON file
with open('output.json', 'w') as file:
    json.dump(json_dict, file, indent=4)
