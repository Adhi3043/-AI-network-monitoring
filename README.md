# 🚀 AI-Powered Real-Time Network Behavior Monitoring System

This project is an intelligent, automated network monitoring tool that scans devices in a local network, detects open ports, and provides real-time visual insights using bar and pie charts. It's ideal for identifying active hosts and potential security risks.

---

## 🔧 Features

* ✅ Real-time network scanning using `nmap`
* 📊 Bar and Pie chart visualizations with `matplotlib` and `seaborn`
* 🔍 Detection of open TCP ports (1-1024)
* 📑 JSON + TXT reporting of scan results
* ⏰ Periodic scans with configurable intervals
* 📤 Automatically saves results and visual output

---

## 📚 Technologies Used

* Python 3.10+
* Nmap + python-nmap
* Matplotlib, Seaborn
* Pandas, NumPy
* Scapy (optional future use)

---

## 📂 Project Structure

```
network-monitoring-project/
├── env310/                    # Virtual environment (excluded in .gitignore)
├── network-monitoring-project/
│   ├── src/
│   │   └── main.py            # Main scanner and visualizer
│   ├── reports/              # Auto-generated scan reports
│   │   ├── scan_report.json
│   │   ├── scan_report.txt
│   │   ├── scan_bar_chart.png
│   │   └── scan_pie_chart.png
│   └── README.md
├── .gitignore
└── requirements.txt (optional)
```

---

## 🚀 How to Run

```bash
# Step 1: Clone the repo
https://github.com/Adhi3043/-AI-network-monitoring.git
cd AI-network-monitoring

# Step 2: Create and activate a virtual environment (if not already)
python3 -m venv env310
source env310/bin/activate

# Step 3: Install dependencies
pip install --break-system-packages -r requirements.txt

# Step 4: Run the project
sudo python network-monitoring-project/src/main.py
```

> **Note:** `sudo` is required for nmap to run SYN scans

---

## 📊 Sample Output

Scan report saved in:

* `reports/scan_report.txt`
* `reports/scan_report.json`

Visual charts generated in:

* `reports/scan_bar_chart.png`
* `reports/scan_pie_chart.png`

---

## 📈 Future Improvements

* Add threat scoring for hosts with critical ports
* Integrate alert system (Slack/email)
* Enable scanning for UDP services
* Web dashboard using Flask

---

## 👤 Author

**Jhansi Aditya Akula**
Cybersecurity Enthusiast | Python Developer | Network Security Learner

GitHub: [Adhi3043](https://github.com/Adhi3043)

---

> If you liked this project, feel free to give it a ⭐ and connect with me!
