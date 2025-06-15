# 🔌 API Security Labs

This section explores vulnerabilities and misconfigurations in **APIs (Application Programming Interfaces)** — one of the most frequent attack surfaces in modern applications.

These examples are created for **educational and research purposes only**, and do **not** include fully functional backends or vulnerable services by default.

---

## 📁 Lab Structure

| Folder                   | Focus Area                              |
|--------------------------|------------------------------------------|
| `01_GraphQL/`            | GraphQL introspection, injection        |
| `02_NoSQL_Injection/`    | Mongo-style injection & filters abuse   |
| `03_JWT_Kid_Manip/`      | JWT `kid` header tampering              |
| `04_RateLimit_Bypass/`   | Exploiting improper rate limiting       |

---

## ⚠️ Disclaimer

> **Important Note**  
This repository **does not include actual vulnerable APIs** or server implementations for safety reasons. It provides:
- Sample requests and responses
- Payload crafting logic
- Common vulnerable patterns
- Static or emulated code samples

🔒 Use responsibly on controlled, sandboxed, or lab environments **you own**.

---

## 🧪 Recommended Usage

- Use with tools like Postman, Burp Suite, or `curl`
- Simulate behavior with mocked APIs (e.g., Flask, Express, Mock Service Worker)
- Ideal for:
  - Red Teamers
  - Bug Bounty Hunters
  - Security Engineers

---

## 🔧 Tools You May Use

- Burp Suite / ZAP Proxy
- Postman / Insomnia
- JWT.io / jwt_tool
- GraphQL Voyager / GraphQLmap
- NoSQLMap
- Slowloris / Turbo Intruder (for rate limit fuzzing)

---

## 📚 License

MIT License — for educational and ethical testing only.
