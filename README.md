# NoCode-bench-ATSE-TUM
An AI agent that generates code patches from documentation changes. Project for "Advanced Topics in Software Engineering" at TUM.

# NoCode-Agent Setup Guide (Steps 1–2)

This guide summarizes the essential steps required to set up the project environment for **NoCode-Agent**, including project structure, environment setup, dependencies, Docker configuration, and dataset preparation.

---

## ✅ Step 1 — Initialize Project & Environment

### **1.1 Clone NoCode-bench Core**

Clone the official benchmark repository into a dedicated folder so your own backend/frontend remain clean:

```bash
git clone https://github.com/NoCode-bench/NoCode-bench.git bench_core
```

Folder layout after this step:

```
nocode-agent/
├── backend/
├── bench_core/   # NoCode-bench source code
├── frontend/
└── .git/
```

### **1.2 Create Conda Environment (Python 3.12)**

The benchmark requires Python **3.12**, so create and activate the environment:

```bash
conda create -n ncb python=3.12 -y
conda activate ncb
```

> **Important:** Always activate this environment before running backend or benchmark scripts.

### **1.3 Install Required Libraries**

#### A) **Install dependencies for NoCode-bench core**

```bash
cd bench_core
pip install -r requirements.txt
cd ..
```

#### B) **Install backend dependencies**

Create `backend/requirements.txt` containing:

```
fastapi
uvicorn
python-multipart
datasets
docker
openai
requests
```

Then install:

```bash
pip install -r backend/requirements.txt
```

---

## ✅ Step 2 — Prepare Docker & Datasets

### **2.1 Install Docker Desktop**

Make sure Docker Desktop is installed and running:

* Windows/macOS: Install Docker Desktop
* Linux: Install Docker Engine + Docker Compose plugin

Verify installation:

```bash
docker --version
docker compose version
```

### **2.2 Pull Required Docker Images**

Move into the environment directory inside the benchmark core:

```bash
cd bench_core/environment
```

Pull repository-level images using the provided script:

```bash
bash ./pull_from_hub.sh
```

This downloads all base Docker images required for running the benchmark tasks.

### **2.3 Verify Dataset Availability**

Use the built‑in script to check whether datasets are correctly downloaded:

```bash
python check_data.py
```

If any dataset is missing, the script will notify you and provide hints for fixing the issue.
