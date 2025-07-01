# GitHub Logs Processing Pipeline
![Pipeline Architecture](https://drive.google.com/file/d/1AgWepLxou1keuVm4AVkmIVg27lfereIu/view?usp=share_link)


This project is an end-to-end data pipeline that retrieves public event logs from the GitHub API, stores them in local files, uploads to AWS S3 and transfer to Redshift, can be quired by Athena or Redshift

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

- 🔁 Automatically fetch GitHub event logs using the GitHub API daily
- 🧹 Clean and structure logs for storage
- 🛢 Upload logs to:
  - Local storage (for audit/debugging)
  - Amazon S3
- ⛓️ Orchestrated by Apache Airflow
- 🧪 Ready for extension to Amazon Redshift

## 🛠 Setup Instructions

```bash
git clone https://github.com/your-username/github-logs-processing.git
cd github-logs-processing
docker-compose build
docker-compose run --rm airflow-init
docker-compose up -d
```