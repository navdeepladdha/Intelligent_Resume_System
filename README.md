# Intelligent Resume System

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI](https://img.shields.io/badge/ci-pending-lightgrey.svg)](#)

> **Intelligent Resume System** — AI + heuristic resume analysis, template-based resume builder, and automated job search (LinkedIn / Naukri scraper).

---

## ✅ Project Summary

This repository contains an **Intelligent Resume System** that helps job seekers by:

* **Analyzing resumes** vs a job description using heuristics and AI (keyword matching, TF–IDF / cosine similarity, NER, LLM suggestions).
* **Building resumes** from user-provided data using predefined templates (LaTeX / HTML → PDF).
* **Searching and scraping jobs** across portals like LinkedIn and Naukri using Selenium WebDriver and automated match scoring.

It’s designed to produce ATS-friendly resumes, point out missing skills/sections, and return job listings that match the candidate profile.

---

## 🔎 Features

* Resume text extraction (PDF, DOCX, image/OCR)
* Heuristic checks (required sections, formatting, length)
* Keyword & semantic matching (TF–IDF, cosine similarity)
* Named Entity Recognition for skills, degrees, companies
* LLM-driven suggestions for missing content and rephrasing
* Template-based resume generator (LaTeX / HTML → PDF)
* Job scraper for LinkedIn, Naukri (Selenium + WebDriver)
* Job–Resume matching and scoring
* Exportable resume, suggestions report, and job list

---

## 📁 Repo Structure (suggested)

```
/ (root)
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ .env.example
├─ /backend
│  ├─ app.py (FastAPI/Flask entry)
│  ├─ resume_analysis/
│  │  ├─ extractor.py
│  │  ├─ nlp.py
│  │  └─ scorer.py
│  ├─ resume_builder/
│  │  └─ templates/
│  └─ job_scraper/
│     ├─ linkedin_scraper.py
│     └─ naukri_scraper.py
├─ /frontend
│  └─ react-app/
├─ /templates
│  ├─ latex/
│  └─ html/
└─ tests/
```

---

## 🛠️ Technologies

* Python 3.10+
* FastAPI / Flask
* React (optional) for frontend
* Selenium WebDriver (Chromedriver/Geckodriver)
* pdfplumber / PyPDF2 / python-docx
* spaCy / NLTK / Scikit-learn (TF–IDF, cosine similarity)
* OpenAI / other LLM API (optional)
* LaTeX (`pdflatex`) or `WeasyPrint` / `pdfkit`
* MongoDB / PostgreSQL / SQLite (as needed)

---

## ⚙️ Installation

> This guide assumes a UNIX-like environment. Adjust commands for Windows.

1. Clone the repo

```bash
git clone https://github.com/<your-username>/intelligent-resume-system.git
cd intelligent-resume-system
```

2. Create virtual environment & install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Create `.env` from example and fill required keys

```
cp .env.example .env
# edit .env to include API keys, DB URL, driver paths
```

4. Download the appropriate webdriver (ChromeDriver or geckodriver) and put it in `PATH` or point to it in `.env`.

---

## ⚙️ Environment Variables (.env.example)

```ini
# Backend
PORT=8000
ENV=development

# Database
DB_URL=mongodb://localhost:27017/resume_system

# WebDriver
WEBDRIVER_PATH=/usr/local/bin/chromedriver

# LLM / API Keys (optional)
OPENAI_API_KEY=

# Scraping settings
SCRAPER_USER_AGENT=Mozilla/5.0 (X11; Linux x86_64) ...
SCRAPER_MAX_PAGES=5
```

---

## 🚀 How to run (development)

### Backend (FastAPI example)

```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port ${PORT:-8000}
```

### Frontend (React example)

```bash
cd frontend/react-app
npm install
npm start
```

---

## 🔍 Usage Examples

### 1) Analyze a resume against a job description

**Endpoint:** `POST /analyze`
**Payload:**

```json
{
  "resume_file": "<multipart file>",
  "job_description": "<text or file>",
  "options": {"use_llm": true}
}
```

**Response:** JSON report with:

* overall match score
* missing skills
* formatting suggestions
* suggested bullet points

### 2) Build a resume from form data

**Endpoint:** `POST /build`
**Payload:**

```json
{
  "profile": {"name":"...","email":"...", "education": [...], "experience": [...]},
  "template": "modern-1",
  "output_format": "pdf"
}
```

### 3) Scrape jobs for a candidate

**Endpoint:** `POST /scrape`
**Payload:**

```json
{
  "query": "Software Engineer",
  "location": "Bangalore",
  "max_pages": 3
}
```

**Response:** list of jobs with title, company, skills, link and a match score

---

## 🧩 Design decisions & rationale

* **TF–IDF + cosine similarity** for fast, interpretable resume ↔ job scoring.
* **NER** to reliably extract entities like skills, years, organizations.
* **LLM (optional)** to produce higher-quality rewrite suggestions and custom bullet points.
* **Selenium** for job sites without a public API (LinkedIn/Naukri). Use with respect to site terms of service.
* **Templates (LaTeX / HTML)** give deterministic, ATS-friendly output.

---

## ⚠️ Legal & Ethical Considerations

* Scraping websites may violate terms of service. Use responsibly and respect rate limits.
* Do not store or share personal data without consent. Follow privacy rules applicable to your jurisdiction.
* Implement protections to avoid account lockouts or IP bans (random waits, rotate UA, respect robots.txt).

---

## 🐞 Common Issues & Troubleshooting

* **Selenium fails with login protected pages:** use cookie-based sessions or authenticated API access (if available).
* **Dynamic selectors break:** use robust XPaths or CSS selectors and fallback strategies.
* **Poor match scores:** tune TF–IDF vectorizer parameters or add synonym expansion and skill synonyms mapping.
* **LLM costs:** use LLM sparingly; cache suggestions where possible.

---

## ✅ Testing

Add unit tests for:

* resume text extraction (PDF/DOCX/ocr)
* keyword extraction & NER
* TF–IDF similarity scoring
* resume builder output matches (snapshot test)

Run tests:

```bash
pytest tests/
```

---

## 🧭 Deployment (short)

* Use Docker to containerize backend & a separate frontend build.
* Use a job queue (Celery/RQ) for long tasks: scraping, PDF build, LLM calls.
* Deploy on any cloud provider (DigitalOcean, AWS, GCP) and use managed DB.

**Example Docker-compose (simplified)**

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports: ['8000:8000']
    env_file: .env
  frontend:
    build: ./frontend/react-app
    ports: ['3000:3000']
```

---

## ♻️ Future Work

* Integrate OAuth and apply-on-behalf (email automation)
* Add a scheduling & application tracker dashboard
* Add more portals & more robust anti-bot handling
* Improve LLM-driven tailored resume generation

---

## 🤝 Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feat/my-feature`
3. Commit changes: `git commit -m "feat: add ..."`
4. Push: `git push origin feat/my-feature`
5. Open a PR

Please adhere to coding style and add tests for new features.

---

## 📄 License

This project is released under the **MIT License** — see `LICENSE` for details.

---

## 📫 Contact

Created by **Your Name** — replace with your name and links.

* Email: `navdeepladdha75@gmail.com`
* LinkedIn: `https://www.linkedin.com/in/navdeep-laddha-038704249/`
* GitHub: `https://github.com/navdeepladdha`

---


> * create a `README` that includes demo GIFs / screenshot placeholders
> * produce a `CONTRIBUTING.md`, `ISSUE_TEMPLATE.md`, and sample `WORKFLOW` for CI
