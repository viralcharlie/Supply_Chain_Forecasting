Automated Holt’s Linear Trend Forecasting for Supply Chain Data
Project Overview
This project automates the process of selecting the best smoothing parameters (alpha and beta) for Holt’s Linear Trend Method, ensuring an optimal balance between accuracy and forecast stability. The script loops through different values of alpha and beta, selects the best fit based on MAPE (Mean Absolute Percentage Error), and visualizes the results.

Key Features
✅ Automated selection of best alpha and beta values
✅ Loops through multiple products in the dataset
✅ Filters results within 10-20% MAPE for reliability
✅ Generates and saves forecasts as visual plots
✅ Exports best alpha and beta values to a CSV file

Files in This Repository
📂 Automating_best_model.py – Python script that automates the forecasting process
📂 best_alpha_beta.csv – CSV file containing the best alpha and beta values for each product
📂 forecast_plots/ – Folder containing sample forecast images

How It Works
1️⃣ Load the dataset from an Excel file
2️⃣ Ensure Date is in datetime format and set it as the index
3️⃣ Define alpha and beta ranges (from 0.1 to 1.0)
4️⃣ Train Holt’s model for each product in the dataset
5️⃣ Select the best alpha-beta combination based on the lowest MAPE (10%-20%)
6️⃣ Generate forecast plots and save the results
7️⃣ Export best parameters to CSV

Usage
To Run the Script
Make sure you have the required Python libraries installed:
pip install pandas numpy matplotlib statsmodels

Then, run the script
python Automating_best_model.py

Interpreting Results
The best_alpha_beta.csv file shows the optimal parameters for each product.
The generated plots visualize the actual vs. forecasted values.
The script helps in automating demand forecasting in supply chain analytics.

Future Improvements
🔹 Extend to other forecasting models like ARIMA or Exponential Smoothing
🔹 Incorporate seasonal adjustments for more complex datasets
🔹 Deploy as a web application for interactive forecasting

Author
Aromeh Barnabas Charles
viralcharlie007@gmail.com
Happy Forecasting! 
