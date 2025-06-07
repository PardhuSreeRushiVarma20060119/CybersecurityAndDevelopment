<h1 align="center">🛡️ Legacy to Watchtower - Home XDR & SIEM for My Home Lab 🛡️</h1>

<p align="center">
  <b>Building a Home XDR & SIEM VM with Wazuh and Rocky Linux for Offensive & Dev Operating Systems in my Virtual Home Lab</b><br>
  <i>A step-by-step guide to setting up a robust security infrastructure for your personal lab.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/focus-CyberSecurity-red?style=flat-square">
  <img src="https://img.shields.io/badge/OS-RockyLinux%209-blueviolet?style=flat-square">
  <img src="https://img.shields.io/badge/SIEM%20%26%20XDR-Active-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/status-Setup Complete-black?style=flat-square">
</p>

## 🚀 Introduction

In my ongoing journey of mastering cybersecurity, I transitioned from an old-school, scattered cyber lab into a centralized, modern defensive watchtower. This blog details how I built a fully functioning **XDR (Extended Detection and Response)** and **SIEM (Security Information and Event Management)** system at home using **Wazuh** on **Rocky Linux 9**, monitoring multiple offensive and development VMs running on **VMware Workstation Pro**.

---

## 🛠️ Lab Components

Here’s what my home virtual lab currently includes:

- **SIEM/XDR Server**: Rocky Linux 9 + Wazuh
- **Monitored VMs**:
  - Kali Linux (Red Team)
  - Parrot OS (Offensive)
  - Ubuntu (General Linux)
  - REMnux (Malware Analysis) *(excluded for now)*
  - FlareVM (Reverse Engineering) *(excluded for now)*

---

## 📦 Why Wazuh?

Wazuh is an open-source security platform for threat detection, integrity monitoring, incident response, and compliance. It integrates everything from log analysis to vulnerability detection and integrates well with ELK stack components.

---

## 🧰 Installing Wazuh on Rocky Linux 9

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

---

## 🤖 Installing Wazuh Agents

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
# Replace MANAGER_IP with 192.168.1.104 (or your Rocky9 IP)
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

- Add REMnux and FlareVM with limited access
- Create dashboards for visualizing alerts
- Explore Elastic and Kibana integrations
- Start testing attack simulations using Atomic Red Team

---

## 📷 Gallery (Add Screenshots)
*(Add screenshots of dashboard, VM structure, Wazuh UI here)*

---

**Stay sharp, stay secure. 🛡️**