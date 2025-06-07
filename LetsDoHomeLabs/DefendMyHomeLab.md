<h2 align="center">🛡️ Old-School Lab Setup to Defensive & Monitored Home Lab : The XDR & SIEM for My Virtual Machines🛡️</h2>

<p align="center">
  <b>Building a Home XDR & SIEM VM with Wazuh and Rocky Linux for Monitoring Offensive & Dev Operating Systems in my Virtual Home Lab</b><br>
  <i>A step-by-step guide to setting up a robust security infrastructure for your personal lab.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/focus-CyberSecurity-red?style=flat-square">
  <img src="https://img.shields.io/badge/OS-RockyLinux9%20%7C%20Kali2025.1c%20%7C%20Parrot6.3-blueviolet?style=flat-square">
  <img src="https://img.shields.io/badge/SIEM%20%26%20XDR-Active-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/status-Setup Complete-black?style=flat-square">
</p>

## 🧭 Navigation

- [📦 Introduction](#-introduction)
- [⚒️ Lab Components](#-lab-components)
- [🚀 Why Wazuh and Installation Guide](#-why-wazuh-and-installation-guide)
- [💡 Troubleshooting Tips](#-troubleshooting-tips)
- [🧠 Lessons Learned](#-lessons-learned)
- [📌 Final Thoughts](#-final-thoughts)
- [💡 Next Steps](#-next-steps)
- [📷 Gallery](#-gallery)

---
## 🚀 Introduction

In my ongoing journey of mastering cybersecurity, I transitioned from an old-school, scattered cyber lab into a centralized, having modern defensive watchtower. This blog details how I built a fully functioning **XDR (Extended Detection and Response)** and **SIEM (Security Information and Event Management)** system at home using **Wazuh** on **Rocky Linux 9**, monitoring multiple offensive and development VMs running on **VMware Workstation Pro**.

---

## 🛠️ Lab Components

Here’s what *my home virtual lab* currently includes:

<table>
  <tr>
    <td><strong>🛡️ SIEM/XDR System & Software</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Rocky_Linux_9-10B981?style=flat&logo=rockylinux&logoColor=white" title="Rocky Linux 9 (SIEM & XDR Server)" />
      <img src="https://img.shields.io/badge/Wazuh-005C96?style=flat&logo=elasticstack&logoColor=white" title="Wazuh (with Elastic Stack)" />
    </td>
  </tr>
  <tr>
    <td><strong>🖥️ Monitored VMs</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=flat&logo=kalilinux&logoColor=white" title="Kali Linux (Red Team)" />
      <img src="https://img.shields.io/badge/Parrot_OS-0085FF?style=flat&logo=linux&logoColor=white" title="Parrot OS (Offensive)" />
      <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=ubuntu&logoColor=white" title="Ubuntu (Dev Linux)" />
    </td>
  </tr>
  <tr>
    <td><strong>⛔ Excluded VM's (isolated)</strong></td>
    <td>
      <img src="https://img.shields.io/badge/REMnux-1C1C1C?style=flat&logo=linux&logoColor=white" title="REMnux (Malware Analysis - Excluded)" />
      <img src="https://img.shields.io/badge/FlareVM-181717?style=flat&logo=windows&logoColor=white" title="FlareVM (Reverse Engineering - Excluded)" />
    </td>
  </tr>
</table>

---

## 📦 Why Wazuh? and Installation Guide

Wazuh is an open-source security platform for threat detection, integrity monitoring, incident response, and compliance. It integrates everything from log analysis to vulnerability detection and integrates well with ELK stack components.


### 🧰 Installing Wazuh on Rocky Linux 9

```bash
curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh
sudo bash wazuh-install.sh -a -i
```

⚠️ *You may encounter a compatibility warning. Use the `-i` flag to ignore system check for Rocky Linux 9.*

### Ensure Firewall Ports are Open
```bash
sudo firewall-cmd --permanent --add-port=1515/tcp
sudo firewall-cmd --permanent --add-port=1514/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload
```

### 🤖 Installing Wazuh Agents

Install Wazuh agents on Kali, Parrot, and Ubuntu:
```bash
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --dearmor -o /etc/apt/keyrings/wazuh.gpg
echo "deb [signed-by=/etc/apt/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
sudo apt update
sudo apt install wazuh-agent
```

Then configure the agent to point to the manager’s IP (Rocky Linux machine):
```bash
sudo nano /var/ossec/etc/ossec.conf
# Replace MANAGER_IP with 192.168.X.XX (or your Rocky9 IP)
```

Start and enable the agent:
```bash
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

---

## 🧪 Troubleshooting Tips

### 🔁 Agent Not Connecting?
- Check NAT/Bridged Network Status in VMware
- Verify VM IPs and hostname resolutions
- Use `netstat -tulnp | grep 1514` and `1515` to ensure Wazuh is listening

### 🔥 NAT/Bridged Not Working?
Sometimes VMware networking glitches out. Reset network settings or restart `vmnetbridge` / `vmnat` services.

---

## 🧠 Lessons Learned

- NAT worked inconsistently across distros; Bridged mode failed initially for Rocky9 due to lack of network interface mapping but got resolved eventually.
- Centralized monitoring saves massive debugging effort later.
- Wazuh setup script works well even if you skip hardware checks.
- XDR+SIEM in home lab brings real-world SOC experience.

---

## 📌 Final Thoughts

This setup now serves as my central **Watchtower**—collecting logs, detecting anomalies, and giving me a bird’s eye view of every packet and log line. Whether it’s Red Teaming from Kali or coding in Ubuntu, everything is now under defensive visibility.

---

## 💡 Next Steps

- Create dashboards for visualizing alerts
- Explore Elastic, Suricata and Kibana integrations
- Start testing attack simulations using Atomic Red Team

---

## 📷 Gallery
> *My Lab Infrastructure*
![home-lab](https://github.com/user-attachments/assets/4725edfb-e25f-46c8-a159-e569cbe9ea94)

> *Leave A Message (For Fun)* 
![leaveamsg](https://github.com/user-attachments/assets/92eeb9f1-5d3a-475c-8f6a-db3967b81bdc)

> *Wazuh Agent Log In Kali*
![agent-log-in-kali](https://github.com/user-attachments/assets/87ed2b12-0fec-441b-a789-c77be5e4200e)

> *Wazuh Agent Log In Parrot*
![agent-log-in-parrot](https://github.com/user-attachments/assets/c50a4abb-f4bb-4058-ad2c-75828b1bfc3f)

> *Wazuh Agents Dashboard in Rocky9*
![WADinRocky9](https://github.com/user-attachments/assets/b2b5c118-3dd1-4fab-847a-f36edc26d157)

> *Recent MITRE ATT&CK Framework Attempts In Parrot From Rocky9*
![MitreAtt&ckInParrot](https://github.com/user-attachments/assets/01b124ed-ffc5-4597-8abb-c946fd848c0b)

> *Security Events Dashboard Of Kali In Rocky9*
![SEDofKali](https://github.com/user-attachments/assets/bb967edc-f0f0-4492-97f1-9f0bacf50ded)

> *Security Events Of Kali In Rocky9*
![SEofKali](https://github.com/user-attachments/assets/43ebac4f-addd-4f5c-be55-5b4f18c4e3dc)

---
<p align="center"> <i>“Build Defense, Before Attack” — Life Around Cybersecurity🛡️”</i> </p>
