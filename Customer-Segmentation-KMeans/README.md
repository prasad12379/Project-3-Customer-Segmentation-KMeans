# Customer Segmentation Using K-Means Clustering

A machine learning project that segments customers into distinct groups based on their **Annual Income** and **Spending Score** using **K-Means clustering**.

## Project Overview
This model segments customers of a mall based on their income and spending behavior. It helps businesses:
- Understand customer demographics and purchasing patterns.
- Tailor marketing strategies for different customer groups.
- Optimize resource allocation for maximum ROI.

## Dataset
**File:** `Mall_Customers.csv`  
**Observations:** 200 customers  
**Features:**
- `CustomerID` - Unique identifier
- `Genre` - Gender (Male/Female)
- `Age` - Customer age
- `Annual Income (k$)` - Income in thousands of dollars
- `Spending Score (1-100)` - Mall’s spending rating  


## What I Did
1. **Data Exploration & Preprocessing**  
   - Loaded and analyzed the dataset.
   - Selected relevant features: `Annual Income` and `Spending Score`.
2. **Clustering Analysis**  
   - Applied the **Elbow Method** to determine optimal clusters (K=5).
   - Implemented **K-Means Clustering** to segment customers.
3. **Visualization**  
   - Plotted clusters and centroids for intuitive insights.

## Results
- **5 distinct customer segments** identified:
  - **High Income, Low Spenders**
  - **Moderate Income, Moderate Spenders**
  - **High Income, High Spenders** (Target for luxury offers)
  - **Low Income, High Spenders** (Budget-sensitive)
  - **Low Income, Low Spenders**


## Tech Stack
- **Language:** Python
- **Libraries:**  
  - Pandas, NumPy (Data handling)  
  - Scikit-learn (K-Means, Elbow Method)  
  - Matplotlib (Visualizations)  

## Files Included
- `customer_segmentation.py` - Full clustering pipeline.
- `Mall_Customers.csv` - Dataset.
- `README.md` - Project documentation.

## � Business Impact
- Enables **personalized marketing** (e.g., discounts for high spenders).
- Improves customer retention by understanding behavior.
- Guides inventory planning based on income clusters.

## Author
**Prasad Dhokane**  
- 📧 Email: [prasaddhokane9@gmail.com](prasaddhokane9@gmail.com)  
- 🔗 LinkedIn: [Prasad Dhokane](www.linkedin.com/in/prasad-dhokane-58487728a)  

