# AWS EC2 Deployment Guide (Docker Hub)

## Prerequisites

1. Docker Hub account
2. GitHub repository with this code
3. EC2 instance running (Ubuntu 22.04 recommended)
4. Docker installed on EC2

## EC2 Setup

### 1. Configure EC2 Security Group
- Allow inbound: SSH (22), HTTP (80), HTTPS (443), Custom (8501)
- Source: Your IP for SSH, 0.0.0.0/0 for HTTP/HTTPS/8501

### 2. Setup EC2 Instance
```bash
# SSH into EC2
sudo apt update
sudo apt install docker.io -y
sudo usermod -aG docker ubuntu
# Logout and login back
```

### 3. Login to Docker Hub on EC2 (One-time)
```bash
docker login
# Enter your Docker Hub credentials
```

## GitHub Secrets Configuration

Add these secrets in your GitHub repository settings:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token
- `EC2_HOST`: EC2 public IP or DNS
- `EC2_SSH_KEY`: Private SSH key content (full key file)
- `GOOGLE_API_KEY`: Your Google AI API key

## Deployment

1. Push code to main branch
2. GitHub Actions automatically:
   - Builds Docker image
   - Pushes to Docker Hub
   - Deploys to EC2

## Access Application

```
http://<your-ec2-public-ip>:8501
```

## Manual Deployment (if needed)

```bash
# From EC2 instance
docker pull <dockerhub-username>/construction-genai
docker stop construction-genai
docker rm construction-genai
docker run -d --name construction-genai -p 8501:8501 --restart unless-stopped <dockerhub-username>/construction-genai
```
