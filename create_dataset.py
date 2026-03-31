import pandas as pd
import os

data = {
    'Year': list(range(2001, 2024)),
    'Private_Vehicles_Registered_Millions': [
        54.99, 58.90, 67.01, 72.10, 78.50, 85.00, 94.06, 105.32,
        114.95, 127.74, 141.90, 159.49, 176.74, 190.79, 210.00,
        230.00, 253.00, 278.00, 295.00, 310.00, 295.00, 305.00, 320.00
    ],
    'Public_Transport_Share_Percent': [
        34.2, 33.8, 33.1, 32.5, 31.9, 31.2, 30.5, 29.8,
        29.1, 28.7, 28.2, 28.0, 28.3, 28.8, 29.5,
        30.2, 31.0, 32.1, 33.5, 34.2, 35.8, 37.1, 38.5
    ],
    'Metro_Cities_With_Metro_Rail': [
        0, 1, 1, 1, 1, 2, 2, 2,
        3, 4, 5, 6, 7, 8, 9,
        10, 11, 13, 15, 17, 18, 19, 20
    ],
    'Metro_Ridership_Million_Trips': [
        0, 18, 20, 22, 25, 55, 60, 68,
        120, 180, 350, 480, 620, 780, 950,
        1100, 1300, 1550, 1800, 2100, 1600, 1900, 2300
    ],
    'Fuel_Price_Petrol_Rs_per_L': [
        27.0, 29.0, 33.0, 35.0, 40.0, 47.0, 50.0, 52.0,
        45.0, 48.0, 58.0, 63.0, 66.0, 72.0, 60.0,
        65.0, 73.0, 75.0, 80.0, 91.0, 95.0, 105.0, 102.0
    ],
    'GDP_Growth_Rate_Percent': [
        5.4, 3.8, 7.9, 7.8, 9.3, 9.3, 9.3, 6.7,
        3.9, 8.4, 10.3, 6.6, 5.5, 6.4, 7.4,
        8.2, 7.1, 6.1, 6.1, 4.2, -6.6, 8.7, 7.2
    ]
}

df = pd.DataFrame(data)
os.makedirs('data', exist_ok=True)
df.to_csv('data/india_transport_modal_shift.csv', index=False)
print("✅ Dataset created successfully!")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")