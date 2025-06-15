# 🌐 LifeAroundWebAttacks

This repository contains categorized, minimal yet realistic examples of common and modern web application attacks.  
These are designed specifically for **red teamers**, **security engineers**, and **CTF practitioners** focused on understanding the offensive edge of web vulnerabilities.

---

## 📁 Structure

| Module         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `ClassicWeb/`  | Old-school but still relevant attacks like SQLi, XSS, CSRF, file uploads.   |
| `ModernWeb/`   | Advanced & evolving vulnerabilities like JWT abuse, WebSockets, SSRF, etc.  |
| `APIAttacks/`  | API-specific exploits including GraphQL, CORS, NoSQLi, Race Conditions.     |

Each subfolder contains:
- `.html`, `.graphql`, `.http`, or `.py` attack examples
- No backend or actual server-side logic (for safety)
- Optional request files for Postman/Burp, or replay automation

---

## 🚨 Safety Disclaimer

> All examples are **non-functional** and contain no backend components or actual payload execution mechanisms.  
These are purely **educational** and are meant for **controlled environments** or **internal lab testing** only.

---

## 📌 Recommended Usage

- Use as reference during labs (TryHackMe, HackTheBox, PortSwigger).
- Practice with intentionally vulnerable apps (DVWA, bWAPP, Juice Shop).
- Use snippets in CTFs or internal red team tools.
- Expand modules with your own `*.http`, `*.graphql`, or PoC scripts.

---

## 🧰 Upcoming Modules

- `05_CORS_Misconfig/`
- `06_WebCache_Poisoning/`
- `07_DOM_Based_Vulns/`
- `08_Business_Logic_Breaks/`

---

> Built by red teamers, for red teamers. 🔥
