# ci-cd-airflow

This project automates the provisioning of an Apache Airflow instance on a GCP Compute Engine VM using a Bash script. It includes Airflow installation, Cloud SQL Proxy setup, MySQL DB connection, systemd service configuration, and DAG synchronization from a GitHub repository.

---

## 🚀 Features

- Installs Apache Airflow (v2.9.3) in a Python virtual environment
- Uses Cloud SQL Proxy to connect to a managed MySQL database
- Initializes Airflow metadata DB and creates an admin user
- Sets up Airflow Webserver and Scheduler as systemd services
- Automatically syncs DAGs from a GitHub repository every 2 minutes using cron

---

## 🧰 Prerequisites

- Ubuntu-based GCP Compute Engine VM
- Cloud SQL instance (MySQL)
- Billing enabled and IAM access configured
- Google Cloud SDK (`gcloud`) installed and authenticated
- GitHub SSH access configured for the Airflow user
- Secret in Secret Manager containing DB password

---

## 📁 File Structure
'''
ci-cd-airflow/
│
├── script.sh # Main provisioning script
├── dags/ # DAGs pulled from GitHub (auto-synced)
└── README.md # This documentation
'''


---

## ⚙️ Configuration Variables

The following variables are configurable in `script.sh`:

| Variable                | Description                                         |
|-------------------------|-----------------------------------------------------|
| `AIRFLOW_USER`          | System user that runs Airflow                       |
| `AIRFLOW_VERSION`       | Airflow version to install                          |
| `INSTANCE_CONNECTION_NAME` | Cloud SQL instance identifier (`project:region:instance`) |
| `DB_USER`, `DB_NAME`    | Database credentials                                |
| `SECRET_NAME`           | Name of the secret in Google Secret Manager         |
| `REPO_URL`              | GitHub repository URL containing DAGs               |
| `BRANCH_NAME`           | Git branch to sync DAGs from                        |

---

## 📜 How to Use

1. **Login to your VM**

   ```bash
   ssh <your-vm>
---------------------------------------

# Make the script executable
# chmod +x script.sh

# Run the script as root
# sudo ./script.sh

