# Exploits Repository

## Description

Welcome to the **ExploitSpace-Repo** repository, a comprehensive collection of vulnerability exploits, proof-of-concept (PoC) payloads, ctf's and reverse-engineering techniques tailored for my cybersecurity and cloud security needs. This repository documents a wide spectrum of **attack vectors** across different platforms, operating systems, cloud environments, and applications. From web-based exploits to kernel-level privilege escalation, this repository covers them all.

### Categories of Exploits Included:

- **Web Application Vulnerabilities**  
  - **SQL Injection (SQLi)**: Exploiting improper sanitization of user inputs in database queries.
  - **Cross-Site Scripting (XSS)**: Injecting malicious scripts into web pages to target users.
  - **Cross-Site Request Forgery (CSRF)**: Forcing users to execute unwanted actions.
  - **Command Injection**: Exploiting untrusted user inputs in system commands.
  - **XML External Entity (XXE)**: Attacking vulnerable XML parsers via external entity references.
  - **File Inclusion**: Remote/Local file inclusion vulnerabilities for executing arbitrary scripts.
  - **Open Redirects**: Redirecting users to malicious URLs by exploiting vulnerable web apps.
  - **Server-Side Request Forgery (SSRF)**: Triggering requests from the server to internal resources.

- **Privilege Escalation & Kernel Exploits**  
  - **Sudo Caching Vulnerabilities**: Leveraging improper configuration of Sudo to elevate privileges.
  - **Kernel Vulnerabilities**: Local privilege escalation techniques targeting Linux/Windows kernels.
  - **Dirty COW**: Exploit to gain root privileges by exploiting a race condition in the Linux kernel.
  - **Sudoers File Misconfigurations**: Escalating privileges via misconfigurations in sudoers.
  - **Stack/Heap Overflows**: Exploiting memory corruption in kernel modules for privilege escalation.

- **Network Protocol Exploits**  
  - **Man-in-the-Middle (MITM)**: Intercepting and manipulating network traffic, including SSL/TLS decryption.
  - **SMB Exploits**: Leveraging flaws in the Server Message Block (SMB) protocol for remote code execution or information leakage.
  - **DNS Spoofing**: Hijacking DNS responses to redirect users to malicious sites.
  - **ARP Spoofing**: Redirecting traffic between devices on a local network.

- **Zero-Day Exploits**  
  - **Exploit Research**: Reversing new software vulnerabilities, including those with no known patches.
  - **Advanced Evasion Techniques**: Creating custom payloads that evade detection by signature-based IDS/IPS systems.

- **Mobile Platform Exploits**  
  - **Android Exploits**: Privilege escalation and remote code execution techniques for Android devices.
  - **iOS Exploits**: Jailbreaking, privilege escalation, and sandbox bypass methods for iOS systems.

- **Cryptographic Exploits**  
  - **RSA Key Exploits**: Attacks leveraging weak cryptographic implementations (e.g., weak key generation).
  - **Side-channel Attacks**: Exploiting timing or power consumption to retrieve cryptographic keys.
  - **SSL/TLS Attacks**: Breaking SSL/TLS encryption or impersonating servers using attacks like POODLE, BEAST, and Heartbleed.

- **Reverse Engineering**  
  - **Binary Analysis**: Techniques for reverse-engineering compiled binaries (Linux and Windows).
  - **Obfuscation Bypass**: Methods to bypass code obfuscation used in software protection.
  - **Code Injection**: Injecting malicious code into running processes (DLL Injection, etc.).

- **Post-Exploitation Techniques**  
  - **Persistence Mechanisms**: Techniques to maintain access after exploiting a system.
  - **Data Exfiltration**: Methods for silently extracting sensitive data from compromised systems.
  - **Command and Control (C2) Channels**: Creating covert communication channels with compromised systems.

- **Social Engineering Frameworks**  
  - **SET (Social-Engineer Toolkit)**: A framework for automating social engineering attacks such as credential harvesting and payload delivery.

- **Red Teaming Techniques**  
  - **Active Directory Exploits**: Targeting Active Directory for privilege escalation, lateral movement, and domain control.
  - **Password Cracking**: Attacking weak passwords using dictionary and brute-force methods.
  - **Pivoting and Lateral Movement**: Gaining access to additional systems via an initial foothold in a network.

- **Cloud Exploits**  
  - **AWS Exploits**: Exploiting misconfigurations in AWS environments, such as **S3 bucket misconfigurations**, **IAM role abuse**, and **instance metadata service vulnerabilities**.
  - **Azure Exploits**: Targeting Azure environments by exploiting **misconfigured RBAC roles**, **Azure Functions misconfigurations**, and **Service Principal abuse**.
  - **Google Cloud Platform (GCP) Exploits**: Gaining unauthorized access through **misconfigured GCP IAM roles**, **Service Account Key theft**, and **Cloud Functions vulnerabilities**.
  - **Cloud Infrastructure Misconfigurations**: Exploiting **exposed cloud storage buckets**, **API key leaks**, and **public cloud instances** to gain unauthorized access.
  - **Serverless Exploits**: Targeting serverless functions (AWS Lambda, Azure Functions) for privilege escalation and unauthorized execution.
  - **Cloud Metadata Exploits**: Exploiting cloud metadata services to gain sensitive information such as API keys, tokens, or credentials.
  - **Cloud Container Exploits**: Exploiting **container misconfigurations** in Kubernetes, Docker, and other container services for unauthorized access and lateral movement.

### **Why This Repository Exists**  
The goal of this repository is to provide **continuous learning** for professionals in the field, document evolving **exploitation techniques**, and create **proof-of-concept** scripts for educational and research purposes. All exploits are **demonstrated in a controlled environment** (e.g., CTFs or vulnerable machines), following ethical hacking practices.

We strive to create a repository that is both **educational** and **cutting-edge**, ensuring that each exploit is accompanied by a detailed explanation of the underlying vulnerability, the exploitation method, and mitigations or defenses.
