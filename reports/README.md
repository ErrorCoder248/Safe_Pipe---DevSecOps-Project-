# SafePipe – Secret Leak Detection Tool

SafePipe is a Python-based tool that detects sensitive information like API keys, passwords, tokens, and private keys. It has:

1. **Streamlit Dashboard** – Visual metrics, color-coded severity, downloadable JSON reports.
2. **Headless Scanner** – Can be integrated into CI/CD pipelines (Azure DevOps, etc.).
3. **Reusable Core Logic** – Shared scanning engine for both dashboard and pipeline.
4. Successfully Deployed in Render  

## Folder Structure

- `app.py` – Dashboard interface
- `safe_pipe_core.py` – Core scanning logic
- `run_safe_pipe.py` – Headless scanner for pipelines
- `test_secrets.txt` – Demo file for dashboard
- `dummy_keys/` – Folder for pipeline testing
- `reports/` – Output JSON reports
- `requirements.txt` – Python dependencies
- `README.md` – Project documentation
  
