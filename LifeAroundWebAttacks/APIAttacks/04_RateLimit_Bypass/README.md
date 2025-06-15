# 🧨 Rate Limiting Bypass Strategies

APIs and login forms implement rate limiting to block brute-force and abuse. Poor implementations allow attackers to **evade detection** and **continue attacks**.

## 🧠 Techniques to Bypass

### 1. IP Spoofing via Headers
If backend relies on HTTP headers for IP detection:
X-Forwarded-For: 127.0.0.1
X-Client-IP: 192.168.1.1
X-Real-IP: 10.10.10.10
Forwarded: for=192.0.2.60

### 2. Parallelization
Run attacks across multiple processes, endpoints, or distributed IPs.

### 3. URL/Param Obfuscation
Examples like:
/login?username=admin
/login/?username=admin
/login#@?username=admin

### 4. Header Token Rotation
Rotate Bearer tokens to reset counters.

### 5. Cookie Regeneration
Re-fetch forms to get fresh tokens.

### 6. Response Time Profiling
Use timing to detect rate limit triggers.

## 🛠 Tools
ffuf, Burp Intruder, Python + requests

## 🎯 Targets
Login forms, API keys, CAPTCHA, password reset abuse
