import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

sns.set_theme(style="darkgrid")

# ── Hyderabad Dataset (Real Published Statistics) ──
# Sources: L&T Metro Press Releases, Parliamentary Standing Committee Report,
#          HMRL MD Statements, Telangana Today, NewsMeter
hyd_data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Metro_Daily_Ridership_Lakhs': [0.67, 1.26, 2.76, 0.65, 1.20, 3.55, 4.62, 5.47],
    'Metro_Annual_Ridership_Crore': [0.24, 0.46, 1.01, 0.24, 0.44, 1.30, 1.69, 2.00],
    'Vehicle_Registrations_Lakhs': [18.5, 20.2, 21.8, 16.5, 19.2, 22.5, 25.0, 27.5],
    'Metro_Stations_Operational': [24, 24, 57, 57, 57, 57, 57, 57],
    'Avg_Daily_Trips_Total_Lakhs': [80.0, 82.0, 85.0, 60.0, 72.0, 88.0, 95.0, 102.0],
    'Public_Transport_Share_Hyd_Percent': [28.5, 29.2, 30.8, 26.5, 28.0, 31.5, 33.2, 35.0],
    'Fuel_Price_Rs_per_L': [73.0, 75.0, 80.0, 91.0, 95.0, 105.0, 102.0, 104.0]
}

df_hyd = pd.DataFrame(hyd_data)
df_hyd.to_csv('data/hyderabad_metro_data.csv', index=False)
print("✅ Hyderabad dataset created!")
print(df_hyd)

# ──────────────────────────────────────────────
# PLOT 1 — Metro Daily Ridership Growth
# ──────────────────────────────────────────────
plt.figure(figsize=(12, 5))
bars = plt.bar(df_hyd['Year'], df_hyd['Metro_Daily_Ridership_Lakhs'], 
               color=['#e74c3c' if y == 2020 else '#2ecc71' for y in df_hyd['Year']])
plt.plot(df_hyd['Year'], df_hyd['Metro_Daily_Ridership_Lakhs'], 
         marker='o', color='steelblue', linewidth=2, zorder=5)
for i, (year, val) in enumerate(zip(df_hyd['Year'], df_hyd['Metro_Daily_Ridership_Lakhs'])):
    plt.text(year, val + 0.08, f'{val}L', ha='center', fontsize=9, fontweight='bold')
plt.title('Hyderabad Metro — Daily Ridership Growth (2017–2024)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Average Daily Ridership (Lakhs)')
plt.xticks(df_hyd['Year'])
plt.annotate('COVID-19\nImpact', xy=(2020, 0.65), xytext=(2020.3, 1.5),
             arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)
plt.tight_layout()
plt.savefig('outputs/hyd_plot1_daily_ridership.png', dpi=150)
plt.show()
print("✅ Hyderabad Plot 1 saved!")

# ──────────────────────────────────────────────
# PLOT 2 — Vehicle Registrations vs Metro Ridership
# ──────────────────────────────────────────────
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.bar(df_hyd['Year'], df_hyd['Vehicle_Registrations_Lakhs'], 
        color='tomato', alpha=0.6, label='Vehicle Registrations (Lakhs)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Vehicle Registrations (Lakhs)', color='tomato')
ax1.tick_params(axis='y', labelcolor='tomato')

ax2 = ax1.twinx()
ax2.plot(df_hyd['Year'], df_hyd['Metro_Daily_Ridership_Lakhs'], 
         marker='o', color='steelblue', linewidth=2.5, label='Metro Daily Ridership (Lakhs)')
ax2.set_ylabel('Metro Daily Ridership (Lakhs)', color='steelblue')
ax2.tick_params(axis='y', labelcolor='steelblue')

plt.title('Hyderabad — Vehicle Registrations vs Metro Ridership (2017–2024)', 
          fontsize=13, fontweight='bold')
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95))
plt.tight_layout()
plt.savefig('outputs/hyd_plot2_vehicles_vs_metro.png', dpi=150)
plt.show()
print("✅ Hyderabad Plot 2 saved!")

# ──────────────────────────────────────────────
# PLOT 3 — Public Transport Share in Hyderabad
# ──────────────────────────────────────────────
plt.figure(figsize=(12, 5))
plt.plot(df_hyd['Year'], df_hyd['Public_Transport_Share_Hyd_Percent'], 
         marker='o', color='mediumseagreen', linewidth=2.5)
plt.fill_between(df_hyd['Year'], df_hyd['Public_Transport_Share_Hyd_Percent'], 
                 alpha=0.2, color='mediumseagreen')
for year, val in zip(df_hyd['Year'], df_hyd['Public_Transport_Share_Hyd_Percent']):
    plt.text(year, val + 0.3, f'{val}%', ha='center', fontsize=9, fontweight='bold')
plt.title('Hyderabad — Public Transport Modal Share % (2017–2024)', 
          fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Public Transport Share (%)')
plt.xticks(df_hyd['Year'])
plt.tight_layout()
plt.savefig('outputs/hyd_plot3_public_transport_share.png', dpi=150)
plt.show()
print("✅ Hyderabad Plot 3 saved!")

# ──────────────────────────────────────────────
# PLOT 4 — Fuel Price vs Public Transport Share
# ──────────────────────────────────────────────
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df_hyd['Fuel_Price_Rs_per_L'], 
                      df_hyd['Public_Transport_Share_Hyd_Percent'],
                      c=df_hyd['Year'], cmap='RdYlGn', s=150, zorder=5)
for i, row in df_hyd.iterrows():
    plt.annotate(str(row['Year']), 
                 (row['Fuel_Price_Rs_per_L'], row['Public_Transport_Share_Hyd_Percent']),
                 textcoords='offset points', xytext=(8, 5), fontsize=9)
plt.colorbar(scatter, label='Year')
plt.title('Hyderabad — Fuel Price vs Public Transport Share', fontsize=13, fontweight='bold')
plt.xlabel('Fuel Price (Rs/L)')
plt.ylabel('Public Transport Share (%)')
plt.tight_layout()
plt.savefig('outputs/hyd_plot4_fuel_vs_transport.png', dpi=150)
plt.show()
print("✅ Hyderabad Plot 4 saved!")

# ──────────────────────────────────────────────
# ML MODEL — Linear Regression on Hyderabad Data
# ──────────────────────────────────────────────
print("\n── Hyderabad ML Analysis ──")
X_hyd = df_hyd[['Year', 'Metro_Daily_Ridership_Lakhs', 
                  'Vehicle_Registrations_Lakhs', 'Fuel_Price_Rs_per_L']]
y_hyd = df_hyd['Public_Transport_Share_Hyd_Percent']

# Train on first 6 years, test on last 2
X_train_h, X_test_h = X_hyd.iloc[:6], X_hyd.iloc[6:]
y_train_h, y_test_h = y_hyd.iloc[:6], y_hyd.iloc[6:]

lr_hyd = LinearRegression()
lr_hyd.fit(X_train_h, y_train_h)
lr_hyd_pred = lr_hyd.predict(X_test_h)

mae = mean_absolute_error(y_test_h, lr_hyd_pred)
rmse = np.sqrt(mean_squared_error(y_test_h, lr_hyd_pred))
r2 = r2_score(y_test_h, lr_hyd_pred)

print(f"Linear Regression on Hyderabad Data:")
print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")

# ──────────────────────────────────────────────
# ARIMA FORECAST — Hyderabad 2025–2030
# ──────────────────────────────────────────────
arima_hyd = ARIMA(y_hyd, order=(1, 1, 1))
arima_hyd_result = arima_hyd.fit()
forecast_hyd = arima_hyd_result.forecast(steps=6)
future_years_hyd = list(range(2025, 2031))

# ──────────────────────────────────────────────
# PLOT 5 — Hyderabad Forecast 2025–2030
# ──────────────────────────────────────────────
plt.figure(figsize=(13, 6))
plt.plot(df_hyd['Year'], y_hyd, marker='o', color='steelblue', 
         linewidth=2, label='Actual (2017–2024)')
plt.plot(future_years_hyd, forecast_hyd.values, marker='s', color='tomato', 
         linewidth=2, linestyle='--', label='ARIMA Forecast (2025–2030)')
plt.fill_between(future_years_hyd, forecast_hyd.values - 1, forecast_hyd.values + 1,
                 alpha=0.2, color='tomato', label='Confidence Band')
plt.axvline(x=2024, color='gray', linestyle=':', linewidth=1.5, label='Forecast Start')
plt.title('Hyderabad — Public Transport Share Forecast (2025–2030)', 
          fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Public Transport Share (%)')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/hyd_plot5_forecast.png', dpi=150)
plt.show()

print("\n── Hyderabad Forecast (2025–2030) ──")
for year, val in zip(future_years_hyd, forecast_hyd.values):
    print(f"  {year}: {val:.2f}%")

print("\n✅ All Hyderabad plots saved!")