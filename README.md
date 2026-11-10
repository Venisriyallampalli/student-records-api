# Student Records Management System - Lab Assignment

This project contains the complete implementation and solutions for all 4 assignment questions.

---

## Question 1: Simple REST API Using Python Flask (Student Records)

### Implementation
- **Source Code**: [`app.py`](app.py)
- **Dependencies**: [`requirements.txt`](requirements.txt) (`Flask>=3.0.0`)
- **Automated Test Client**: [`test_api.py`](test_api.py)

### Endpoints Table

| HTTP Method | Endpoint | Description | Request Body | Success Status |
|-------------|----------|-------------|--------------|----------------|
| `GET` | `/` | Root endpoint showing API documentation | None | `200 OK` |
| `GET` | `/health` | Healthcheck endpoint | None | `200 OK` |
| `GET` | `/students` | Retrieve all student records | None | `200 OK` |
| `GET` | `/students/<id>` | Retrieve a single student by ID | None | `200 OK` (or `404`) |
| `POST` | `/students` | Create/add a new student record | `{"name": "...", "course": "...", "grade": "..."}` | `201 CREATED` |
| `PUT` | `/students/<id>` | Update an existing student record | `{"name": "...", "course": "...", "grade": "..."}` | `200 OK` (or `404`) |
| `DELETE` | `/students/<id>`| Remove/delete a student record | None | `200 OK` (or `404`) |

### How to Run and Test
1. **Start the API Server**:
   ```bash
   python app.py
   ```
2. **Run Automated Endpoint Tests**:
   ```bash
   python test_api.py
   ```
3. **Test using cURL**:
   - **GET All Students**:
     ```bash
     curl -i http://127.0.0.1:5000/students
     ```
   - **POST (Add New Student)**:
     ```bash
     curl -i -X POST http://127.0.0.1:5000/students -H "Content-Type: application/json" -d "{\"name\": \"Kiran Kumar\", \"course\": \"Data Science\", \"grade\": \"A\"}"
     ```
   - **PUT (Update Student ID 4)**:
     ```bash
     curl -i -X PUT http://127.0.0.1:5000/students/4 -H "Content-Type: application/json" -d "{\"name\": \"Kiran Kumar\", \"course\": \"Artificial Intelligence\", \"grade\": \"A+\"}"
     ```
   - **DELETE (Delete Student ID 2)**:
     ```bash
     curl -i -X DELETE http://127.0.0.1:5000/students/2
     ```

---

## Question 2: Local Git Repository, Branching, Merging & GitHub Push

### 1. Initialize Local Repository and Initial Commit
```bash
git init -b main
git add .
git commit -m "Initial commit: Flask Student Records REST API, Dockerfile, and Kubernetes Deployment"
```

### 2. Create Feature Branch and Merge into Main
```bash
# Create and switch to feature branch
git checkout -b feature/student-improvements

# Make changes (added /health endpoint to app.py)
git add app.py
git commit -m "Feature: Add health check endpoint"

# Switch back to main and merge
git checkout main
git merge feature/student-improvements --no-ff -m "Merge branch 'feature/student-improvements' into main"
```

### 3. Verify Branch History
```bash
git log --graph --oneline --all
```
Output:
```
*   75f2f23 Merge branch 'feature/student-improvements' into main
|\  
| * 21b66b4 Feature: Add health check endpoint
|/  
* b7c3bcf Initial commit: Flask Student Records REST API, Dockerfile, and Kubernetes Deployment
```

### 4. Push to Remote GitHub Repository
```bash
# Add your GitHub remote repository URL
git remote add origin https://github.com/<your-username>/student-records-api.git

# Ensure current branch is named main
git branch -M main

# Push the committed code to GitHub
git push -u origin main
```

---

## Question 3: Dockerfile, Build, Run, Port Mapping & cURL Demo

### Dockerfile
- **File**: [`Dockerfile`](Dockerfile)
```dockerfile
# Use an official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency definition
COPY requirements.txt .

# Install dependencies without cache to keep image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variable to run in production mode
ENV FLASK_ENV=production

# Run the Flask application
CMD ["python", "app.py"]
```

### Docker Commands
1. **Build Docker Image**:
   ```bash
   docker build -t student-api:latest .
   ```
2. **Run Docker Container with Port Mapping (`host:container = 5000:5000`)**:
   ```bash
   docker run -d --name student-api-app -p 5000:5000 student-api:latest
   ```
3. **Verify Container is Running**:
   ```bash
   docker ps
   ```
4. **Demonstrate Application via Browser or cURL**:
   - Browser URL: `http://localhost:5000/students`
   - cURL Terminal:
     ```bash
     curl -i http://localhost:5000/students
     ```

---

## Question 4: Kubernetes Deployment YAML & Verification with kubectl

### Deployment and Service Configuration
- **File**: [`deployment.yaml`](deployment.yaml)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: student-api-deployment
  labels:
    app: student-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: student-api
  template:
    metadata:
      labels:
        app: student-api
    spec:
      containers:
      - name: student-api-container
        image: student-api:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 5000
        resources:
          limits:
            cpu: "500m"
            memory: "256Mi"
          requests:
            cpu: "100m"
            memory: "128Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: student-api-service
spec:
  type: NodePort
  selector:
    app: student-api
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
      nodePort: 30005
```

### Apply and Verify with kubectl
1. **Apply Deployment and Service**:
   ```bash
   kubectl apply -f deployment.yaml
   ```
2. **Verify Pods (showing 2 replicas running)**:
   ```bash
   kubectl get pods -l app=student-api
   ```
   *Expected Output:*
   ```
   NAME                                     READY   STATUS    RESTARTS   AGE
   student-api-deployment-7d58f5bc9b-8vkmw   1/1     Running   0          15s
   student-api-deployment-7d58f5bc9b-w9zxp   1/1     Running   0          15s
   ```
3. **Verify Deployment**:
   ```bash
   kubectl get deployments
   ```
   *Expected Output:*
   ```
   NAME                     READY   UP-TO-DATE   AVAILABLE   AGE
   student-api-deployment   2/2     2            2           20s
   ```
4. **Verify Service**:
   ```bash
   kubectl get svc student-api-service
   ```
