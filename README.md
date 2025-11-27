🚀 SafePipe
Secret Leak Detection & Alerting System for CI/CD Pipelines

SafePipe is an intelligent, real-time secret leak detection system designed to prevent API keys, credentials, and sensitive tokens from leaking into code repositories or CI/CD pipelines.
It integrates seamlessly with modern DevOps workflows and provides instant alerts, reports, and dashboards to help engineering teams maintain security hygiene.

📚 Table of Contents — SafePipe

Features

Project Structure

Setup Instructions

Usage

Screenshots

Contributing

License

🚀 Features

Real-time secret leak detection using regex + entropy scanning

CI/CD integration for GitHub Actions, GitLab, Jenkins & Bitbucket

Interactive dashboard to view, filter, and analyze detected secrets

Instant alerts via Email/Slack with severity insights

Exportable reports in PDF, CSV, and JSON formats

AI-assisted summaries and risk analysis (upcoming)

🏗️ Project Structure

safepipe/
│
├── backend/
│   ├── api/                # FastAPI routes
│   ├── scanner/            # Secret scanning engine
│   ├── models/             # Database models (PostgreSQL/SQLite)
│   ├── utils/              # Helper functions
│   └── main.py             # Backend entry point
│
├── dashboard/
│   ├── components/         # Reusable UI components
│   ├── pages/              # Dashboard views
│   ├── services/           # API calls
│   └── App.jsx             # Frontend entry point
│
├── config/                 # Alerts, environment configs
├── docs/                   # Documentation & assets
├── .github/workflows/      # CI/CD workflow files
│
└── README.md               # Project documentation

⚙️ Setup Instructions

Clone the repository

git clone https://github.com/yourusername/safepipe.git
cd safepipe


Backend setup

cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Dashboard setup

cd dashboard
npm install
npm run dev


Configure environment variables
Update values in config/ (API keys, alert settings, DB connection).

▶️ Usage

Run the backend and dashboard.

Upload or select a repository to scan.

SafePipe automatically scans for leaked secrets.

View detected issues on the dashboard with severity labels.

Export results as PDF/CSV/JSON.

Integrate with CI/CD to block unsafe commits.

🖼️ Screenshots

(Add your images like this)

![Dashboard Overview](docs/screenshots/dashboard.png)
![Scan Report](docs/screenshots/report.png)

🤝 Contributing

Contributions are welcome!
To contribute:

Fork the repository

Create a feature branch

Commit your changes

Open a pull request

Please ensure code is clean and documented.

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute the project with attribution.
