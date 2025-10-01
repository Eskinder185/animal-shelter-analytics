
# Grazioso Salvare Dashboard

![Built with](https://img.shields.io/badge/Built%20with-Python%203.10%2B%20%7C%20Dash%20%7C%20Plotly-blue)
![Database](https://img.shields.io/badge/Database-MongoDB-47a248)
![Style](https://img.shields.io/badge/Code-Clean%20%26%20Modular-5b5)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A user-friendly dashboard for **Grazioso Salvare** to explore the **Austin Animal Center Outcomes** dataset.  
Interactive filters, dynamic visualizations, and a **geo map** help turn raw data into actionable insights.

> This project demonstrates a clean **CRUD module** (from Project One) integrated with a full **Dash** app (Project Two), backed by **MongoDB**.

[✨ Features](#-features) · [🚀 Quick Start](#-quick-start) · [⚙️ Config](#-configuration) · [🧱 Architecture](#-architecture) · [🗂 Structure](#-project-structure) · [🧪 Tests](#-tests) · [❓FAQ](#-faq)

---

## ✨ Features

- **Interactive filters** (species, age, outcome type, date range, location)
- **Dynamic charts** (bar/line/pie KPIs: intakes vs outcomes, outcomes by type, breed trends)
- **Geolocation map** (Plotly map of outcome locations)
- **Clean CRUD module** (`create`, `read`, `update`, `delete`) reused by the dashboard
- **Responsive layout** (works on laptop and tablet)
- **Export** (filtered results to CSV)

---

## 🚀 Quick Start

### Requirements
- Python **3.10+**
- MongoDB (Atlas or local)

### 1) Clone & install
```bash
git clone https://github.com/YOUR_USER/grazioso-salvare-dashboard.git
cd grazioso-salvare-dashboard
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
2) Configure environment
