import requests

# 1. Configuration
# Paste your token here (Keep the quotes around it)
# 1. Configuration
TOKEN = 'REMOVED_FOR_SECURITY_BYPASS'
REPO_NAME = 'automated-api-repo'

# 2. Setup the API URL and Secure Headers
url = "https://api.github.com/user/repos"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# 3. Define the settings for your new repository
repo_data = {
    "name": REPO_NAME,
    "description": "This repository was created automatically using a Python script!",
    "private": True,  # Making it private for safety
    "has_issues": True,
    "has_projects": True,
    "has_wiki": True
}

print(f"🚀 Sending request to GitHub to create '{REPO_NAME}'...")

# 4. Make the POST request to create the repository
response = requests.post(url, json=repo_data, headers=headers)

# 5. Check the results
if response.status_code == 201:
    print("🎉 Success! Your new repository has been created.")
    # Extract the web URL from the JSON response
    repo_url = response.json()['html_url']
    print(f"🔗 View it live here: {repo_url}")
else:
    print(f"❌ Failed to create repository. Status Code: {response.status_code}")
    print(f"Error Details: {response.text}")