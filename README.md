# 🎧 Spotify End-to-End Azure Data Engineering Project

## 🚀 Production-Ready Azure Data Pipeline

This project demonstrates a production-style Data Engineering pipeline built on Microsoft Azure.

The pipeline ingests Spotify datasets and processes them through a scalable Lakehouse architecture using Azure services.

The solution follows Medallion Architecture (Bronze → Silver → Gold).

---

## ⭐ Key Highlights

✔ End-to-End Azure Pipeline  
✔ Medallion Architecture  
✔ Incremental Data Loading  
✔ PySpark Transformations  
✔ Meta-data driven pipeline
✔ Delta Tables  
✔ Star Schema Modeling

---

## 🏗️ Architecture

(Add architecture diagram here)

![Architecture](architecture/architecture.png)

---

## ⚙️ Tech Stack

Azure Data Factory  
Azure Databricks  
Azure Data Lake Gen2  
Azure SQL Database  
PySpark  
Delta Lake  
SQL  
GitHub

---

## 🔄 Data Pipeline

Source → Azure Data Factory → Bronze → Databricks → Silver → Databricks → Gold

---

## 🧱 Medallion Architecture

### Bronze Layer

Raw data ingested from source system.

(Add Screenshot)

![Bronze](screenshots/bronze.png)

---

### Silver Layer

Cleaned and transformed data.

(Add Screenshot)

![Silver](screenshots/silver.png)

---

### Gold Layer

Analytics-ready business tables.

(Add Screenshot)

![Gold](screenshots/gold.png)

---

## 📊 Data Model

Star Schema implemented in Gold Layer.

(Add Screenshot)

![StarSchema](screenshots/star_schema.png)

---

## 📂 Repository Structure

spotify-azure-project/

├── notebooks/  
├── pipelines/  
├── scripts/  
├── screenshots/  
├── architecture/  
└── README.md

---

## 🚀 How to Run

1. Create Azure Resources  
2. Deploy Data Factory Pipelines  
3. Run Databricks Notebooks  
4. Verify Gold Tables

---

## 🎯 Skills Demonstrated

• Azure Data Factory  
• Azure Databricks  
• PySpark  
• Data Modeling  
• ETL Development  
• Data Lake Architecture

---

## 👩‍💻 Author

Lavanya K  
Data Analyst | Aspiring Data Engineer
