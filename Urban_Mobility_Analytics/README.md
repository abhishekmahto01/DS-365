# 🚖 Urban Mobility Analytics

A Data Science project built as part of my **DS-365 (365-Day Data Scientist Challenge)**. The objective of this project is to analyze Uber pickup data, perform exploratory data analysis (EDA), build machine learning models, and create an end-to-end data science workflow using Python and PostgreSQL.

---

## 📌 Project Overview

This project focuses on analyzing Uber pickup datasets to understand travel patterns, demand distribution, and mobility trends.

The workflow includes:

* Data Collection
* Data Loading into PostgreSQL
* Data Profiling
* Exploratory Data Analysis (EDA)
* Data Cleaning
* Feature Engineering
* Machine Learning
* Visualization
* Model Evaluation

---

## 🛠️ Tech Stack

* Python
* PostgreSQL
* Pandas
* SQLAlchemy
* Psycopg2
* Git & GitHub
* VS Code

---

## 📂 Project Structure

```text
Urban_Mobility_Analytics/
│
├── data/
├── notebooks/
├── src/
│   ├── load_data.py
│   └── profile_data.py
│
├── README.md
└── requirements.txt
```

---

## ✅ Progress Log

### Day 1

* Created project structure.
* Initialized Git repository.
* Set up Python virtual environment.
* Created GitHub repository.

### Day 2

* Installed required Python libraries.
* Created PostgreSQL database.
* Configured SQLAlchemy connection.

### Day 3

* Imported Kaggle Uber datasets into PostgreSQL.
* Verified successful data loading.
* Listed all tables from the database.

### Day 4

* Created reusable `load_data()` function.
* Created reusable `profile_dataset()` function.
* Loaded tables dynamically from PostgreSQL.
* Generated dataset profile including:

  * Dataset shape
  * Data types
  * Summary statistics
  * Missing values

---

## 📊 Current Features

* PostgreSQL database connection
* Dynamic table loading
* Dataset profiling
* Reusable Python functions

---

## 🚀 Upcoming Tasks

* Duplicate value detection
* Memory usage analysis
* Data cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Data Visualization
* Machine Learning Models
* Model Evaluation
* Dashboard Development

---

## 🎯 Learning Goals

Through this project, I aim to strengthen my skills in:

* Python Programming
* SQL & PostgreSQL
* Data Analysis
* Exploratory Data Analysis
* Machine Learning
* Git & GitHub
* Writing production-ready, reusable code

---

## 👨‍💻 Author

**Abhishek Kumar**

* Data Analyst / Database Developer
* DS-365 (365-Day Data Scientist Challenge)

---

⭐ If you found this project useful, feel free to star the repository and follow my DS-365 journey.



## Project Progress

| Day | Task | Status |
|-----|------|--------|
| Day 1 | Project setup & repository structure | ✅ |
| Day 2 | Dataset collection & environment setup | ✅ |
| Day 3 | PostgreSQL connection & initial data profiling | ✅ |
| Day 4 | Data quality analysis | 🔄 |




## Day 4 — Data Cleaning & Feature Engineering

### Data Profiling

Performed initial data profiling on the `other_american_b01362` dataset.

* Rows: **91,712**
* Columns: **6**
* Useful Columns: **3**
* Completely Empty Columns: **3**
* Duplicate Rows: **588**
* Missing Values in Useful Columns: **0**
* Unique Dates: **92**
* Unique Pickup Addresses: **10,608**

### Data Cleaning

Implemented a basic data-cleaning pipeline using Pandas:

* Removed completely empty columns.
* Removed duplicate records.
* Converted `DATE` from string to datetime.
* Converted `TIME` from string to time format.
* Validated missing values after cleaning.
* Validated duplicate records after cleaning.

After cleaning:

* Rows: **91,124**
* Columns: **3**
* Missing values in useful columns: **0**
* Duplicate rows: **0**

### Feature Engineering

Created a combined `pickup_datetime` column from `DATE` and `TIME`.

Derived time-based analytical features:

* `pickup_date`
* `pickup_time`
* `pickup_hour`
* `pickup_minute`
* `pickup_second`
* `pickup_day`
* `pickup_month`
* `pickup_year`
* `pickup_weekday`
* `pickup_week`
* `pickup_quarter`
* `pickup_dayofyear`
* `is_weekend`

These features will be used later for time-based demand analysis and exploratory data analysis (EDA).

### Current Pipeline

```text
Raw PostgreSQL Data
        ↓
Data Profiling
        ↓
Data Quality Checks
        ↓
Remove Empty Columns
        ↓
Remove Duplicates
        ↓
Date & Time Transformation
        ↓
Pickup Datetime Creation
        ↓
Feature Engineering
        ↓
EDA (Next)
```

### Day 4 Status

**Completed ✅**

* Data profiling
* Data cleaning
* Duplicate removal
* Date/time transformation
* Feature engineering
* Code pushed to GitHub

**Next:** Create a separate cleaned table in PostgreSQL and begin Exploratory Data Analysis (EDA).
