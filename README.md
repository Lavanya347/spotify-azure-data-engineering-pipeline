# 🎧 Spotify End-to-End Azure Data Engineering Pipeline

This project demonstrates a **production-style Data Engineering pipeline built on Microsoft Azure**.

The pipeline ingests Spotify datasets, stores them in a Data Lake, performs scalable transformations using Databricks, and produces analytics-ready datasets using **Medallion Architecture (Bronze → Silver → Gold).**

This project showcases the core skills required for modern **Cloud Data Engineering roles**.

---

# ⭐ Project Highlights

✔ Built an end-to-end Azure Data Engineering pipeline  
✔ Implemented Medallion Architecture (Bronze → Silver → Gold)  
✔ Developed dynamic ingestion pipelines using Azure Data Factory  
✔ Performed scalable transformations using PySpark in Azure Databricks  
✔ Designed an analytical **Star Schema data model**

---

# 🏗️ Project Architecture

The architecture shows how data flows across Azure services from ingestion to analytics.

![Architecture](screenshots/1.%20Architecture.png)

---

# 🔄 Data Flow Pipeline

The pipeline processes data through multiple layers.

Source Data  
⬇  
Azure Data Factory (Data Ingestion)  
⬇  
Azure Data Lake Storage Gen2 (Bronze Layer – Raw Data)  
⬇  
Azure Databricks (PySpark Transformations)  
⬇  
Silver Layer (Cleaned Data)  
⬇  
Gold Layer (Analytics Tables)

---

# ☁️ Azure Resource Setup

All services used in the project are grouped inside a single Azure Resource Group.

![Resource Group](screenshots/2.%20Resource_group.png)

---

# 🔄 Azure Data Factory Pipeline

Azure Data Factory orchestrates the ingestion pipeline that loads raw Spotify data into the Data Lake.

![ADF Pipeline](screenshots/4.%20ADF_Pipeline.png)

The pipeline dynamically ingests multiple files using **ForEach activity**, enabling scalable ingestion.

---

# 🥉 Bronze Layer (Raw Data)

The Bronze layer stores raw data exactly as it arrives from the source.

This layer preserves the original dataset for traceability and reprocessing.

![Bronze Layer](screenshots/6.%20Bronze.png)

---

# 🥈 Silver Layer (Cleaned Data)

The Silver layer contains cleaned and transformed datasets generated using **PySpark in Databricks**.

Data quality improvements and standardization occur in this layer.

![Databricks Silver Tables](screenshots/9.%20Databricks_Silver_Tables.png)

---

# 🥇 Gold Layer (Analytics Ready)

The Gold layer contains analytics-ready tables designed for BI and reporting workloads.

![Databricks Gold Tables](screenshots/10.%20Databricks_Gold_Tables.png)

---

# ⭐ Gold Layer Data Model

The Gold layer implements a **Star Schema** optimized for analytical queries.

Fact Table

- factstream

Dimension Tables

- dimartist  
- dimtrack  
- dimdate  
- dimuser  

This schema enables efficient reporting and dashboarding.

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|--------|
Azure Data Factory | Data Ingestion & Orchestration |
Azure Data Lake Storage Gen2 | Data Lake Storage |
Azure Databricks | Distributed Data Processing |
PySpark | Data Transformations |
Delta Lake | Reliable Data Storage |
GitHub | Version Control |

---

# 📊 Data Engineering Concepts Demonstrated

- End-to-End Data Pipeline Development
- Medallion Architecture
- Cloud Data Lake Design
- Incremental Data Ingestion
- Distributed Data Processing
- Data Modeling (Star Schema)
- ETL / ELT Pipelines

---

# 📂 Repository Structure

```
Azure-Project/

dataset/                 → Source datasets
factory/                 → Data Factory configuration
linkedService/           → Azure service connections
pipeline/                → ADF pipelines
screenshots/             → Project screenshots
spotify_dab/             → Databricks notebooks
README.md
```

---

# 🚀 How to Run This Project

1️⃣ Create Azure Resource Group  
2️⃣ Create Azure Data Lake Storage Gen2  
3️⃣ Deploy Azure Data Factory pipelines  
4️⃣ Load datasets into the Bronze layer  
5️⃣ Run Databricks notebooks for transformations  
6️⃣ Generate Silver and Gold tables  

---

# 👩‍💻 Author

Hi, I’m **Lavanya** 👋
I’m an IT professional and aspiring **Data Analyst** passionate about building data-driven solutions.
I enjoy working with SQL, data warehousing, and analytics to transform raw data into meaningful insights.
This project is part of my portfolio to demonstrate hands-on experience in **data engineering and analytics**.

## 🔗 Connect with Me
🔗 **[LinkedIn Profile](https://www.linkedin.com/in/lavanya-lk)**  
📧 **Email:** lavanya347@gmail.com  
Lavanya K  

Data Analyst | Aspiring Data Engineer
