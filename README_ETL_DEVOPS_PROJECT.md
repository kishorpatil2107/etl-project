# ETL DevOps Pipeline Project 🚀

This project demonstrates an end-to-end ETL pipeline built using DevOps best practices. It processes sales and balance CSV data, transforms it using Python, loads it into PostgreSQL, and enables visualization through Apache Superset. The pipeline is containerized with Docker, orchestrated using Kubernetes CronJobs, and deployed via Jenkins CI/CD.

---

## 🔧 Tech Stack

- **ETL Language**: Python (Pandas, SQLAlchemy)
- **Containerization**: Docker
- **Orchestration**: Kubernetes CronJobs
- **CI/CD**: Jenkins
- **Database**: PostgreSQL
- **Monitoring**: Prometheus + Grafana
- **Visualization**: Apache Superset

---

## 📁 Project Structure

```
etl-project/
├── etl/                  # Python ETL code & Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── k8s/                  # Kubernetes CronJob + Postgres manifests
│   ├── etl-cronjob.yaml
│   └── postgres-deployment.yaml
├── jenkins/              # Jenkins pipeline script
│   └── Jenkinsfile
├── data/                 # Sample input CSVs
│   ├── sales.csv
│   └── balance.csv
└── README.md
```

---

## ⚙️ How It Works

1. **Data Ingestion**: Python reads `sales.csv` and `balance.csv` from the `data/` folder.
2. **Transformation**: Dates and columns are cleaned using Pandas.
3. **Load**: Data is inserted into PostgreSQL using SQLAlchemy.
4. **Scheduling**: ETL job runs hourly via a Kubernetes CronJob.
5. **CI/CD**: Jenkins automates Docker build, push, and deployment.
6. **Monitoring**: Prometheus/Grafana track job health, runtime, and database status.
7. **Visualization**: Superset connects to PostgreSQL for real-time dashboards.

---

## 🚀 Getting Started

### Prerequisites

- Docker
- Kubernetes (Minikube, Kind, or Cloud cluster)
- Jenkins
- PostgreSQL
- Python 3.10+

### Local Setup

```bash
git clone https://github.com/yourusername/etl-devops-pipeline.git
cd etl-project

# Build Docker image
docker build -t etl-job ./etl

# Apply K8s deployments
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/etl-cronjob.yaml
```

### Jenkins Pipeline

Jenkinsfile includes:
- Docker image build
- Push to Docker registry
- `kubectl apply` to deploy ETL CronJob

---

## 📊 Visualization

Use Apache Superset to create dashboards from the PostgreSQL database.

Example query for sales summary:

```sql
SELECT DATE_TRUNC('month', date) AS month, SUM(amount) AS total_sales
FROM sales
GROUP BY 1;
```

---

## 🧪 Monitoring

Prometheus and Grafana dashboards can be configured for:

- CronJob success/failure
- ETL execution time
- PostgreSQL connection metrics

---

## 📬 License

MIT License. Feel free to fork and adapt for your use case.