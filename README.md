Crypto Analytics Pipeline with Databricks & Delta Lake.

This project implements a batch data pipeline using Databricks, PySpark and Delta Lake, following a Bronze–Silver–Gold architecture.

Architecture
- **Bronze**: Raw ingestion from Coinbase API
- **Silver**: Data cleaning, type casting and normalization
- **Gold**: Analytical layer with window functions (daily price variation)

Technologies
- Databricks
- Apache Spark (PySpark)
- Delta Lake
- REST API

Key Concepts Applied
- Schema evolution (`mergeSchema`)
- Window functions (`LAG`)
- Medallion Architecture
- Data type handling from external APIs

Motivation
This project is part of a personal 50-day challenge focused on deepening my skills in data engineering and analytics.

