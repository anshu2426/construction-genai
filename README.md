# 🏗️ Construction Content Generator

An AI-powered construction site report generator built using Streamlit and modern DevOps practices. This system leverages LLMs and vector search to generate professional, structured construction reports efficiently.

---

## 📌 Project Overview

The **Construction Content Generator** is a smart AI application designed to automate construction report creation. It integrates **LLM-based content generation** with **vector-based document retrieval** to produce accurate and context-aware reports.

The system is containerized using Docker and supports both:
- Local development
- Production deployment via CI/CD pipelines

---

## 🚀 Key Features

- 🧠 AI-powered report generation using Google Gemini
- 📄 Professional PDF report generation
- 🔍 Vector-based document search (TF-IDF)
- 🌐 Modern and responsive UI with Streamlit
- 🐳 Dockerized application for consistent environments
- ⚙️ CI/CD pipeline for automated deployment
- ☁️ Supports deployment on AWS EC2 and Kubernetes (Minikube)

---

---

## 🛠️ Tech Stack

| Category            | Technology |
|--------------------|-----------|
| Frontend           | Streamlit |
| AI/LLM             | Google Gemini (`google-genai`) |
| Vector Search      | scikit-learn (TF-IDF) |
| PDF Generation     | fpdf |
| Containerization   | Docker |
| Orchestration      | Kubernetes (Minikube) |
| CI/CD              | GitHub Actions |
| Cloud Deployment   | AWS EC2 |

---

---

## 📂 Project Structure

    .
    ├── .github/
    │   └── workflows/
    │       └── deploy.yml          # CI/CD pipeline for EC2 deployment
    │
    ├── k8s/                        # Kubernetes manifests
    │   ├── deployment.yaml         # Defines pods, replicas, and rolling updates
    │   ├── service.yaml            # Exposes application (ClusterIP / NodePort / LoadBalancer)
    │   └── secret.yaml             # Stores sensitive data like API keys (not committed)
    │
    ├── construction_genai/         # Core application source code
    │   ├── app.py                  # Main Streamlit application (entry point)
    │   ├── llm_engine.py           # Handles LLM (Google Gemini) integration
    │   ├── vector_db.py            # Implements vector search (TF-IDF)
    │   ├── prompts.py              # Prompt templates for AI generation
    │   └── data/                   # Knowledge base documents
    │
    ├── Dockerfile                  # Docker image build instructions
    ├── docker-compose.yml          # Local multi-container setup
    ├── requirements.txt            # Python dependencies
    │
    ├── .dockerignore               # Files excluded from Docker build
    ├── .gitignore                  # Files ignored by Git
    │
    ├── README.md                   # Project documentation
    ├── DEPLOYMENT.md               # AWS EC2 deployment guide
    └── MINIKUBE_SETUP.md           # Kubernetes (Minikube) setup guide

---

### 📖 Structure Explanation

- **.github/workflows/**  
  Contains CI/CD pipeline configuration.  
  `deploy.yml` automates the process of building, pushing, and deploying the application.

- **k8s/**  
  Kubernetes configuration files for container orchestration:
  - `deployment.yaml` → Defines pods, replicas, and rolling updates  
  - `service.yaml` → Exposes the application to users  
  - `secret.yaml` → Stores sensitive data like API keys securely  

- **construction_genai/**  
  Core application logic:
  - `app.py` → Main Streamlit UI (entry point)  
  - `llm_engine.py` → Handles interaction with LLM (Google Gemini)  
  - `vector_db.py` → Implements document retrieval using TF-IDF  
  - `prompts.py` → Stores prompt templates  
  - `data/` → Knowledge base for contextual responses  

- **Dockerfile**  
  Defines how the application is containerized into a Docker image.

- **docker-compose.yml**  
  Helps run the application locally using containers.

- **requirements.txt**  
  Lists all Python dependencies required to run the project.

- **.dockerignore & .gitignore**  
  Prevent unnecessary or sensitive files from being included in builds or version control.

- **Documentation Files**  
  - `README.md` → Project overview and usage  
  - `DEPLOYMENT.md` → AWS EC2 deployment steps  
  - `MINIKUBE_SETUP.md` → Local Kubernetes setup  

---

## 🧠 How It Works

1. User inputs construction-related requirements  
2. The system processes input using predefined prompts  
3. Vector database retrieves relevant documents  
4. LLM generates structured construction content  
5. Output is displayed via Streamlit UI and can be exported as PDF  

---

## ⚙️ Setup & Execution Steps

### 🔹 Local Development

#### Step 1: Clone the Repository  
`git clone <your-repo-url>`  
`cd construction-content-generator`

#### Step 2: Install Dependencies  
`pip install -r requirements.txt`

#### Step 3: Run the Application  
`streamlit run construction_genai/app.py`

---

### 🐳 Docker Setup

#### Step 1: (Optional) Set Docker Host  
`export DOCKER_HOST=unix:///home/anshul/.docker/desktop/docker.sock`

#### Step 2: Build & Start Containers  
`docker-compose up -d`

#### Step 3: View Logs  
`docker-compose logs -f`

#### Step 4: Stop Containers  
`docker-compose down`

---

### 🚀 Deployment (AWS EC2 - CI/CD)

#### Step 1: Push Code to GitHub  
`git add .`  
`git commit -m "Deploy application"`  
`git push origin main`

#### Step 2: CI/CD Pipeline Execution  

Pipeline Flow:  
`Git Push → GitHub Actions → Build Docker Image → Push to Docker Hub → Deploy to EC2`

#### Step 3: Verify Deployment  
- Check running containers on EC2  
- Access application using EC2 Public IP  

---

### ⚙️ Kubernetes (Minikube)

#### Step 1: Start Minikube  
`minikube start`

#### Step 2: Apply Kubernetes Configurations  
`kubectl apply -f k8s/deployment.yaml`  
`kubectl apply -f k8s/service.yaml`

#### Step 3: Verify Resources  
`kubectl get pods`  
`kubectl get services`

#### Step 4: Access Application  
`minikube service <service-name>`

---

## 🔄 CI/CD Pipeline (Detailed Stages)

1. **Checkout Code**  
   Pull latest code from repository  

2. **Build Docker Image**  
   Build container image using Dockerfile  

3. **Docker Authentication**  
   Login to Docker Hub using credentials  

4. **Push Docker Image**  
   Push image to Docker Hub repository  

5. **Deployment to EC2**  
   Pull latest image and run container on server  

6. **Verification**  
   Ensure application is live and accessible  

---

## 📦 Scalability & Architecture

- Stateless containerized application  
- Easily deployable across multiple environments  
- Supports horizontal scaling using Kubernetes  
- Modular design (LLM + Vector DB separation)  

---

## 📈 Future Enhancements

- 🔹 Integrate advanced vector databases (FAISS / Pinecone)  
- 🔹 Add user authentication & role-based access  
- 🔹 Implement monitoring (Prometheus + Grafana)  
- 🔹 Enable autoscaling (Kubernetes HPA)  
- 🔹 Improve prompt engineering for higher accuracy  

---

## Group Members

| Sr No | Name            | Enrollment Number |
|-------|-----------------|------------------|
| 01    | Ansh Kumbhare   | EN22CS301140     |
| 02    | Anshul Sen      | EN22CS301158     |
| 03    | Anshul Yadav    | EN22CS301159     |
| 04    | Armi Bhawsar    | EN22CS301194     |
| 05    | Atharv Dubey    | EN22CS301229     |  

---

## 🎓 Academic Context

- Institution: Medicaps University  
- Program: Datagami Skill-Based Program  
- Academic Year: 2025–2026  

---

## 📄 License

This project is for educational and demonstration purposes.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.

---
