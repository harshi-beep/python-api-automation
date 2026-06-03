import requests

# Paste your BRAND NEW credentials here
CLIENT_ID = "Ov23li1VAYdsIrGKzpQ4"
CLIENT_SECRET = "154af337c1527b46865be955f5eacc02b979d631"

def run_backup_flow():
    print("==========================================")
    print("🚀 Manual OAuth Flow Initialization")
    print("==========================================\n")
    
    # Manually constructed URL to ensure no library formatting issues
    auth_url = f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&redirect_uri=http://localhost:8000/callback&scope=user"
    
    print("👉 STEP 1: Copy and paste this exact URL into your browser:\n")
    print(auth_url)
    print("\n==========================================")
    
    redirect_url = input("\n👉 STEP 2: Paste the full broken localhost URL here: ").strip()
    
    # Extract the code parameter manually out of the URL string
    try:
        code = redirect_url.split("code=")[1].split("&")[0]
    except IndexError:
        print("❌ Error: Could not find the 'code=' part in the URL you pasted. Try again!")
        return

    print(f"\n🔄 Code extracted: {code}")
    print("📡 Swapping code for access token...")
    
    # POST request to grab the token
    token_response = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "redirect_uri": "http://localhost:8000/callback"
        }
    )
    
    token_json = token_response.json()
    access_token = token_json.get("access_token")
    
    if not access_token:
        print("❌ Failed to get token. GitHub response:")
        print(token_json)
        return
        
    print("✅ Token Acquired successfully!")
    
    # Step 3: Hit the API
    user_response = requests.get(
        "https://api.github.com/user",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    
    print("\n🎉 Your Profile Data from GitHub API:")
    print(user_response.json())

if __name__ == "__main__":
    run_backup_flow()