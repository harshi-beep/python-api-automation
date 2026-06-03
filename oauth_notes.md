# Day 3: OAuth 2.0 and JWT Security Notes

## 🔑 What is OAuth 2.0?
OAuth 2.0 is an authorization framework that allows web applications to securely obtain limited access to user profiles and cloud services (like Google or GitHub) without ever needing the user's login password.

## 🔄 The Token Exchange Workflow
Using the Google OAuth 2.0 Playground, I successfully tracked the complete web authorization code flow:
1. **Scope Selection:** Requested target user scopes (`userinfo.profile` and `openid`).
2. **User Consent:** Authenticated via standard secure login prompts to allow account tracking.
3. **Authorization Code:** Received a temporary verification code string starting with `4/0Aeo...`.
4. **Token Exchange:** Sent that temporary code to Google's tokens backend to return a structurally validated JSON Web Token (`id_token`).

## 🎟️ Analyzing the JSON Web Token (JWT)
Pasting the generated token payload directly into the `jwt.io` interactive debugger visually broke down our identity credentials into three crucial components:
* **Header:** Specified the standard asymmetric encryption metadata used (`RS256`).
* **Payload:** Openly exposed user account strings verifying my name (`"harshu gowda"`) and specific app access fields.
* **Signature:** Handled server check sequences ensuring cryptographic validity.

## 📸 JWT Decoded Screenshot Evidence
![JWT Decoded](./jwt_decoded.png)