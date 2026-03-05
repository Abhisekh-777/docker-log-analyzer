# 🔍 Docker Log Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## 📌 Problem Statement

Manual inspection of server logs is slow, error-prone, and 
inefficient at scale. On a busy server, hundreds of log 
entries are generated every hour — finding critical errors 
manually takes 20–25 minutes per session.

## ✅ Solution

An automated Python-based log analyzer that parses server 
logs, detects ERROR, WARNING, and CRITICAL patterns, and 
generates a clean summary report — reducing analysis time 
from 25 minutes to under 2 minutes (92% faster).

## 🏗️ Architecture
```
access.log (server logs)
       ↓
  app.py (Python parser)
       ↓
Pattern matching: ERROR | WARNING | CRITICAL
       ↓
  Summary Report Output
       ↓
Docker Container (runs on any OS)
       ↓
Crontab (scheduled execution — no human needed)
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Log parsing and pattern detection |
| Docker | Containerized execution across environments |
| Dockerfile | Custom image build for portability |
| Crontab | Scheduled automated execution |
| Linux | Host environment |

## 📁 Project Structure
```
docker-log-analyzer/
├── app.py              # Main log parser script
├── access.log          # Sample server log file
├── Dockerfile          # Container build instructions
└── requirements.txt    # Python dependencies
```

## ⚡ Performance Impact

| Metric | Before (Manual) | After (Automated) |
|---|---|---|
| Analysis time | ~25 minutes | ~2 minutes |
| Time saved | — | 92% faster |
| Human effort | Required every session | Zero — fully automated |
| Error detection | Inconsistent | 100% consistent |

## 🚀 How to Run

### Option 1 — Run with Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/Abhisekh-777/docker-log-analyzer.git
cd docker-log-analyzer

# Build the Docker image
docker build -t log-analyzer .

# Run the container
docker run --rm -v $(pwd)/access.log:/app/access.log log-analyzer
```

### Option 2 — Run locally with Python
```bash
pip install -r requirements.txt
python app.py
```

## ⏰ Automate with Crontab

Run analysis every hour automatically:
```bash
# Open crontab
crontab -e

# Add this line — runs every hour
0 * * * * docker run --rm -v /path/to/access.log:/app/access.log log-analyzer
```

## 💡 What I Learned

- Writing production-grade Python log parsers
- Building and optimizing Docker images for Python apps
- Scheduling automated tasks with Crontab
- Designing tools that work consistently across Linux and Windows
- Reducing manual DevOps overhead through automation
```

---

**Step 2 — Click ⚙️ gear → Add About description:**
```
Automated Python log analyzer containerized with Docker — 
detects ERROR/WARNING/CRITICAL patterns, 92% faster than manual inspection
```

**Step 3 — Add these topics:**
```
python  docker  linux  devops  automation  
log-analysis  crontab  monitoring  dockerfile
