# Predicting Fantasy Premier League Total Player Season Points & Identifying Budget Assets

- **Author:** Chukwuebuka Ozoh, chukkyozoh@gmail.com
- * *This work was realized as part of the capstone project of the MS in Data Science at Pace University.*


* **Overview:** 
- Fantasy Premier League (FPL) managers juggle a £100 m budget to assemble a 15-man squad of Premier League stars.
- Every player earns points each gameweek for goals, assists, clean sheets, minutes played and bonus points.
- But how do you spot the best bargains, the players who deliver the most points for every million spent?

This project uses **2023–24 FPL season data** and a handful of core metrics to:

- **Predict total season points** for each player via Linear Regression, Random Forest and XGBoost.  
- **Compute a “value score”** (total points ÷ cost in £ m) to rank cost-effectiveness.  
- **Identify the Top-N value picks** across all positions (MID, DEF, GKP, FWD).  
- **Visualize key insights** with correlation heatmaps, scatterplots and actual-vs-predicted charts.  
- **Provide an interactive Streamlit dashboard** so managers can filter by position, price range and view the best budget targets at a glance.

Whether you’re a data scientist or an FPL fanatic, this repo offers a clear, data-driven roadmap to building a high-scoring, budget-friendly squad.


- **Structure:**
  1. `data/` – [Sourced from Kaggle](https://www.kaggle.com/datasets/meraxes10/fantasy-premier-league-dataset-2023-2024)  
  2. `notebooks/` – EDA & modeling  
  3. `app.py` – Streamlit dashboard  
  4. `presentation.pptx` – final slides  
- **Installation:**
  ```bash
  pip install -r requirements.txt
