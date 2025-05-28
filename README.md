# End-to-End GitHub Actions CI/CD Workflow with Docker Hub

This project demonstrates a complete CI/CD pipeline using **GitHub Actions** with **Docker Hub** integration. It showcases how to build, test, and deploy a containerized Flask application automatically whenever code changes are pushed to the repository.

## 🚀 Project Overview

This Flask web application demonstrates:

- **Flask REST API**: Simple mathematical operations service
- **Comprehensive Testing**: Unit tests and integration tests
- **Docker Containerization**: Multi-stage Docker builds
- **GitHub Actions CI/CD**: Automated testing, building, and deployment
- **Docker Hub Integration**: Automated image publishing with authentication
- **Security Best Practices**: Secret management and secure deployments

## 📁 Project Structure

```
Second_Github_Action_CI_CD_Dockerhub/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Local development setup
├── .dockerignore              # Docker ignore file
├── .github/
│   └── workflows/
│       └── ci-cd-dockerhub.yml # GitHub Actions workflow
├── tests/
│   ├── __init__.py
│   ├── test_app.py            # Unit tests
│   └── test_integration.py    # Integration tests
├── .gitignore
└── README.md
```

## 🛠️ Flask Application Features

### API Endpoints

| Method | Endpoint     | Description                      | Example                                                                                                                 |
| ------ | ------------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| GET    | `/`          | Health check and welcome message | `curl http://localhost:5000/`                                                                                           |
| POST   | `/calculate` | Perform mathematical operations  | `curl -X POST -H "Content-Type: application/json" -d '{"operation":"add","a":5,"b":3}' http://localhost:5000/calculate` |
| GET    | `/health`    | Application health status        | `curl http://localhost:5000/health`                                                                                     |

### Supported Mathematical Operations

- **Addition**: `{"operation": "add", "a": 5, "b": 3}`
- **Subtraction**: `{"operation": "subtract", "a": 10, "b": 4}`
- **Multiplication**: `{"operation": "multiply", "a": 6, "b": 7}`
- **Division**: `{"operation": "divide", "a": 15, "b": 3}`

### Example API Usage

```bash
# Addition
curl -X POST -H "Content-Type: application/json" \
  -d '{"operation":"add","a":10,"b":5}' \
  http://localhost:5000/calculate

# Response: {"result": 15, "operation": "add", "operands": [10, 5]}
```

## 🐳 Docker Integration

### Multi-Stage Docker Build

The Dockerfile uses multi-stage builds for optimization:

1. **Build Stage**: Install dependencies and prepare application
2. **Production Stage**: Copy only necessary files for smaller image size
3. **Security**: Runs as non-root user
4. **Health Checks**: Built-in container health monitoring

### Local Development with Docker

```bash
# Build the Docker image
docker build -t flask-dockerhub-app .

# Run the container
docker run -p 5000:5000 flask-dockerhub-app

# Using Docker Compose (recommended for development)
docker-compose up --build
```

## 🔄 CI/CD Pipeline with GitHub Actions

### Workflow Triggers

- **Push to main branch**: Full CI/CD pipeline
- **Pull Request**: Testing and validation only
- **Manual dispatch**: On-demand workflow execution

### Pipeline Stages

#### 1. **Code Quality & Testing**

```yaml
- Checkout code
- Set up Python environment
- Install dependencies
- Run linting (flake8)
- Execute unit tests
- Execute integration tests
- Generate test coverage reports
```

#### 2. **Docker Build & Security**

```yaml
- Build Docker image
- Scan for vulnerabilities (Trivy)
- Test Docker container functionality
- Validate health checks
```

#### 3. **Docker Hub Deployment**

```yaml
- Authenticate with Docker Hub
- Tag images with version/latest
- Push to Docker Hub repository
- Clean up temporary resources
```

### Docker Hub Image Tagging Strategy

- `latest`: Most recent successful build from main branch
- `v1.0.0`: Semantic versioning for releases
- `main-{sha}`: Commit-specific builds for traceability

## 🔐 Security Configuration

### Required GitHub Secrets

You must configure these secrets in your GitHub repository:

| Secret Name          | Description                             | Example                   |
| -------------------- | --------------------------------------- | ------------------------- |
| `DOCKERHUB_USERNAME` | Your Docker Hub username                | `your-dockerhub-username` |
| `DOCKERHUB_TOKEN`    | Docker Hub access token (not password!) | `dckr_pat_xxxxxxxx`       |

### Setting Up GitHub Secrets

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the required secrets:

```bash
# Create Docker Hub Access Token first:
# 1. Login to Docker Hub
# 2. Go to Account Settings → Security → Access Tokens
# 3. Generate new token with Read/Write/Delete permissions
# 4. Copy the token (you won't see it again!)
```

### Docker Hub Access Token Setup

1. **Login to Docker Hub**: Go to [hub.docker.com](https://hub.docker.com)
2. **Account Settings**: Click on your profile → Account Settings
3. **Security Tab**: Navigate to Security section
4. **Access Tokens**: Click "New Access Token"
5. **Token Configuration**:
   - **Description**: `GitHub Actions CI/CD`
   - **Permissions**: `Read, Write, Delete`
6. **Copy Token**: Save the generated token immediately
7. **Add to GitHub**: Use this token as `DOCKERHUB_TOKEN` secret

## 🧪 Testing Strategy

### Unit Tests

- Test individual functions and methods
- Mock external dependencies
- Validate input/output behavior
- Cover edge cases and error handling

### Integration Tests

- Test complete API endpoints
- Validate request/response cycles
- Test error scenarios
- Database integration (if applicable)

### Running Tests Locally

```bash
# Install development dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test categories
pytest tests/test_app.py -v           # Unit tests
pytest tests/test_integration.py -v  # Integration tests
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+**
- **Docker & Docker Compose**
- **Git**
- **Docker Hub Account**

### Local Development Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/Second_Github_Action_CI_CD_Dockerhub.git
   cd Second_Github_Action_CI_CD_Dockerhub
   ```

2. **Set up Python environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:

   ```bash
   python app.py
   ```

4. **Test the application**:

   ```bash
   # Health check
   curl http://localhost:5000/

   # Test calculation
   curl -X POST -H "Content-Type: application/json" \
     -d '{"operation":"add","a":10,"b":5}' \
     http://localhost:5000/calculate
   ```

## 🔧 Configuration Management

### Environment Variables

| Variable    | Default      | Description             |
| ----------- | ------------ | ----------------------- |
| `FLASK_ENV` | `production` | Application environment |
| `PORT`      | `5000`       | Application port        |
| `LOG_LEVEL` | `INFO`       | Logging level           |

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

## 🎯 Learning Objectives

This project teaches:

- **Modern CI/CD practices** with GitHub Actions
- **Docker containerization** best practices
- **Flask web development** fundamentals
- **Automated testing** strategies
- **Security** in DevOps workflows

## 🔗 Related Projects

- [First GitHub Actions Project](../First_Github_Action_Project/): Basic CI/CD fundamentals
- [Airflow ETL Pipeline](../Airflow_ETL_Pipeline_Astro_Postgres/): Data pipeline automation

---

**Happy Coding! 🚀**
