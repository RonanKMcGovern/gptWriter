import subprocess

# Call getGptResponse.py
subprocess.run(['python', 'getGptResponse.py'], check=True)

# Call getUpdateJson.py
subprocess.run(['python', 'getUpdateJson.py'], check=True)

# Call updateData.py
subprocess.run(['python', 'updateData.py'], check=True)
