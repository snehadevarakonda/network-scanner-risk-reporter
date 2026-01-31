# 🌐 Network Scanner & Risk Reporter

A Python-based cybersecurity tool that uses Nmap to scan a target system,
identify open ports and services, and generate a basic security risk report.

This project demonstrates network reconnaissance and exposure analysis,
which are essential skills for SOC and Cybersecurity Analysts.

---

## 🚀 Features
- Scans a target IP using Nmap
- Identifies open TCP ports and services
- Generates a readable security report
- Provides basic risk assessment and recommendations

---

## 🛠️ Tools & Technologies
- Python 3
- Nmap
- Linux (Kali / Ubuntu)
- Git & GitHub

---

## 📂 Project Structure
network-scanner/
├── scanner.py
├── README.md
├── .gitignore
├── reports/


---

## ⚙️ How It Works
1. The script runs an Nmap SYN scan on the target system
2. Captures scan output using Python
3. Filters open TCP ports and services
4. Writes findings into a security report
5. Adds basic risk level and mitigation suggestions

---

## ▶️ How to Run

### 1. Install Nmap (if not installed)
```bash
sudo apt install nmap -y
python3 scanner.py
cat reports/scan_report.txt


