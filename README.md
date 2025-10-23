# 🧪 Flask Lab Project — Collaborative CI/CD & Docker Setup

### 🎯 Objective  
A collaborative Flask web application demonstrating **Docker containerization** and **Continuous Integration/Continuous Deployment (CI/CD)** using **GitHub Actions**.

---

## 👥 Team Members & Roles

| Member | Role | Responsibilities |
|--------|------|------------------|
| **Member 1** | 🧩 Backend Lead | Implemented core Flask routes and application logic (`/`, `/health`, `/data` endpoints) |
| **Member 2** | 🎨 Frontend / API Integration | Built HTML templates, static files, and integrated frontend with backend APIs |
| **Member 3 (You)** | ⚙️ DevOps Engineer | Created Docker configuration, wrote automated tests, and set up CI/CD pipeline using GitHub Actions |

---

## 🏗️ Project Structure

```
flask_lab_project/
│
├── main/
│   ├── app.py                # Main Flask application
│   ├── requirements.txt      # Dependencies list
│   ├── Dockerfile            # Docker configuration
│   ├── tests/
│   │   └── test_app.py       # Unit tests for app routes
│   └── .github/
│       └── workflows/
│           └── ci-cd.yml     # GitHub Actions pipeline
│
├── member1_backend/          # Backend work area
├── member2_frontend/         # Frontend work area
└── member3_devops/           # DevOps work area
```

---

## ⚙️ How to Build, Test, and Run the Project

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/<your-team-name>/flask-lab-project.git
cd flask-lab-project/main
```

---

### 🔹 2. Install Dependencies (Local Environment)

Make sure you have **Python 3.10+** installed.

```bash
pip install -r requirements.txt
```

Run the Flask app:
```bash
python app.py
```

Now open your browser and visit:  
👉 [http://localhost:5000](http://localhost:5000)

---

### 🔹 3. Run Unit Tests

Run tests using `pytest`:
```bash
pytest tests/test_app.py
```

✅ **Expected Output**
```
================== test session starts ==================
collected 2 items

tests/test_app.py ..                                                             [100%]
================== 2 passed in 0.35s ===================
```

---

### 🔹 4. Run with Docker 🐳

#### Build Docker Image
```bash
docker build -t flask-lab .
```

#### Run Docker Container
```bash
docker run -p 5000:5000 flask-lab
```

Then visit:  
👉 [http://localhost:5000](http://localhost:5000)

---

## 🔄 Continuous Integration / Continuous Deployment (CI/CD)

Our **GitHub Actions pipeline** is located at:

```
main/.github/workflows/ci-cd.yml
```

### 🚀 Workflow Summary
1. Triggered automatically on every **push or PR to `main`**  
2. **Checks out** the repository  
3. **Installs dependencies**  
4. **Runs automated tests** using `pytest`  
5. **Builds Docker image**  
6. *(Optional)* Pushes Docker image to Docker Hub  

You can view pipeline runs under the **Actions** tab on GitHub.

---

## 🧾 Deliverables

- ✅ **GitHub Repository Link**  
- ✅ **Screenshot of Successful CI/CD Pipeline Run**  
- ✅ **Screenshot of App Running via Docker**  
- ✅ **README.md (This File)** — includes roles, setup, and execution guide

---

## 💬 Summary

This project showcases:
- Team collaboration with Git branches & pull requests  
- Backend–Frontend integration in Flask  
- Docker containerization for consistent deployment  
- CI/CD automation through GitHub Actions  

It represents a complete **DevOps workflow** — from development to automated deployment. 🚀

---

**Created by:**  
👩‍💻 *Team Flask Lab Project (Backend, Frontend, and DevOps Collaboration)*
