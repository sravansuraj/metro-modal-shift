Mode of Travel Shift Analysis from Private to Public Transport 🚇

  Student:   Sravan Suraj Chunduru  
  Project Lead:   Dr. Shivani Yadao, Associate Professor  
  Submission Deadline:   15th April 2026  
---

## 📌 Project Overview
This project analyzes the modal shift from private to public transport in India 
using 23 years of data (2001–2023). Three machine learning models are implemented 
and compared to predict public transport share and forecast future trends through 2030.
---

## 🎯 Objective
- Analyze trends in private vs public transport usage in India
- Identify key drivers of modal shift (metro expansion, fuel prices, GDP)
- Compare ML models for predicting public transport share
- Forecast public transport adoption through 2030
---

## 📁 Project Structure
metro_modal_shift/
├── data/
│   └── india_transport_modal_shift.csv    ← Main dataset (2001–2023)
├── notebooks/
│   ├── day1_eda.ipynb                     ← EDA and visualizations
│   └── day2_models.ipynb                  ← ML models and comparison
├── outputs/
│   ├── plot1_private_vehicles.png
│   ├── plot2_public_transport_share.png
│   ├── plot3_metro_ridership.png
│   ├── plot4_private_vs_public.png
│   ├── plot5_correlation_heatmap.png
│   ├── plot6_model_comparison.png
│   ├── plot7_metrics_comparison.png
│   ├── plot8_future_forecast.png
│   ├── dashboard.html                     ← Interactive dashboard
│   └── IEEE_Research_Paper_Sravan.docx    ← IEEE format research paper
├── create_dataset.py                      ← Dataset generation script
├── dashboard.py                           ← Dashboard generation script
├── generate_ieee_paper.py                 ← IEEE paper generation script
├── day1_documentation.md                  ← Day 1 detailed documentation
├── day2_documentation.md                  ← Day 2 detailed documentation
└── README.md                              ← This file


---

## 📊 Dataset
| Column | Description | Unit |
|---|---|---|
| Year | Year of observation | Year |
| Private_Vehicles_Registered_Millions | Total private vehicles registered | Millions |
| Public_Transport_Share_Percent | % of travel via public transport | % |
| Metro_Cities_With_Metro_Rail | Cities with operational metro | Count |
| Metro_Ridership_Million_Trips | Total metro trips | Million Trips |
| Fuel_Price_Petrol_Rs_per_L | Average petrol price | Rs/L |
| GDP_Growth_Rate_Percent | India GDP growth rate | % |


## 🤖 Models Used

| Model | MAE | RMSE | R² Score |
|---|---|---|---|
| Linear Regression | 0.4865 | 0.5719 | 0.9217 |
| Random Forest | 0.9222 | 0.9863 | 0.7672 |
|   ARIMA (2,1,2)   ✅ |   0.3098   |   0.3788   |   0.9574   |

  Best Model: ARIMA   — lowest error, highest accuracy


## 🔮 Forecast (2024–2030)

| Year | Public Transport Share |
|---|---|
| 2024 | 39.92% |
| 2025 | 41.34% |
| 2026 | 42.69% |
| 2027 | 43.97% |
| 2028 | 45.16% |
| 2029 | 46.26% |
| 2030 | 47.27% |

---

## 🛠️ How to Run

  1. Clone the repository:  

  2. Install dependencies:  

  3. Generate dataset:  

  4. Run EDA notebook:  

  5. Run ML models notebook:  

  6. Generate dashboard:  

python dashboard.py

  7. Generate IEEE paper:  

python generate_ieee_paper.py


## 📈 Key Findings
1. Private vehicle registrations grew 6x from 2001 to 2023
2. Public transport share hit lowest point (28%) in 2012 before recovering
3. Metro expansion to 20 cities was the biggest driver of modal shift
4. Fuel price hikes strongly correlate with public transport adoption (r=0.82)
5. ARIMA forecasts public transport share reaching 47.27% by 2030


## 📄 Deliverables
- ✅ Working Python code on GitHub
- ✅ Interactive dashboard (outputs/dashboard.html)
- ✅ IEEE format research paper (outputs/IEEE_Research_Paper_Sravan.docx)
- ✅ 3-algorithm comparative analysis with metrics
- ✅ Day 1 & Day 2 documentation
- ⬜ Project report (signed by Dr. Shivani Yadao)
- ⬜ Spiral bound hardcopy

## 🔗 References
1. Ministry of Road Transport and Highways — Road Transport Yearbook 2022–23
2. Delhi Metro Rail Corporation — DMRC Annual Report 2022–23
3. World Bank — India GDP Growth Rate Data
