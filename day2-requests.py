import requests

print("=========================================")
print("🚀 DAY 2: AUTOMATING APIs WITH PYTHON")
print("=========================================\n")

# ---------------------------------------------------
# 1. GET REQUEST - GitHub User Profile with Error Handling
# ---------------------------------------------------
print("[Testing GET: GitHub Profile]")
try:
    response = requests.get("https://api.github.com/users/harshi-beep")
    
    # Check if the request was successful (200 OK)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Success! Status Code: {response.status_code}")
        print(f"👤 Login Name:  {data['login']}")
        print(f"📂 Public Repos: {data['public_repos']}")
        print(f"👥 Followers:    {data['followers']}\n")
    else:
        print(f"❌ Error: Received status code {response.status_code}\n")

except Exception as e:
    print(f"💥 Connection Error: {e}")


# ---------------------------------------------------
# 2. GET REQUEST - List First 5 Repositories
# ---------------------------------------------------
print("[Testing GET: GitHub Repositories]")
try:
    repo_response = requests.get("https://api.github.com/users/harshi-beep/repos")
    
    if repo_response.status_code == 200:
        repos = repo_response.json()
        print(f"✅ Success! Found {len(repos)} repositories.")
        print("--- First 5 Repos ---")
        for repo in repos[:5]:
            print(f"- {repo['name']}")
        print("")
    else:
        print(f"❌ Error fetching repos: Status {repo_response.status_code}\n")
        
except Exception as e:
    print(f"💥 Connection Error: {e}")


# ---------------------------------------------------
# 3. POST REQUEST - Create data on JSONPlaceholder
# ---------------------------------------------------
print("[Testing POST: Creating Fake Post]")
new_post = {
    "title": "Day 2 API Test",
    "body": "Testing POST with Python requests",
    "userId": 1
}

try:
    post_response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post
    )
    
    # POST success is typically 201 Created
    if post_response.status_code == 201:
        print(f"✅ Success! Status Code: {post_response.status_code}")
        print(f"🆔 Created Resource ID: {post_response.json()['id']}\n")
    else:
        print(f"❌ Error creating post: Status {post_response.status_code}\n")

except Exception as e:
    print(f"💥 Connection Error: {e}")

print("=========================================")
print("🏁 Automation Script Execution Finished!")
print("=========================================")