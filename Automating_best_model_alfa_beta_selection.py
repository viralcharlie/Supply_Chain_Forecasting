import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import Holt

# Load the dataset
data_path = r'C:\Users\Barnabas\Desktop\for auto.xlsx'
df = pd.read_excel(data_path)

# Ensure date column is in datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%b')
df.set_index('Date', inplace=True)
df = df.asfreq('ME')  # Set frequency to Monthly
# Define alpha and beta ranges
alpha_values = np.arange(0.1, 1.0, 0.1)  # Step size of 0.1
beta_values = np.arange(0.1, 1.0, 0.1)

# Function to calculate MAPE
def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# Store best parameters
best_params = []

# Loop through each product column
for product in df.columns:
    best_alpha, best_beta, best_mape = None, None, float('inf')
    best_forecast = None
    train = df[product].iloc[:-3]  # Use all but last 3 months as training
    test = df[product].iloc[-3:]  # Last 3 months for testing
    
    for alpha in alpha_values:
        for beta in beta_values:
            try:
                model = Holt(train).fit(smoothing_level=alpha, smoothing_trend=beta)
                forecast = model.forecast(len(test))
                mape = mean_absolute_percentage_error(test, forecast)
                
                if 10 <= mape <= 20 and mape < best_mape:  # Keeping within 10-20% MAPE
                    best_alpha, best_beta, best_mape = alpha, beta, mape
                    best_forecast = forecast
                    print(f"Product: {product}, Alpha: {alpha}, Beta: {beta}, MAPE: {mape:.2f}")

            except:
                continue
    
    if best_alpha and best_beta:
        best_params.append([product, best_alpha, best_beta, best_mape])
        print(f"Best parameters found for {product}: {best_alpha}, {best_beta}, MAPE: {best_mape}")

        
        # Plot results
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df[product], label='Actual Data', marker='o')
        plt.plot(test.index, best_forecast, label=f'Forecast (α={best_alpha}, β={best_beta})', linestyle='--')
        plt.title(f'Forecast for {product}')
        plt.legend()
        plt.show()
print(f"Testing α={alpha}, β={beta} for {product}")
print(f"MAPE: {mape}")

# Save best alpha and beta values to CSV
best_params_df = pd.DataFrame(best_params, columns=['Product', 'Alpha', 'Beta', 'MAPE'])
output_csv_path = '/mnt/data/best_alpha_beta.csv'
best_params_df.to_csv(output_csv_path, index=False)

print(f"Best alpha and beta values saved to {output_csv_path}")
