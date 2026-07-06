# 📧 Email Automation Project

## 📌 Overview
This project shows how to **automate email sending with Python**.  
It connects to Gmail securely using an **App Password**, creates an email with subject, body, and optional attachments, and can send to multiple recipients.  
The script also supports **scheduling**, so reports or updates can be delivered automatically at a fixed time every day.

---

## 🎯 Features
- **Send Emails** → Automated delivery via Gmail SMTP.  
- **Attachments** → Add PDF, Excel, or other files.  
- **Multiple Recipients** → Send to a list of people.  
- **Scheduling** → Automate daily reports at a chosen time.  
- **Logging** → Track when emails were sent.  

---

## 🛠️ Tech Stack
- **Python 3**  
- Libraries: `smtplib`, `email.mime`, `schedule`, `datetime`  
- Gmail SMTP with **App Passwords** for secure login  

---

## 📂 Project Structure
EmailAutomationProject/
│
├── email_automation.py   # Main script
├── report.pdf            # Sample attachment
├── recipients.csv        # (Optional) List of recipients
└── README.md             # Project documentation

## Use Cases 
Daily Sales Reports → Auto‑send Excel/PDF reports to managers.

Meeting Reminders → Notify team members before meetings.

Client Updates → Send bulk updates to multiple clients.
