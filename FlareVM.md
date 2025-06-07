# FLARE VM

![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)
![License](https://img.shields.io/github/license/fireeye/flare-vm)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen)

**FLARE VM** is a freely available and open-source Windows-based security distribution designed for:
<p align="center">
  - Reverse engineers  
  - Malware analysts  
  - Incident responders  
  - Cyber Forensic Investigators  
  - Penetration testers
</p>

Inspired by Linux-based distributions like **Kali Linux** and **REMnux**, FLARE VM offers a **fully-configured platform** with a wide set of **Windows-native security tools**, including:

<p align="center">
  - Debuggers, disassemblers, and decompilers  
  - Static & dynamic analysis utilities  
  - Network traffic analysis tools 
</p>
 <p align="center">
  - Web assessment, exploitation, and vulnerability scanners  
  - Tools developed by the FLARE team such as <strong>FLOSS</strong> and <strong>FakeNet-NG</strong>
</p>


---

## 🔧 How to Get It

You’ll need a **Windows 7 or later** system (preferably a **virtual machine**).

> ⚠️ **Important:** You must use **Internet Explorer** to initiate the install (other browsers won't work).

1. Open **Internet Explorer** and visit:  https://github.com/mandiant/flare-vm/blob/main/install.ps1

2. A Boxstarter WebLauncher dialog appears.  
Click **Run**.

3. After the initial installer opens, you’ll be prompted for your **Windows password** (used for reboots).

4. Sit back! The installation takes **30–40 minutes** depending on connection speed and system resources. Your system will **reboot multiple times**.

---

## ⚙️ Post-Installation Tips

- **Switch to Host-Only networking mode** to isolate malware samples.
- **Take a fresh VM snapshot** to save the clean FLARE VM state.

Final installation should resemble this:

![FLARE VM Desktop](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro3_diot.max-1200x1200.png)

---

## 🚀 Getting Started

The FLARE team has curated and built the VM for over a decade to aid malware RE. Tools are organized in a clear directory structure:

![FLARE VM Tools](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro4_mgqa.max-1200x1200.png)

Most tools are in the **FLARE Start Menu folder** or can be run from **CLI**. For documentation, visit:  
👉 [http://flarevm.info](http://flarevm.info)

---

## 🔬 Sample Malware Analysis

### Example: Using FLOSS

1. Run **FLOSS** (FLARE’s enhanced strings utility) on a sample:

![FLOSS](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro5_ystg.max-700x700.png)

2. Strings are extracted, though sometimes unclear:

![Strings Output](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro6_sdvt.max-1000x1000.png)

---

### Example: PE Analysis with CFF Explorer

- Inspect **resources**, **imports**, and **headers**:

![CFF Explorer](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro7_txyj.max-1200x1200.png)

- Embedded payloads may be encrypted:

![Encrypted Payload](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro8_tckq.max-1200x1200.png)

---

### Dynamic Analysis with FakeNet-NG + Procmon

- Launch **FakeNet-NG** to emulate network services.
- Run **Procmon** to observe file, registry, and API activity.

![Dynamic Tools](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro9_kfkc.max-1200x1200.png)

- FakeNet-NG captures malware HTTP calls:

![FakeNet](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro10_njyw.max-1200x1200.png)

- Confirm system-level changes via Procmon:

![Procmon](https://storage.googleapis.com/gweb-cloudblog-publish/images/flare-vm-intro11_mysk.max-1200x1200.png)

---

## 🧰 Power Tools Included

Some of the high-value tools in FLARE VM:

- FLOSS
- FakeNet-NG
- IDA Freeware & Binary Ninja (community version)
- CFF Explorer
- x64dbg, OllyDbg
- Sysinternals Suite
- Wireshark, Fiddler
- Python, .NET, PowerShell toolkits
- Disassembly and PE header viewers
- YARA, PEStudio, Pestudio, CAPA

---

## 🧱 Customization with Chocolatey
FLARE VM is powered by [Chocolatey](https://chocolatey.org/) — the Windows package manager.
To install a new tool (e.g., Firefox), just run:

```powershell
> choco install firefox
```
🔄 Staying Up to Date
Keep all tools updated by running:

```powershell
 cinst flare-vm -y
```
> ✅ Don’t forget to snapshot your VM after updates and reset networking to Host-Only.

### 📣 Conclusion
FLARE VM is a trusted, free, and powerful RE platform. Whether you're performing static or dynamic analysis, it offers a complete toolkit to assist your workflow.
Next time you set up a malware analysis lab — try FLARE VM.

📬 Feedback & Issues
GitHub: https://github.com/fireeye/flare-vm
Website: http://flarevm.info
