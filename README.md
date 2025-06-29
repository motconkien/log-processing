# GitHub Logs Processing Pipeline

This project is an end-to-end data pipeline that retrieves public event logs from the GitHub API, stores them in local files, uploads to AWS S3 and prepares for further transfer to Amazon Redshift.

## 📦 Project Structure
```
GitHub-logs-processing/
├── configs/
│ └── config.json # Configuration file (API tokens, AWS keys, paths)
├── dags/
│ └── logs_dag.py # Apache Airflow DAG to orchestrate the pipeline
├── data/
│ ├── logs/ # Stored GitHub logs data
│ └── users/ # Stored GitHub users data
├── pipelines/
│ ├── log_pipeline.py # Fetch and process GitHub logs
│ ├── users_pipeline.py # Fetch and process GitHub user data
│ └── aws_pipeline.py # Upload data to AWS S3 
├── utils/
│ └── constants.py # Constants used across the project
├── airflow.env # Environment variables for Airflow
├── docker-compose.yml # Docker compose file for services
├── Dockerfile # Dockerfile for building the project image
├── requirements.txt # Python dependencies list
└── README.md # Project documentation
```


## 🚀 Features

- 🔁 Automatically fetch GitHub event logs using the GitHub API
- 🧹 Clean and structure logs for storage
- 🛢 Upload logs to:
  - Local storage (for audit/debugging)
  - PostgreSQL database
  - Amazon S3
- ⛓️ Orchestrated by Apache Airflow
- 🧪 Ready for extension to Amazon Redshift

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/github-logs-processing.git
cd github-logs-processing
docker-compose build
docker-compose run --rm airflow-init
docker-compose up -d
```