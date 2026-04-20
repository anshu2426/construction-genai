# Minikube Setup Guide for Construction GenAI

## Prerequisites

- Docker installed (for Minikube driver)
- At least 4GB RAM available
- 20GB free disk space
- Linux/macOS/Windows

## Note: Local Development vs Kubernetes

**For local development without Kubernetes:**
```bash
# Use .env file (already configured)
streamlit run construction_genai/app.py
```

**For Kubernetes deployment (this guide):**
Use Kubernetes Secrets (see Step 5 below)

## Step 1: Install Minikube

### Linux
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

### macOS
```bash
brew install minikube
```

### Windows
```bash
choco install minikube
```

## Step 2: Install kubectl

### Linux
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
```

### macOS
```bash
brew install kubectl
```

### Windows
```bash
choco install kubectl
```

## Step 3: Start Minikube

```bash
# Start Minikube with Docker driver
minikube start --driver=docker

# Verify status
minikube status

# Enable dashboard (optional)
minikube dashboard
```

## Step 4: Verify Docker Hub Image

The deployment uses the Docker Hub image `anshulyd26/construction-genai:latest`. Ensure this image exists and is up-to-date.

```bash
# Verify image exists on Docker Hub
docker pull anshulyd26/construction-genai:latest

# Verify image locally
docker images | grep construction-genai
```

## Step 5: Configure Google API Key

The `k8s/secret.yaml` file is already configured with your API key. If you need to update it, edit the file directly.

**Note:** `k8s/secret.yaml` is in `.gitignore` to prevent your API key from being committed to git.

## Step 6: Deploy to Kubernetes

```bash
# Apply all manifests
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Verify deployment
kubectl get pods
kubectl get services
```

## Step 7: Access the Application

```bash
# Get the URL to access your app
minikube service construction-genai --url

# Or use tunnel (works on all platforms)
minikube tunnel

# In another terminal, access the service
kubectl port-forward service/construction-genai 8501:8501
```

Then open: `http://localhost:8501`

## Step 8: Demonstrate Kubernetes Features

### Check Pod Status
```bash
kubectl get pods -w
```

### Scale Deployment
```bash
# Scale to 3 replicas
kubectl scale deployment construction-genai --replicas=3

# Scale back to 2
kubectl scale deployment construction-genai --replicas=2
```

### Self-Healing Demo
```bash
# List pods
kubectl get pods

# Delete a pod (watch it restart automatically)
kubectl delete pod <pod-name>

# Watch it recreate
kubectl get pods -w
```

### View Logs
```bash
# Get pod name
kubectl get pods

# View logs
kubectl logs <pod-name>

# Follow logs in real-time
kubectl logs -f <pod-name>
```

### Rolling Update
```bash
# Build and push new image to Docker Hub
docker build -t anshulyd26/construction-genai:v2 .
docker push anshulyd26/construction-genai:v2

# Update deployment
kubectl set image deployment/construction-genai construction-genai=anshulyd26/construction-genai:v2

# Watch rollout status
kubectl rollout status deployment/construction-genai
```

### Rollback if needed
```bash
kubectl rollout undo deployment/construction-genai
```

## Step 9: Stop Minikube

```bash
# Stop cluster (preserves state)
minikube stop

# Delete cluster (removes everything)
minikube delete
```

## Common Commands Reference

```bash
# Cluster management
minikube start              # Start cluster
minikube stop               # Stop cluster
minikube delete             # Delete cluster
minikube status             # Check status
minikube dashboard          # Open dashboard

# Kubernetes operations
kubectl get pods            # List pods
kubectl get services        # List services
kubectl get deployments     # List deployments
kubectl describe pod <name>  # Pod details
kubectl logs <pod-name>     # View logs
kubectl exec -it <pod-name> -- /bin/bash  # Access container shell

# Troubleshooting
kubectl get events          # View cluster events
kubectl describe pod <name> # Diagnose pod issues
minikube logs               # View Minikube logs
```

## Troubleshooting

### Minikube won't start
```bash
# Delete and restart
minikube delete
minikube start --driver=docker
```

### Pods not starting
```bash
# Check pod status
kubectl describe pod <pod-name>

# Check events
kubectl get events
```

### Image pull errors
```bash
# Verify image exists on Docker Hub
docker pull anshulyd26/construction-genai:latest

# Verify image locally
docker images | grep construction-genai

# Rebuild and push if needed
docker build -t anshulyd26/construction-genai:latest .
docker push anshulyd26/construction-genai:latest
```

### Port already in use
```bash
# Find process using port 8501
lsof -i :8501

# Kill the process
kill -9 <PID>
```

## For College Project Documentation

Include screenshots of:
1. Minikube status showing cluster running
2. `kubectl get pods` showing running pods
3. `kubectl get services` showing the service
4. The application running in browser
5. Scaling demonstration (before/after)
6. Self-healing demonstration (pod deletion and recreation)
7. Kubernetes dashboard (if used)

## Key Concepts to Explain in Report

- **Pod**: Smallest deployable unit
- **Deployment**: Manages pod replicas and updates
- **Service**: Network endpoint to access pods
- **ReplicaSet**: Ensures specified number of pod replicas
- **Self-healing**: Automatic pod restart on failure
- **Scaling**: Horizontal scaling with replicas
- **LoadBalancer**: Exposes service externally

## Production vs Development

Explain that for production, you would:
- Use AWS EKS instead of Minikube
- Store Docker images in Docker Hub or ECR
- Use proper secrets management (AWS Secrets Manager)
- Set up proper monitoring and logging
- Configure ingress controllers for routing
- Implement proper resource limits and quotas
