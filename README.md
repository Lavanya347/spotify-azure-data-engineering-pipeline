# 🎧 Spotify End-to-End Azure Data Engineering Project

This project demonstrates a complete **End-to-End Data Engineering pipeline built on Microsoft Azure**.

The pipeline ingests Spotify dataset files, processes them using scalable Azure services, and transforms them into analytics-ready datasets using **Medallion Architecture (Bronze → Silver → Gold).**

The project implementation is inspired by the learning content from **Ansh Lamba**.

---

# 🚀 Project Architecture

The architecture shows how data flows across Azure services including ingestion, transformation, and storage.

![Architecture](screenshots/1.%20Architecture.png)

---

# ☁️ Azure Resource Group

All Azure services used in the project are organized under a single **Resource Group** for easy management.

![Resource Group](screenshots/2.%20Resource_group.png)

---

# 📦 Data Lake Storage Containers

The Azure Data Lake Storage contains multiple containers for organizing raw and processed data.

Typical containers include:

- Bronze (Raw Data)
- Silver (Cleaned Data)
- Gold (Analytics Data)

![Containers](screenshots/3.%20Containers.png)

---

# 🔄 Azure Data Factory Pipeline

Azure Data Factory is used to orchestrate the ingestion pipeline that loads raw Spotify data into the data lake.

![ADF Pipeline](screenshots/4.%20ADF_Pipeline.png)

---

# 🔁 Incremental Ingestion Using ForEach Loop

The pipeline uses **ForEach activity** to dynamically ingest multiple files from the source system.

This makes the ingestion pipeline scalable and automated.

![ADF ForEach Pipeline](screenshots/5.%20ADF_Pipeline(For%20each).png)

---

# 🥉 Bronze Layer (Raw Data)

The Bronze layer stores the raw ingested data exactly as it arrives from the source.

No transformations are applied here.

![Bronze Layer](screenshots/6.%20Bronze.png)

---

# 📂 Project Repository Structure

The repository is organized to clearly separate pipelines, datasets, linked services, and Databricks notebooks.

![Folder Structure](screenshots/7.%20folder_struct.png)

---

# 🥇 Gold Layer Data Pipeline

The Gold layer contains **business-ready datasets** used for reporting and analytics.

Transformations are executed using **Azure Databricks and PySpark**.

![Gold Pipeline](screenshots/8.%20Gold_Pipeline.png)

---

# 🧠 Databricks Catalog & Tables

Azure Databricks is used for large-scale data transformations and table creation.

Tables are registered in the Databricks catalog for easy querying and analysis.

![Databricks Catalog](screenshots/9.%20DataBricks_Catalog.png)

---

# ⚙️ Technologies Used

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- Azure SQL
- GitHub

---

# 📊 Data Engineering Concepts Demonstrated

- End-to-End Data Pipeline
- Medallion Architecture
- Incremental Data Ingestion
- Data Lake Design
- ETL / ELT Pipelines
- PySpark Transformations
- Cloud Data Engineering

---

# 👩‍💻 Author

Lavanya K  
Data Analyst | Aspiring Data Engineer
