# 🚀 DS-365 | Urban Mobility Analytics

A 365-day Data Engineering & Data Science challenge focused on building production-ready data pipelines, analytics workflows, and machine learning solutions using real-world datasets.

---

## 🎯 Project Goal

The goal of this project is to master the complete Data Science lifecycle by working on a real-world urban mobility dataset.

The project covers:

- Data Engineering
- SQL
- PostgreSQL
- Python
- Data Analysis
- Data Visualization
- Machine Learning
- Deployment

---

# 🛠 Tech Stack

- Python
- PostgreSQL
- SQLAlchemy
- Pandas
- Git
- GitHub
- VS Code

---

# 📅 Progress

| Day | Module | Status |
|------|--------|--------|
| Day 1 | Project Setup & Dataset Collection | ✅ |
| Day 2 | PostgreSQL ETL Pipeline | ✅ |

---

# 🚀 Day 1

## Objective

Initialize the project and prepare the development environment.

### Completed

- Created project structure
- Configured Git repository
- Created Python virtual environment
- Installed required libraries
- Downloaded and organized 19 CSV datasets

### Learning

- Git & GitHub
- Virtual Environment
- Project Structure
- Dataset Organization

---

# 🚀 Day 2

## Objective

Build an automated ETL pipeline to load CSV files into PostgreSQL.

### Completed

- Connected Python with PostgreSQL
- Created automated CSV loader
- Imported 19 CSV files
- Automatic table creation
- Dynamic table naming
- Encoding fallback support
- Successfully loaded all datasets into PostgreSQL

### Learning

- SQLAlchemy
- Pandas
- PostgreSQL
- ETL Pipeline
- Error Handling

---

# 📌 Next Step

- Data Profiling
- Data Validation
- Exploratory Data Analysis (EDA)




## 📅 Day 3 – PostgreSQL Integration & First Data Profiling

### 🎯 Objective

Connect Python to PostgreSQL and begin exploring the imported datasets.

### ✅ Tasks Completed

* Connected Python application to PostgreSQL using **SQLAlchemy**.
* Successfully tested the database connection.
* Queried **`information_schema.tables`** to discover all available tables.
* Verified that **19 datasets** were successfully imported into PostgreSQL.
* Retrieved the first table dynamically from the database.
* Loaded the first dataset into a **Pandas DataFrame** using `pd.read_sql()`.
* Performed initial data profiling:

  * Checked dataset shape (**91,712 rows × 6 columns**).
  * Inspected column names.
  * Examined data types.
  * Previewed the first five records using `df.head()`.

### 📚 Key Concepts Learned

* SQLAlchemy database connection
* Executing SQL queries from Python
* PostgreSQL metadata (`information_schema.tables`)
* Reading SQL query results into Pandas
* Difference between database metadata and actual table data
* Basic DataFrame inspection (`shape`, `columns`, `dtypes`, `head()`)

### 🚀 Outcome

Successfully established the complete workflow from **Python → PostgreSQL → SQL Query → Pandas DataFrame**. This creates the foundation for automated profiling, data cleaning, and feature engineering in the upcoming stages of the project.

### 🔜 Next Goal (Day 4)

* Perform detailed data quality assessment.
* Check missing values and duplicate records.
* Identify unnecessary columns.
* Convert date/time columns to appropriate data types.
* Begin automating profiling for all 19 datasets.
