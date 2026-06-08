# Child Nutrition Trend and Future Condition Prediction using Machine Learning
<img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/ce745d3d-cef2-4c71-839a-39d81f88f563" />

## Project Overview

This project analyzes Growth Monitoring Program (GMP) data to identify child nutrition trends and predict future nutrition conditions using machine learning techniques.

The system performs data cleaning, nutrition condition classification, clustering, trend analysis, and future condition prediction based on historical MUAC measurements and visit records.

---

## Objectives

* Clean and preprocess GMP data
* Classify child nutrition conditions using MUAC values
* Identify nutrition risk groups using K-Means clustering
* Analyze nutrition improvement and deterioration trends
* Predict future nutrition conditions using machine learning
* Support early intervention for at-risk children

---

## Dataset Information

### Total Records

* Total Visit Records: 6785
* Total Unique Children: 3041

### Features Used

* Child ID
* Visit Date
* Age (Months)
* MUAC
* Previous MUAC
* MUAC Change
* Visit Number
* Nutrition Condition
* Cluster Information
* Month Gap

---

## Project Workflow

### 1. Data Cleaning

Input:

* Raw GMP Dataset

Output:

* cleaned_data.csv

### 2. Nutrition Condition Classification

MUAC-based classification:

* Good: MUAC ≥ 13.5
* At Risk: 12.5 – 13.49
* Moderate: 11.5 – 12.49
* Severe: MUAC < 11.5

Output:

* condition_data.csv

### 3. K-Means Clustering

Model:

* KMeans (n_clusters=3)

Cluster Labels:

* Healthy
* Moderate Risk
* High Risk

Output:

* clustered_data.csv

### 4. Trend Analysis

Children with at least two visits were analyzed.

Results:

* Improved Children: 717
* Deteriorated Children: 349
* Stable Children: 270

Output:

* trend_analysis.csv
* trend_ready_data.csv

### 5. Future Condition Prediction

Model:

* Random Forest Classifier

Target:

* Next_Condition

Additional Features:

* Previous_MUAC
* MUAC_Change
* Month_Gap

Prediction Output:

* Future Nutrition Condition
* Confidence Score
* Class Probabilities
* Nutrition Recommendation

---

## Machine Learning Model

### Algorithm

Random Forest Classifier

### Features

* MUAC
* Age_Months
* Visit_Number
* Cluster
* Previous_MUAC
* MUAC_Change
* Condition_Enc
* Month_Gap

### Target

* Next_Condition

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Jupyter Notebook

---

## Key Findings

* Total Children Analyzed: 3041
* Children with Multiple Visits: 1336
* Improved Children: 717
* Deteriorated Children: 349
* Stable Children: 270

The trend analysis findings provide valuable insights into child nutrition progress and risk patterns.

---

## Repository Structure

```text
01_Data_Cleaning.ipynb
02_Condition_Classification.ipynb
03_KMeans_Clustering.ipynb
04_Trend_Analysis.ipynb
05_Future_Condition_Prediction.ipynb

data/
models/
outputs/
```

---

## Author

Khadiza Akter Konok

AI Engineer Intern
Save the Children Bangladesh
