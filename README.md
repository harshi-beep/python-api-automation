# GitHub OAuth 2.0 Integration Lab

This repository contains a Python implementation of the three-legged OAuth 2.0 Authorization Flow to securely interact with the production GitHub API.

## 🛠️ Dependencies
* `requests`

## ⚙️ How It Works
1. **Redirection:** The application generates a tailored authorization link pointing to GitHub's secure servers.
2. **Authorization:** The user authenticates natively through GitHub, granting access to public profile data.
3. **Exchange:** The script captures the temporary authorization callback code and exchanges it directly for an API access token.
4. **Consumption:** The script queries the `/user` endpoint to safely fetch user profile configurations.

---

# 🤖 GitHub API Automation Lab

Successfully built a Python automation script that programmatically interacts with the GitHub REST API to manage account infrastructure without manual browser intervention.

## ⚙️ Automation Details:
- **Script Name:** `github_automation.py`
- **Authentication:** Token-based Bearer Auth via custom HTTP headers
- **HTTP Method:** `POST`
- **Endpoint Target:** `/user/repos`
- **Result:** Automated provisioning of a private repository (`automated-api-repo`)

## 💻 Commands Run:
- `python github_automation.py`

---

# AWS Cloud Practice (Local Environment Setup)

Successfully initialized a local development workspace using the official AWS Command Line Interface (CLI) to practice secure infrastructure architecture.

## ⚙️ Environment Configuration (No-Card Method)
- **Profile:** Mock Administrator
- **Region:** `us-east-1`
- **Output Format:** JSON
- **Local Objects Created:** `sample.txt`

## 💻 CLI Commands Practiced:
- `aws configure set ...` (Configured local environment variables without a live root account)
- `echo ... > sample.txt` (Generated local assets for cloud upload testing)