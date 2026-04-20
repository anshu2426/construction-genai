# Construction Content Generator

AI-powered construction site report generator built with Streamlit.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline for EC2 deployment
├── k8s/                        # Kubernetes manifests
│   ├── deployment.yaml         # Deployment configuration
│   ├── service.yaml            # Service configuration
│   └── secret.yaml             # Secret for API keys (gitignored)
├── construction_genai/         # Source code
│   ├── app.py                  # Main Streamlit application
│   ├── llm_engine.py           # LLM integration
│   ├── vector_db.py            # Vector database for document search
│   ├── prompts.py              # AI prompts
│   └── data/                   # Knowledge base documents
├── Dockerfile                  # Container image definition
├── docker-compose.yml          # Docker Compose configuration
├── requirements.txt            # Python dependencies
├── .dockerignore              # Docker build exclusions
├── .gitignore                 # Git exclusions
├── README.md                  # Project documentation
├── DEPLOYMENT.md              # AWS EC2 deployment guide
└── MINIKUBE_SETUP.md          # Kubernetes/Minikube setup guide

```

## Features

- AI-powered content generation using Google Gemini
- Vector-based document search
- Professional PDF report generation
- Modern, responsive UI

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run construction_genai/app.py
```

### Using Docker Compose

```bash
# Set Docker host for Docker Desktop (if using desktop-linux context)
export DOCKER_HOST=unix:///home/anshul/.docker/desktop/docker.sock

# Run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down
```

## Deployment

### Production (AWS EC2)
See [DEPLOYMENT.md](DEPLOYMENT.md) for AWS EC2 deployment instructions using CI/CD.

### Local Development (Minikube/Kubernetes)
See [MINIKUBE_SETUP.md](MINIKUBE_SETUP.md) for running the application on Kubernetes locally using Minikube. This is ideal for learning Kubernetes concepts and demonstration purposes.

## Environment Variables

- `GOOGLE_API_KEY`: Required for Google Gemini AI integration

### Local Development (.env)
For local development (Streamlit directly), use the `.env` file (already configured with your API key).

### Kubernetes (Secret)
For Kubernetes deployment, use `k8s/secret.yaml` (already configured with your API key).

## Tech Stack

- **Frontend**: Streamlit
- **AI**: Google Gemini (google-genai)
- **Vector Search**: scikit-learn (TF-IDF)
- **PDF Generation**: fpdf
- **Deployment**: Docker, GitHub Actions, AWS EC2
