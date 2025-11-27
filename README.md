
---

# **SafePipe**

A powerful and developer-friendly **secret leak detection system** designed to help teams identify exposed API keys, tokens, credentials, and sensitive data across repositories and CI/CD pipelines.
Built with **FastAPI**, **React**, and **Python-based scanners**, SafePipe ensures secure software development through automated scanning, alerting, and reporting.

---

# **Table of Contents**

* **Features**
* **Project Structure**
* **Setup Instructions**
* **Usage**
* **Screenshots**
* **Contributing**
* **License**

---

# **Features**

* 🔍 **High-accuracy secret detection** (regex + entropy)
* ⚡ **CI/CD integration** (GitHub Actions, GitLab, Jenkins, Bitbucket)
* 🖥️ **Modern React Dashboard** to view scan results
* 🚨 **Instant alerts** via Email/Slack with recommended remediation
* 📄 **Exportable reports** (PDF, CSV, JSON)
* 🤖 **AI-based summaries & risk scoring** (upcoming)
* 🔐 Supports detection of:

  * API keys
  * Access tokens
  * OAuth secrets
  * JWTs
  * Passwords
  * Cloud keys (AWS, GCP, Azure)
  * Database credentials
* 🌐 Works across multiple programming languages & file types

---

# **Project Structure**

```
safepipe/
├── backend/                        # FastAPI backend
│   ├── main.py                     # Entry point
│   ├── api/                        # API routes
│   ├── scanner/                    # Secret detection engine
│   ├── models/                     # Database models
│   ├── utils/                      # Helper functions
│   └── config/                     # Email, Slack, DB config
│
├── dashboard/                      # React frontend
│   ├── components/                 # Reusable UI components
│   ├── pages/                      # Dashboard pages
│   ├── services/                   # API communication
│   └── App.jsx                     # Frontend entry point
│
├── docs/                           # Documentation & screenshots
├── scripts/                        # CI/CD scripts
├── .github/workflows/              # GitHub Actions workflows
└── README.md
```

---

# **Setup Instructions**

### **1. Clone the repository**

```bash
git clone <your-repo-url>
cd safepipe
```

---

## **Backend Setup (FastAPI)**

### **2. Create & activate virtual environment**

```bash
python -m venv venv
venv/Scripts/activate   # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### **3. Install dependencies**

```bash
pip install -r backend/requirements.txt
```

### **4. Configure environment**

Update values in `backend/config/settings.py`:

* Database credentials
* Email alert settings
* Slack webhook
* JWT secret

### **5. Run backend**

```bash
cd backend
uvicorn main:app --reload
```

---

## **Frontend Setup (React Dashboard)**

### **6. Install dependencies**

```bash
cd dashboard
npm install
```

### **7. Start development server**

```bash
npm run dev
```

### **8. Access the dashboard**

Open:
👉 [http://localhost:5173/](http://localhost:5173/)

Backend API:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

# **Usage**

* Start **backend** and **dashboard**.
* Upload or link a repository for scanning.
* SafePipe detects secrets automatically in files, commits, and branches.
* View results with severity levels on the dashboard.
* Export reports as PDF/CSV/JSON.
* Configure Email/Slack alerts for real-time notifications.
* Integrate SafePipe with CI/CD pipelines to block insecure deployments.

---

# **Screenshots**

(Add screenshots in the `docs/screenshots/` folder)

```
![Dashboard Overview](docs/screenshots/dashboard.png)
![Scan Results](docs/screenshots/scan_results.png)
![Alerts](docs/screenshots/alerts.png)
```

---

# **Contributing**

Pull requests are welcome!

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

For major changes, please open an issue to discuss them first.

---

If you want, I can compile this into a **ready-to-upload README.md** with formatting, badges, and styling.
