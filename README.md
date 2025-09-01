# Maximizing Website Engagement: Predicting Recipe Popularity

A **data-driven approach at Tasty Bytes** to optimize homepage recipe selection and boost website traffic.  

---

## 📌 Problem Statement

- **Current Situation:** Homepage recipes are manually selected based on preference. Popular recipes can increase traffic by **up to 40%**, leading to higher engagement and subscriptions.  
- **Business Need:** Product team requires a **data-driven model** to predict which recipes will attract high traffic.  
- **Goal:** Build a model that identifies high-traffic recipes with **≥80% precision** to optimize homepage selection.  

---

## 📂 Dataset

- **Source:** Provided CSV (`recipe_site_traffic_2212.csv`)  
- **Rows:** 947 (after cleaning: 895)  
- **Columns (8):**  
  - `recipe` (ID)  
  - `calories`  
  - `carbohydrate`  
  - `sugar`  
  - `protein`  
  - `category` (10 groups)  
  - `servings`  
  - `high_traffic` (binary target: True = high traffic, False = low traffic)  

**Data Cleaning Steps:**  
- Dropped 52 rows missing all nutritional values.  
- Converted `high_traffic` to boolean (`True` / `False`).  
- Cleaned `servings` (removed text, ensured numeric).  
- Standardized categories (merged “Chicken Breast” → “Chicken”).  

---

## 📊 Exploratory Data Analysis

- **Distributions:** Calories, carbs, protein, and sugar were **right-skewed**, requiring transformation.  
- **Category Insights:**  
  - **Vegetables** → 98.7% high-traffic rate  
  - **Potato** and **Pork** also strong performers  
  - **Beverages** → lowest engagement (5.4%)  
- **Takeaway:** Category is a strong predictor; nutrition features add marginal predictive value but may contribute via interactions.  

---

## 🧠 Modeling Approach

- **Problem Type:** Binary Classification  
- **Baseline Model:** Logistic Regression  
- **Comparison Model:** Support Vector Machine (SVM)  

**Preprocessing:**  
- One-hot encoding for `category`  
- **Yeo-Johnson transformation** on skewed numeric features  
- Min-Max scaling for numerical columns  

---

## 📈 Results

| Model                | Accuracy | Precision (High) | HTPR (True ÷ False Positives) |
|----------------------|----------|------------------|--------------------------------|
| Logistic Regression  | 79%      | 0.83             | 4.84                           |
| Support Vector Machine | 80%      | **0.84**         | **5.41**                       |

- Both models met the business threshold (**HTPR ≥ 4.0 ≈ 80% precision**).  
- **SVM outperformed Logistic Regression**, achieving slightly higher precision and confidence in identifying high-traffic recipes.  

---

## 📊 Business KPI

- **High Traffic Precision Ratio (HTPR):**  
  \[
  HTPR = \frac{\text{True Positives}}{\text{False Positives}}
  \]  
- **Threshold:** ≥ 4.0 (≈ 80% precision)  
- **Achieved:**  
  - Logistic Regression = 4.84  
  - SVM = 5.41  

---

## ✅ Recommendations

1. **Deploy the SVM model** for homepage recipe selection.  
2. Prioritize **Vegetable, Potato, and Pork** recipes; minimize Beverages.  
3. Establish a **feedback loop** to retrain the model with new traffic data.  
4. Collect **richer features** (e.g., user ratings, seasonality, images) for continuous improvement.  

---


---

## 🙌 Acknowledgments

- Project brief adapted from *Practical DSP: Recipe Site Traffic* assessment.  
- Analysis and presentation created for **Tasty Bytes** product team.
