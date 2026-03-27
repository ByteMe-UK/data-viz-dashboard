# 🌍 Global COVID-19 Interactive Dashboard

An interactive data dashboard that visualises the **global COVID-19 pandemic** with 6 chart types, real-time data from Our World in Data, and continent/country-level filtering — built with **Python**, **Streamlit**, and **Plotly**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-6.0+-3F4F75?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Demo

> 🔗 **[Open Dashboard on Streamlit Cloud](https://byteme-uk-data-viz-dashboard.streamlit.app)** _(deploy link will be active after setup)_

## 📸 Screenshots

> _Screenshots will be added after deployment_

## ✨ Features

- 🗺️ **World Choropleth Map** — colour-coded by any metric
- 📈 **Time-Series Trends** — track selected countries over time
- 🏆 **Top N Bar Chart** — see which countries lead in any metric
- 🍩 **Continent Donut Chart** — breakdown by region
- 📉 **Daily Area Chart** — stacked daily new cases/deaths
- 💰 **GDP Scatter Plot** — GDP per capita vs COVID metrics (bubble = population)
- 🦠 **KPI Cards** — total cases, deaths, vaccinations, countries tracked
- 🎛️ **Interactive Filters** — continent, country, metric, and top-N controls

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.10+ | Core language |
| Streamlit | Web framework & deployment |
| Plotly | Interactive visualisations |
| Pandas | Data wrangling |
| OWID Dataset | COVID-19 data source |

## 📦 Getting Started

```bash
# Clone the repo
git clone https://github.com/ByteMe-UK/data-viz-dashboard.git
cd data-viz-dashboard

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then visit `http://localhost:8501` in your browser.

## 📁 Project Structure

```
data-viz-dashboard/
├── app.py                     ← Main Streamlit dashboard
├── requirements.txt           ← Python dependencies
├── .streamlit/
│   └── config.toml            ← Streamlit theme & config
├── data/
│   ├── __init__.py
│   └── loader.py              ← Data fetching & caching (OWID)
├── components/
│   ├── __init__.py
│   ├── charts.py              ← 6 Plotly chart functions
│   └── metrics.py             ← KPI metric cards
├── LICENSE
└── README.md
```

## 🚢 Deployment

This app is deployed for **free** on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select `ByteMe-UK/data-viz-dashboard` → `main` → `app.py`
5. Click **Deploy** — done!

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Part of the [ByteMe-UK](https://github.com/ByteMe-UK) portfolio collection.**
