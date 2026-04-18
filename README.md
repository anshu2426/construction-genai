# Construction Content Generator

AI-powered construction site report generator built with Streamlit.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline for EC2 deployment
├── construction_genai/         # Source code
│   ├── app.py                  # Main Streamlit application
│   ├── llm_engine.py           # LLM integration
│   ├── vector_db.py            # Vector database for document search
│   ├── prompts.py              # AI prompts
│   └── data/                   # Knowledge base documents
├── Dockerfile                  # Container image definition
├── requirements.txt            # Python dependencies
├── .dockerignore              # Docker build exclusions
├── .gitignore                 # Git exclusions
└── DEPLOYMENT.md              # Deployment guide

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

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for AWS EC2 deployment instructions using CI/CD.

## Environment Variables

- `GOOGLE_API_KEY`: Required for Google Gemini AI integration

## Tech Stack

- **Frontend**: Streamlit
- **AI**: Google Gemini (google-genai)
- **Vector Search**: scikit-learn (TF-IDF)
- **PDF Generation**: fpdf
- **Deployment**: Docker, GitHub Actions, AWS EC2
