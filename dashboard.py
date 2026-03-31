import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings('ignore')

# ── Load Data ──
df = pd.read_csv('data/india_transport_modal_shift.csv')

# ── ARIMA Forecast ──
y = df['Public_Transport_Share_Percent']
arima_model = ARIMA(y, order=(2, 1, 2))
arima_result = arima_model.fit()
future_steps = 7
forecast = arima_result.forecast(steps=future_steps)
future_years = list(range(2024, 2031))

# ── Create Dashboard ──
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        '1. Private Vehicle Registrations (2001–2023)',
        '2. Public Transport Share % (2001–2023)',
        '3. Metro Ridership Growth (2001–2023)',
        '4. Private vs Public Transport Trend',
        '5. Fuel Price vs Public Transport Share',
        '6. ARIMA Forecast (2024–2030)'
    ),
    vertical_spacing=0.12,
    horizontal_spacing=0.1
)

# Plot 1 — Private Vehicles
fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Private_Vehicles_Registered_Millions'],
    mode='lines+markers', name='Private Vehicles (M)',
    line=dict(color='tomato', width=2),
    marker=dict(size=6)
), row=1, col=1)

# Plot 2 — Public Transport Share
fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Public_Transport_Share_Percent'],
    mode='lines+markers', name='Public Transport Share %',
    line=dict(color='steelblue', width=2),
    marker=dict(size=6)
), row=1, col=2)

# Plot 3 — Metro Ridership
fig.add_trace(go.Bar(
    x=df['Year'], y=df['Metro_Ridership_Million_Trips'],
    name='Metro Ridership (M Trips)',
    marker_color='mediumseagreen'
), row=2, col=1)

# Plot 4 — Private vs Public
fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Private_Vehicles_Registered_Millions'],
    mode='lines+markers', name='Private Vehicles',
    line=dict(color='tomato', width=2)
), row=2, col=2)
fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Public_Transport_Share_Percent'],
    mode='lines+markers', name='Public Transport %',
    line=dict(color='steelblue', width=2, dash='dash'),
    yaxis='y4'
), row=2, col=2)

# Plot 5 — Fuel Price vs Public Transport
fig.add_trace(go.Scatter(
    x=df['Fuel_Price_Petrol_Rs_per_L'], y=df['Public_Transport_Share_Percent'],
    mode='markers', name='Fuel vs Public Transport',
    marker=dict(color='darkorange', size=8),
    text=df['Year']
), row=3, col=1)

# Plot 6 — ARIMA Forecast
fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Public_Transport_Share_Percent'],
    mode='lines+markers', name='Actual (2001–2023)',
    line=dict(color='steelblue', width=2)
), row=3, col=2)
fig.add_trace(go.Scatter(
    x=future_years, y=forecast.values,
    mode='lines+markers', name='Forecast (2024–2030)',
    line=dict(color='tomato', width=2, dash='dash'),
    marker=dict(size=8)
), row=3, col=2)

# ── Layout ──
fig.update_layout(
    title=dict(
        text='<b>Mode of Travel Shift Analysis — India (2001–2030)</b><br>'
             '<sup>Sravan Suraj Chunduru | Project Lead: Dr. Shivani Yadao</sup>',
        font=dict(size=18),
        x=0.5
    ),
    height=1100,
    showlegend=True,
    legend=dict(orientation='h', yanchor='bottom', y=-0.08, xanchor='center', x=0.5),
    template='plotly_white'
)

# Update axes labels
fig.update_xaxes(title_text='Year', row=1, col=1)
fig.update_yaxes(title_text='Vehicles (Millions)', row=1, col=1)
fig.update_xaxes(title_text='Year', row=1, col=2)
fig.update_yaxes(title_text='Share (%)', row=1, col=2)
fig.update_xaxes(title_text='Year', row=2, col=1)
fig.update_yaxes(title_text='Million Trips', row=2, col=1)
fig.update_xaxes(title_text='Year', row=2, col=2)
fig.update_xaxes(title_text='Fuel Price (Rs/L)', row=3, col=1)
fig.update_yaxes(title_text='Public Transport Share (%)', row=3, col=1)
fig.update_xaxes(title_text='Year', row=3, col=2)
fig.update_yaxes(title_text='Share (%)', row=3, col=2)

# ── Save ──
fig.write_html('outputs/dashboard.html')
print("✅ Dashboard saved to outputs/dashboard.html")
fig.show()